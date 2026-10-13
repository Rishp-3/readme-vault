# SVG guide — using `svg-prompt.md` with an AI

Each design folder contains `svg-prompt.md`: a complete, self-contained brief that regenerates that design's SVGs without seeing this repo. Paste it into any capable model and ask for one file at a time (banner first, then card, skills, divider).

## What GitHub allows (and what kills your SVG)
- ✅ Self-contained SVG files committed to the repo, referenced with `<img src="...">` (works in READMEs; SVGs from URLs are blocked by camo).
- ✅ SMIL animations (`animate`, `animateTransform`, `animateMotion`, `set`) and CSS `@keyframes` inside a `<style>` element in the SVG.
- ✅ Filters: `feGaussianBlur`, `feDropShadow`, patterns, gradients, clipPaths, masks.
- ❌ `<script>` — stripped/inert. Never rely on JS.
- ❌ `foreignObject` — GitHub sanitizes it away.
- ❌ Web fonts (`@import`, external `.woff2`) — only system stacks render: `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`.
- ❌ External images/hrefs inside the SVG (`<image href="http…">`) — blocked.
- ⚠️ Keep files small (< 150 KB hard ceiling, aim < 60 KB) and always validate with `xmllint --noout`.

## Checklist after AI generation
1. `xmllint --noout file.svg` passes.
2. `viewBox` + `width`/`height` present; `<title>`/`<desc>` added.
3. No banned constructs above (`grep -E 'script|foreignObject|href="http'`).
4. `prefers-reduced-motion` block exists.
5. Open it in a browser, then in the README preview — animations behave the same.
