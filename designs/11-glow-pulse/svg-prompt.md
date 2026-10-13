# AI prompt — recreate 11 Glow Pulse

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "11-glow-pulse".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- (no extra files)

**Palette:**
- bg: `#0B0B1A`
- violet: `#A78BFA`
- pink: `#F472B6`
- text: `#E9D5FF`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: bg #0B0B1A; orb at (500,150): radial-gradient core circle r 26 blurred stdDev 12 + three pulsing rings r 34/52/72; name 34 px y=250 with feDropShadow violet glow; tagline violet y=285. Divider: faint violet line + blurred pink dot crossing every 3 s. About card: #131328 rounded 14, violet border whose stroke-opacity pulses 5 s plus blurred halo copy. Skills: icons wrapped in groups scaling 1→1.06 staggered.

**Animation:**
Three concentric circles animate r (+10) and opacity over 3 s, staggered 0.5 s, ease-in-out keySplines 0.42 0 0.58 1. Name glow pulses opacity 0.85→1→0.85 over 4 s. Divider pulse dot travels left→right 3 s. Skill icons scale 1→1.06→1 staggered 0.15 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
