#!/usr/bin/env python3
"""One-time migration of the old WordPress site (picsl.upenn.edu) into this Jekyll site.

Scrapes the public pages listed in the WordPress sitemaps, converts their content to
Markdown, downloads uploaded media into images/wp/, and writes member pages, software
pages, research pages and _data/projects.yaml. Every generated file carries a
redirect_from entry for its old URL.

Pages that fail on the live site (several return a WordPress "critical error") are taken
from the Wayback Machine instead. Fetched pages are cached in .migrate_cache/, so the
script can be re-run cheaply after changing it.

Usage: python tools/migrate_wp.py [--root .]
Requires: requests, beautifulsoup4, markdownify, pyyaml
"""

import argparse
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

SITE = "https://picsl.upenn.edu"
SITEMAPS = ["wp-sitemap-posts-page-1.xml", "wp-sitemap-posts-post-1.xml"]
CACHE = Path(".migrate_cache")

# news-style posts that are not migrated
DROP_POSTS = {
    "itk-snap",
    "beta-version-of-itk-snap-3-0-is-released",
    "itk-snap-3-6-tutorial-available-online",
    "recent-camino-updates",
    "new-ants-documentation",
    "tustison-et-al-win-the-brats-challenge",
    "important-milestone-for-the-penn-ex-vivo-atlas-of-the-human-hippocampus-formation",
}

# pages that are not migrated (listing pages are replaced by template pages)
DROP_PAGES = {
    "/", "/sample-page/", "/posts/", "/research/", "/software/",
    "/people/", "/people/faculty-staff/", "/people/post-docs/",
    "/people/students/", "/people/alumni/", "/people/administrators/",
}

# WordPress slugs that need fixing
SLUG_FIX = {"295-2": "jue-wu", "gaylord-holder-2": "gaylord-holder", "min-chen-2": "min-chen"}

# role of each faculty/staff member; everyone else in that group is staff
PIS = {"jim-gee", "paul-yushkevich"}
FACULTY = {"philip-cook", "sandhitsu-sandy-das", "alison-pouch", "long-xie"}
GROUP_ROLE = {"post-docs": "postdoc", "students": "phd", "alumni": "alumni", "administrators": "staff"}

session = requests.Session()


def fetch(url, tries=5):
    for i in range(tries):
        r = session.get(url, timeout=60)
        if r.status_code not in (429, 503) or i == tries - 1:
            break
        time.sleep(30 * (i + 1))
    r.raise_for_status()
    return r


def wayback(url, kind="id_", valid=lambda r: True):
    """Fetch a snapshot of url from the Wayback Machine, trying older ones if needed.

    web/<year><kind>/<url> redirects to the snapshot closest to that year; the id_ and im_
    suffixes serve the original bytes without the Wayback toolbar or rewritten links.
    Recent snapshots of some pages are captures of the WordPress error page.
    """
    for year in ("2026", "2023", "2021", "2018", "2015"):
        try:
            r = fetch(f"https://web.archive.org/web/{year}{kind}/{url}")
        except requests.HTTPError:
            continue
        if valid(r):
            return r
    raise requests.HTTPError(f"no usable Wayback Machine snapshot of {url}")


def fetch_page(url):
    """Fetch page HTML, using the Wayback Machine if the live page is broken. Cached on disk."""
    key = CACHE / (re.sub(r"[^\w.-]+", "_", url) + ".html")
    if key.exists():
        return key.read_text()
    try:
        html = fetch(url).text
    except requests.HTTPError as e:
        html = wayback(url, valid=lambda r: "entry-title" in r.text or "masonrybox" in r.text).text
        print(f"  (live page failed with {e.response.status_code}, used Wayback Machine copy)")
    CACHE.mkdir(exist_ok=True)
    key.write_text(html)
    return html


def sitemap_urls():
    urls = []
    for sm in SITEMAPS:
        xml = fetch(f"{SITE}/{sm}").text
        urls += [(sm, u) for u in re.findall(r"<loc>([^<]+)</loc>", xml)]
    return urls


def classify(sitemap, url):
    """Return (kind, slug, out_path) or None if dropped."""
    path = urlparse(url).path
    parts = [p for p in path.split("/") if p]
    if "posts-post" in sitemap:
        slug = parts[-1]
        if slug in DROP_POSTS:
            return None
        return "research", slug, f"research/{slug}.md"
    if path in DROP_PAGES:
        return None
    if parts[0] == "people" and len(parts) == 3:
        slug = SLUG_FIX.get(parts[2], parts[2])
        return f"member:{parts[1]}", slug, f"_members/{slug}.md"
    if parts[0] == "software" and len(parts) == 2:
        return "software", parts[1], f"software/{parts[1]}.md"
    if parts[0] == "about":
        return "about", "about", "about/index.md"
    # remaining top-level pages (brain-function, brain-injury) are research areas
    return "area", parts[-1], f"research/{parts[-1]}.md"


