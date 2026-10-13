# AI prompt — recreate 19 Glassmorphism

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "19-glassmorphism".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg1: `#312E81`
- bg2: `#0EA5E9`
- blob1: `#F0ABFC`
- blob2: `#38BDF8`
- glass: `#FFFFFF`
- border: `#FFFFFF`
- text: `#FFFFFF`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: diagonal indigo→sky gradient; three big blurred blobs (stdDev 30, pink + sky-blue) drifting behind; central frosted panel 700x160 rx 20: white 18 % fill + 1 px white 40 % stroke + inner top highlight gradient; name 40 px white on panel y=140, tagline y=176, role mono y=206. Divider: 400x20 glass pill. About card: gradient card with two blobs peeking under a smaller glass panel. Skills: 72x80 glass tiles in a row. Note: real backdrop blur is impossible in SVG — this imitates it.

**Animation:**
Two/three large blurred blobs drift slowly (10–14 s) behind static glass panels. Nothing else animates — the illusion must read even frozen.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
