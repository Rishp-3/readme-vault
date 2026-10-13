# Changelog

All notable changes to this project are documented here, format based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), versioning per
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-10-13

### Added
- 20 GitHub profile README designs (`01-minimal` … `20-portfolio-pro`), each with:
  - copy-paste template README + self-contained animated SVG assets
  - a demo README personalised with public data of GitHub user `Rishp-3`
  - `setup.md`, `svg-prompt.md`, `colors.md`, `preview.png`, `variants/`
- Deterministic generator `tools/build.py`, live data fetcher `tools/fetch-data.py`
  (with manual fallback snapshot), CLI filler `tools/replace-placeholders.py`,
  validator `tools/check.py`.
- Shared icon set (original 48×48 glyphs, mono + colored), 6 generic dividers,
  `badges.md`, `placeholders.md`.
- Docs: `CUSTOMIZATION.md`, `SVG-GUIDE.md`, 4×5 `gallery.png`.
- CI: weekly + per-push link check (lychee), design validation workflow.
- Issue templates, PR template, MIT license, code of conduct.
