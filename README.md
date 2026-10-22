Visit **[picsl-upenn.github.io/picsl-website](https://picsl-upenn.github.io/picsl-website)** 🚀

# PICSL website

Static website for the Penn Image Computing and Science Laboratory, replacing the old
WordPress site at https://picsl.upenn.edu. Built with Jekyll on the
[Lab Website Template](https://github.com/greenelab/lab-website-template)
([documentation](https://greene-lab.gitbook.io/lab-website-template-docs)).

The easiest way to update the site is to ask [Claude Code](https://claude.com/claude-code)
to do it, then open a pull request. The tutorial below walks through that.

## Updating the website with Claude Code

### One-time setup

1. Install [Claude Code](https://docs.claude.com/en/docs/claude-code/overview), and make
   sure you have `git`, the GitHub CLI (`gh`, logged in with `gh auth login`) and Ruby with
   Bundler. On a Mac, `brew install git gh ruby` covers all of these.
2. Ask a lab admin to give you write access to the
   [picsl-upenn/picsl-website](https://github.com/picsl-upenn/picsl-website) repository.
3. Clone the repository and start Claude Code in it:

   ```sh
   git clone https://github.com/picsl-upenn/picsl-website.git
   cd picsl-website
   claude
   ```

4. Ask Claude to get the site running locally:

   > Install what's needed and show me how to preview the site locally.

   Claude runs `bundle install`, then starts `bundle exec jekyll serve`. Open
   http://localhost:4000 to see the site. It rebuilds when files change, so you can leave
   it running while you work.

### Making a change

Each change follows the same loop: start a branch, describe what you want in plain
language, check the result, refine, and open a pull request.

**1. Start from a fresh branch.**

> Pull the latest main and create a branch called update-my-profile.

**2. Describe the change.** Be specific and point Claude to sources. Claude can read web
pages, download images, look up papers in PubMed and ORCID, and edit the site files.
Some requests that have worked well:

- *Team:*
  > Add Jane Doe as a PhD student, using her profile at https://example.edu/jane.
  > Use her photo, cropped so the circle is centered on her face.

  > Move John Smith to alumni.

  > Update my photo and positions from my Penn faculty page: https://www.med.upenn.edu/apps/faculty/index.php/...

- *Research highlights:*
  > Write a post for the Research page about our new paper, doi:10.xxxx/yyyy.
  > Use a figure from the paper if its license allows it.

  > Find my most impressive last-author papers from 2025 and write a featured post for each.

- *Fixes:*
  > The thumbnails on the Software page are cropped strangely. Can you fix that?

  > Check all the links on my member page and fix any that are broken.

- *New pages:*
  > Add a Jobs page to the menu with a posting for a postdoc position. Here is the ad: ...

You can paste screenshots into Claude Code to show what looks wrong.

**3. Check the result.** Look at the page at http://localhost:4000, or ask Claude to take
screenshots and review them. Tell Claude what to change ("the photo is too zoomed in",
"move this section to the bottom", "that's not my Google Scholar ID") and repeat until
you're happy.

Check facts yourself, especially names, roles, IDs and anything summarizing a paper.
Claude writes research posts from the abstract and should say when it's unsure, but you
know the work best.

**4. Open a pull request.** When you're done:

> Commit these changes and open a pull request.

Claude commits to your branch, pushes it to GitHub, and opens a pull request (PR)
describing the change. Then:

- Within a few minutes, a bot comments on the PR with a **preview link** showing the
  whole site with your changes. Check it, especially on a phone.
- A lab admin reviews the PR. If they ask for changes, describe them to Claude on the
  same branch and push again; the preview updates automatically.
- Once the PR is merged, the live site updates automatically within a few minutes.

Please don't push directly to `main`. Pull requests give everyone a chance to catch
mistakes and keep a record of what changed and why.

### Tips

- **Images:** photos should be square and centered on the face, since the site shows them
  in a circle. Ask Claude to remove photo metadata (EXIF), which can include GPS location.
- **Figures from papers:** only reuse figures whose license allows it (for example
  CC BY), and credit them. Ask Claude to check the license. When reuse isn't allowed,
  Claude can draw a simple diagram instead, or you can supply one of your own figures.
- **Publications:** the Publications page is generated automatically from the ORCID
  records in `_data/orcid.yaml`. To fix or add papers, update your ORCID record; the site
  picks up changes on the next build.
- **Big changes:** for something large, such as a redesign or many new pages, ask Claude
  to propose a plan first.

## Where things live

| What | Where |
|---|---|
| Team members | `_members/<name>.md` (`role`: `principal-investigator`, `faculty`, `research-associate`, `staff`, `postdoc`, `phd`, `alumni`; add `group: alum` for alumni) |
| Photos of team members | `images/members/` |
| Research and software cards | `_data/projects.yaml` (tag `research` or `software`) |
| Research posts | `research/<slug>.md`, with images in `images/research/` |
| Software pages | `software/<slug>.md` |
| Publications | faculty ORCID IDs in `_data/orcid.yaml`, or individual DOIs in `_data/sources.yaml`. The `update-citations` workflow generates `_data/citations.yaml`; don't edit that file. |
| Navigation menu | the `nav:` block at the top of each top-level page (`about/`, `research/`, `team/`, etc.) |
| Site title, links, footer | `_config.yaml` |
| Colors and fonts | `_styles/-theme.scss` |

Pages migrated from the old site keep their old URLs through `redirect_from` front
matter, so old links and bookmarks still work.

## Running locally without Claude Code

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Deployment

Merges to `main` are built and deployed to GitHub Pages by the workflows in
`.github/workflows/`. Pull requests get a preview build automatically.

To serve the site at picsl.upenn.edu (not done yet):

1. Add a `CNAME` file containing `picsl.upenn.edu`, and set the custom domain in the
   repository's Pages settings.
2. Ask Penn IT to point `picsl.upenn.edu` at GitHub Pages with a `CNAME` record to
   `picsl-upenn.github.io`.
3. When DNS has propagated, turn on "Enforce HTTPS" in the Pages settings.

## Migration from WordPress

`tools/migrate_wp.py` did the one-time import from the WordPress site. It scraped the
pages listed in the WordPress sitemaps, using Wayback Machine copies for pages that
failed on the live site, and downloaded media into `images/wp/`. It is kept for
reference. Don't re-run it: it would overwrite pages that have been edited since.
