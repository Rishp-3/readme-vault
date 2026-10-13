# Customization guide

## Change the colors
Every SVG stores colors inline. Open the file, find-and-replace the hex values from the design's `colors.md`.
Watch the contrast: text must stay ≥ 4.5:1 against the background (each `colors.md` lists the computed ratio).

## Change the text
SVG text lives in `<text>` elements with stable ids documented in each `setup.md`
(e.g. `banner-name`, `card-role`). Keep replacement strings short — measure roughly
`chars × font-size × 0.6` (monospace) and stay inside the box, or lower the `font-size` attribute.

## Change sizes
Scale by editing `width`/`height` (keep `viewBox` untouched and the drawing scales perfectly).
Standard sizes: banner 1000×300, divider 1000×24, section header 1000×56, about card 480×220, skills 1000×120.

## Swap icons
Original 48×48 glyphs are in `shared/icons/` (mono + colored). Each icon is a `<g transform="translate(x,y) scale(k)">…</g>`
block — copy it into any SVG and change its `fill`/`stroke` color. To use official brand logos instead, link shields.io badge images from the README instead of embedding SVGs.

## Dark/light `<picture>` switching
```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img alt="banner" src="assets/banner.svg"/>
</picture>
```
Keep both files identical except palette. Designs 01/02 ship `banner-dark.svg` in `assets/`; 13/14/20 explain their variants in `variants/`.
