# AI prompt — recreate 06 Matrix Rain

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "06-matrix-rain".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#000000`
- head: `#E8FFE8`
- bright: `#00FF41`
- mid: `#008F23`
- dim: `#003B10`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: pure black, 40 rain columns at 25 px pitch built from 8 reusable column defs (`<use>`), 14 glyphs each 18 px mono; center dark rounded rect 500x130 at (250,90) opacity .92 holding name 34 px + tagline 15 px. Divider: single glyph row. About card: black card, green 1 px border, mono lines `> identify --user`, name, role, [status], user_. Skills: green icons 72 px pitch.

**Animation:**
40 glyph columns, each a `<use>` of one of 8 predefined columns, animateTransform translate y −330→330, durations 4–9 s random, negative random begin delays, indefinite.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
