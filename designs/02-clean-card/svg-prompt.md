# AI prompt — recreate 02 Clean Card

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "02-clean-card".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- section-header.svg (1000x56): rounded card title with accent bar

**Palette:**
- bg: `#EEF2F7`
- card: `#FFFFFF`
- text: `#1F2937`
- accent: `#3B82F6`
- border: `#E2E8F0`
- bg_dark: `#0F172A`
- card_dark: `#1E293B`
- text_dark: `#E2E8F0`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: bg full-bleed, rounded 16 px card (40,60,920x180) with feDropShadow; name 34 px at 76,138, role below; accent pill 260x44 rx 22 right side. Section header: 1000x56, accent bar 6x28 at x=24, card rect behind title. About card: rounded card 448x188 with avatar ring (stroke accent 3 px). Skills: 8 tiles per row 108x46 rx 10, icon left + label.

**Animation:**
Card rises (translateY 10→0, opacity) 0.7 s ease-out once on load. Nothing else animates.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
