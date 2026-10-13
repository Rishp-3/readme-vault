# AI prompt — recreate 08 Gradient Wave

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "08-gradient-wave".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- wave-footer.svg (1000x60): mirrored waves for the bottom of the page

**Palette:**
- bg: `#0F172A`
- g1: `#06B6D4`
- g2: `#8B5CF6`
- text: `#E2E8F0`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: bg #0F172A; three filled sine bands (amp 14/18/10, wavelengths 250/330/200, baselines 235/250/265) closing to y=300, gradient fills at 50/55/85 % opacity; name 44 px centered y=120, tagline y=158, role mono y=190. Divider: 500-wide mini wave translated seamlessly. About card: #111c33 rounded 14 with 5 px gradient top bar. Skills: gradient-outline pills auto-width. Footer: 1000x60 mirrored bands.

**Animation:**
Three sine-wave bands drawn twice as wide as the canvas, animateTransform translate 0→−1000 seamless loops at 8 s, 12 s, 18 s. Divider mini-wave 6 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
