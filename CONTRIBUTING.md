# Contributing

Thanks for interest in improving **github-profile-designs**!

## Adding or fixing a design
1. Everything is generated from `tools/build.py` + `tools/design_defs.py` + the SVG builders. **Do not hand-edit generated files** — edit the generator and re-run `python3 tools/build.py`.
2. Add your design config to `DESIGNS` and a builder function; keep the naming scheme `NN-slug`.
3. Run the quality gates: `python3 tools/check.py`, `xmllint --noout` on every new SVG.
4. Preview PNGs are regenerated automatically (cairosvg renders the first frame of SMIL animations — that is expected).

## Conventions
- SVGs must stay self-contained (see `docs/SVG-GUIDE.md`): no scripts, no external refs, system fonts only, reduced-motion respected.
- Templates use only placeholders from `shared/placeholders.md`; personal data appears only in `demo/` folders.
- Text contrast ≥ 4.5:1 on backgrounds.

Open an issue first for big changes. PRs should describe *what* changed and show a screenshot.
