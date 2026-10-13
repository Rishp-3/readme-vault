# AI prompt — recreate 18 Forest Green

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "18-forest-green".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#0F3D22`
- pine: `#166534`
- green: `#22C55E`
- light: `#86EFAC`
- trunk: `#7C5A3A`
- text: `#DCFCE7`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: forest bg #0F3D22; moon top-right with blurred halo; three depth layers of triangle pines (far 8 trees darker/smaller, mid 7, near 5 tallest) each swaying ±1° about trunk base at different speeds; drifting blurred mist band y≈200; nine fireflies (2.5 px warm-yellow) blinking/drifting; name #DCFCE7 42 px y=100. Divider: baseline with 10 tiny tree triangles. About card: wooden-sign — brown outer rounded rect, grain curves, dark green inset with tan border. Skills: leaf-shaped tiles (rounded, one pointed corner) alternating greens.

**Animation:**
Three pine layers sway rotate −1°→+1°→−1° about their trunk base at 5/7/9 s (parallax feel). Nine fireflies drift (small translate) and blink (irregular opacity). Mist band translates x 0→60→0 over 16 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
