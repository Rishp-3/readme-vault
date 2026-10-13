# AI prompt — recreate 03 Monochrome

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "03-monochrome".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- frame.svg (480x220): double white/black frame used around the about card

**Palette:**
- bg: `#000000`
- text: `#FFFFFF`
- dim: `#8A8A8A`
- frame: `#3A3A3A`
- black2: `#111111`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: black bg, inset 1 px white frame at 12 px margin, uppercase name 64 px letter-spacing 6 centered y=150, role 16 px dim y=196, scan line on top. Divider: dashed 4 6. About card: dark inner panel with double frame, initial-circle avatar, uppercase mono text. Skills: grayscale icons 88 px pitch.

**Animation:**
White 2 px scan-line rect (opacity .15) translates x −200→1200 over 6 s, linear, indefinite loop.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
