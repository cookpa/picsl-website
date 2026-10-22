# PICSL website

Static website for the Penn Image Computing and Science Laboratory, replacing the old
WordPress site at https://picsl.upenn.edu. Built with Jekyll on the
[Lab Website Template](https://github.com/greenelab/lab-website-template)
([documentation](https://greene-lab.gitbook.io/lab-website-template-docs)).

## Editing content

| What | Where |
|---|---|
| Team members | `_members/<name>.md` (`role`: `principal-investigator`, `faculty`, `staff`, `postdoc`, `phd`; add `group: alum` for alumni) |
| Research projects and software cards | `_data/projects.yaml` (tag `research` or `software`) |
| Research project pages | `research/<slug>.md` |
| Software pages | `software/<slug>.md` |
| Publications | add faculty ORCID IDs to `_data/orcid.yaml`, or individual DOIs to `_data/sources.yaml`. The `update-citations` GitHub workflow generates `_data/citations.yaml`. |
| Site title, links, footer | `_config.yaml` |
| Colors and fonts | `_styles/-theme.scss` |

Migrated pages keep their old URLs through `redirect_from` front matter, so old links
and bookmarks still work.

## Running locally

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Deployment

Pushes to `main` are built and deployed to GitHub Pages by the workflows in
`.github/workflows/`. To serve the site at picsl.upenn.edu:

1. In the repository settings, under Pages, set the source to the `gh-pages` branch
   (created by the first build) and the custom domain to `picsl.upenn.edu`. The `CNAME`
   file in this repository holds the domain.
2. Ask Penn IT to point `picsl.upenn.edu` at GitHub Pages with a `CNAME` record to
   `<org>.github.io`.
3. When DNS has propagated, turn on "Enforce HTTPS" in the Pages settings.

## Migration from WordPress

`tools/migrate_wp.py` did the one-time import from the WordPress site. It scraped the
pages listed in the WordPress sitemaps, using Wayback Machine copies for pages that
failed on the live site, and downloaded media into `images/wp/`. It is kept for
reference. Re-running it overwrites the migrated files.
