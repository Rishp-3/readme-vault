# AI prompt — recreate 12 Retro Pixel

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "12-retro-pixel".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#2B2D42`
- yellow: `#FFD166`
- red: `#EF476F`
- green: `#06D6A0`
- white: `#EDF2F4`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: flat #2B2D42 night sky; 26 square pixel stars (4 px); stepped pixel mountain silhouettes along the bottom (two grays); original pixel character (head/cap/body/arms rects) at a desk with monitor left third; title rendered from a 5x7 bitmap font in yellow 6 px pixels centered y=60; role subtitle 3 px pixels white. Divider: repeating pixel hearts red/yellow/green. About card: RPG dialog box double-bordered white, `PLAYER 1` yellow bitmap text, HP bar static, XP bar fills once. Skills: 64 px bordered tiles with icons + 2 px bitmap labels.

**Animation:**
Pixel stars blink with discrete opacity step animations (2–4 s, random begin). XP bar fills width 0→372 once over 2.5 s (fill=freeze). shape-rendering crispEdges everywhere.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