class Media:
    """Downloads wp-content/uploads files into images/wp/ and maps old to new URLs."""

    def __init__(self, root):
        self.root = root
        self.done = {}

    def download(self, url):
        candidates = [url]
        # WordPress resized copies (name-300x200.png) are sometimes missing
        original = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", url)
        if original != url:
            candidates.append(original)
        for c in candidates:
            for get in (fetch, lambda u: wayback(u, "im_")):
                try:
                    return get(c).content
                except requests.RequestException:
                    pass
        return None

    def local(self, url):
        url = urljoin(SITE + "/", url).replace("http://", "https://")
        # some content still points at the site's old staging host
        url = url.replace("https://s1048127.instanturl.net/picslWP/", SITE + "/")
        m = re.search(r"/wp-content/uploads/(.+?)(?:\?.*)?$", url)
        if not m:
            return None
        rel = f"images/wp/{m.group(1)}"
        if url not in self.done:
            dest = self.root / rel
            if not dest.exists():
                data = self.download(url)
                if data is None:
                    print(f"  ! media not found: {url}", file=sys.stderr)
                    self.done[url] = None
                    return None
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(data)
            self.done[url] = rel
        return self.done[url]


def new_path(href, urlmap, members):
    """Return the new URL for an old internal link, or None if it isn't one we know."""
    p = urlparse(href)
    if p.netloc and not p.netloc.endswith("picsl.upenn.edu"):
        return None
    path = p.path if p.path.endswith("/") else p.path + "/"
    new = urlmap.get(path)
    # people moved between groups over time (e.g. students who became alumni)
    m = re.match(r"^/people/[^/]+/([^/]+)/$", path)
    if not new and m:
        slug = SLUG_FIX.get(m.group(1), m.group(1))
        new = f"/members/{slug}.html" if slug in members else None
    if new and p.fragment:
        new += f"#{p.fragment}"
    return new


def rewrite_links(soup, media, urlmap, members):
    for img in soup.find_all("img"):
        new = media.local(img.get("src", ""))
        if new:
            img["src"] = "/" + new
        for attr in ("srcset", "sizes", "width", "height", "class", "decoding", "loading", "fetchpriority"):
            img.attrs.pop(attr, None)
    for a in soup.find_all("a"):
        href = a.get("href", "")
        if "/wp-content/uploads/" in href:
            new = media.local(href)
        else:
            new = new_path(href, urlmap, members)
        if new:
            a["href"] = new if new.startswith("/") else "/" + new
    # lightbox wrappers: a link around just an image becomes the image
    for a in soup.find_all("a"):
        img = a.find("img")
        if img and len(a.contents) == 1 and a.get("href", "").startswith("/images/wp/"):
            a.replace_with(img)


def to_markdown(el):
    md = markdownify(str(el), heading_style="ATX", bullets="-")
    md = re.sub(r"[ \t]+\n", "\n", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    md = md.strip() + "\n"
    # keep Jekyll from interpreting liquid-like text in migrated content
    if "{{" in md or "{%" in md:
        md = "{% raw %}\n" + md + "{% endraw %}\n"
    return md


def front_matter(data):
    return "---\n" + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000) + "---\n\n"


def research_thumbnails():
    """Map post path -> thumbnail URL from the old Research page masonry grid."""
    thumbs = {}
    page = 1
    while True:
        url = f"{SITE}/research/" + (f"page/{page}/" if page > 1 else "")
        try:
            soup = BeautifulSoup(fetch_page(url), "html.parser")
        except requests.HTTPError:
            break
        new = 0
        for box in soup.select(".masonrybox"):
            a = box.find("a")
            img = box.find("img")
            if a and img:
                path = urlparse(a["href"]).path
                if path not in thumbs:
                    thumbs[path] = img["src"]
                    new += 1
        if not new:
            break
        page += 1
    return thumbs


