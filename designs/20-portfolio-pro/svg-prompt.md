# AI prompt — recreate 20 Portfolio Pro

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "20-portfolio-pro".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- navy: `#0F172A`
- blue: `#2563EB`
- slate: `#475569`
- border: `#E2E8F0`
- bg: `#FFFFFF`
- text: `#111827`
- bg_dark: `#0B1220`
- text_dark: `#E2E8F0`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: white (dark: #0B1220) with 8 px navy/blue left accent stripe; name 40 px semibold x=60 y=120; role 19 px blue y=158; value statement 15 px slate y=190; three fact chips (navy fill, white text, rx 17) y=210. Divider: thin slate line x 60→940. About card: subtle gray inner card, navy initials circle avatar, name/role/value/contact. Skills: three labeled columns FRONTEND / BACKEND / TOOLS with square bullets.

**Animation:**
Single 1 s fade-in (opacity 0→1) applied to name, role, value line and chips. No looping animation.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
