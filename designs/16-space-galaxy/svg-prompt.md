# AI prompt — recreate 16 Space Galaxy

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "16-space-galaxy".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#05051A`
- indigo: `#6366F1`
- violet: `#C084FC`
- pink: `#F0ABFC`
- star: `#FFFFFF`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: deep space #05051A; 80 stars (r 1/1.5/2.5) twinkling; spiral galaxy left-of-center: bright radial core + four rotated ellipse arms, whole group rotating 120 s; ringed planet right (indigo disc + tilted pink ring); shooting star crossing every 9 s; name 40 px weight 300 letter-spacing 4 centered y=150. Divider: faint line + 20 tiny stars. About card: #0A0A24 rounded card, star-dust dots along top/bottom edges. Skills: 12 icons on two concentric orbit rings counter-rotating 60/80 s.

**Animation:**
80 stars twinkle opacity 0.3→1→0.3 over 2–5 s random. Galaxy group rotates 0→360 over 120 s. Shooting star uses animateMotion across the banner every 9 s with fading opacity. Skills icons sit on two orbit rings rotating ±360 over 60/80 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