def short_description(md, limit=220):
    text = md.replace("{% raw %}", "").replace("{% endraw %}", "")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"^#+ .*$", "", text, flags=re.M)
    text = " ".join(re.sub(r"[*_`>]", "", text).split())
    return text if len(text) <= limit else text[:limit].rsplit(" ", 1)[0] + "…"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", type=Path)
    args = ap.parse_args()
    root = args.root.resolve()
    media = Media(root)

    entries = []
    dropped = []
    failed = []
    for sm, url in sitemap_urls():
        c = classify(sm, url)
        if c is None:
            dropped.append(url)
        else:
            entries.append((url, *c))

    # old path -> new URL, for internal link rewriting
    urlmap = {}
    for url, kind, slug, out in entries:
        if kind.startswith("member"):
            new = f"/members/{slug}.html"
        elif out.endswith("index.md"):
            new = "/" + out[: -len("index.md")]
        else:
            new = "/" + out[:-3] + ".html"
        urlmap[urlparse(url).path] = new
    members = {slug for _, kind, slug, _ in entries if kind.startswith("member")}

    thumbs = research_thumbnails()
    projects = {"research": [], "software": [], "area": []}
    # WordPress id -> new URL, for ?page_id=N and ?p=N links
    ids = {}
    outputs = []

    for url, kind, slug, out in entries:
        print(f"{url} -> {out}")
        try:
            html = fetch_page(url)
        except requests.HTTPError as e:
            print(f"  ! skipped {url}: {e}", file=sys.stderr)
            failed.append(url)
            continue
        soup = BeautifulSoup(html, "html.parser")
        old_path = urlparse(url).path
        article = soup.select_one("article[id^=post-]")
        if article:
            ids[article["id"][len("post-"):]] = urlmap[old_path]
        title = soup.select_one("h1.entry-title").get_text(strip=True)
        body = soup.select_one(".entry-content")
        rewrite_links(body, media, urlmap, members)
        md = to_markdown(body)

        if kind.startswith("member"):
            group = kind.split(":")[1]
            thumb = soup.select_one(".personnel_thumbnail img")
            image = media.local(thumb["src"]) if thumb else None
            if group == "faculty-staff":
                role = "principal-investigator" if slug in PIS else "faculty" if slug in FACULTY else "staff"
            else:
                role = GROUP_ROLE[group]
            fm = {"name": title, "image": image or "images/fallback.svg", "role": role}
            if group == "alumni":
                fm["group"] = "alum"
        else:
            fm = {"title": title}
            posted = soup.select_one("time.entry-date")
            if kind == "research":
                fm["layout"] = "post"
                if posted:
                    fm["date"] = posted["datetime"][:10]
            if kind == "about":
                fm["nav"] = {"order": 1, "tooltip": "About PICSL"}
            image = None
            if old_path in thumbs:
                image = media.local(thumbs[old_path])
            if not image:
                first = re.search(r"!\[[^\]]*\]\(/(images/wp/[^)\s]+)", md)
                image = first.group(1) if first else None
            if kind in projects:
                item = {"title": title, "image": image or "images/fallback.svg",
                        "link": urlmap[old_path], "description": short_description(md)}
                if fm.get("date"):
                    item["date"] = fm["date"]
                projects[kind].append(item)
        # pages whose URL didn't change must not redirect to themselves
        if urlmap[old_path] != old_path:
            fm["redirect_from"] = [old_path]

        heading = "" if kind.startswith("member") or kind == "research" else f"# {title}\n\n"
        outputs.append((out, front_matter(fm) + heading + md))

    # resolve ?page_id=N / ?p=N links now that all ids are known
    def resolve_id(m):
        return f"({ids[m.group(1)]}" if m.group(1) in ids else m.group(0)

    id_link = re.compile(r"\((?:https?://picsl\.upenn\.edu)?/?\?(?:page_id|p)=(\d+)")
    for out, text in outputs:
        dest = root / out
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(id_link.sub(resolve_id, text))

    # projects data file: research posts newest first, then research areas, then software
    data = []
    for item in sorted(projects["research"], key=lambda p: p.get("date", ""), reverse=True):
        data.append({**item, "tags": ["research"]})
    for item in projects["area"]:
        data.append({**item, "group": "area", "tags": ["research"]})
    for item in projects["software"]:
        data.append({**item, "tags": ["software"]})
    (root / "_data/projects.yaml").write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000))

    print(f"\nCoverage: {len(outputs)} migrated, {len(dropped)} dropped, "
          f"{len(failed)} failed, {len([m for m in media.done.values() if m])} media files")
    for u in dropped:
        print(f"  dropped: {u}")
    for u in failed:
        print(f"  FAILED (live and archived copies unavailable): {u}")


if __name__ == "__main__":
    main()
