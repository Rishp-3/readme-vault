# AI prompt — recreate 14 Sunset Gradient

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "14-sunset-gradient".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- o: `#FF9A3C`
- p1: `#FF5E7E`
- p2: `#9B4DCA`
- deep: `#2A1233`
- sun: `#FFD166`
- text: `#FFFFFF`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: vertical gradient orange→coral→purple→deep; half sun (r 70 radial + blurred halo) rising/falling ±14 px 12 s behind hills; three hill silhouettes (paths) in darkening purples at bottom; three simple bird strokes crossing via animateMotion; name white 44 px y=120, tagline y=156. Divider: gradient horizon line + sun dot. About card: gradient bg with translucent white inner card (18 % white, 1 px white border). Skills: white icons on translucent circular pills.

**Animation:**
Sun group translates y +14→−14→+14 over 12 s. Three birds follow animateMotion straight paths 20–28 s with negative begins for staggering.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
