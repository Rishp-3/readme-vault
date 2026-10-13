# AI prompt — recreate 07 Cyberpunk

Copy everything below into an AI that outputs SVG code.

---

Create SVG files for a GitHub profile README, design "07-cyberpunk".

**Constraints:** fully self-contained; no `<script>`, no `foreignObject`, no external fonts/images/href URLs (only xmlns); `viewBox` set plus explicit `width`/`height`; one `<title>` and one `<desc>` per file; system font stacks only (`ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` and `-apple-system, "Segoe UI", Helvetica, Arial, sans-serif`); each file under 150 KB; animation via SMIL (`animate`, `animateTransform`, `animateMotion`, `set`) or CSS `@keyframes` inside `<style>` in the SVG only; include `@media (prefers-reduced-motion: reduce){*{animation:none !important;}}`; valid XML.

**Files:**
- banner.svg (1000x300)
- divider.svg (1000x24)
- about-card.svg (480x220)
- skills.svg (1000x120)
- hud-frame.svg (480x220): cut-corner bracket frame overlay

**Palette:**
- bg1: `#140A28`
- bg2: `#0A0A1F`
- pink: `#FF2BD6`
- cyan: `#00E5FF`
- yellow: `#F7E03C`
- panel: `#2A1450`

**Typography:** headings in the sans stack, small labels/terminal text in the mono stack; banner name 40–46 px bold, tagline 15–18 px, card name 19–22 px.

**Layout:**
Banner: vertical gradient #140A28→#0A0A1F; perspective floor: 13 converging lines + 4 horizontals near bottom (y 240–300); main cut-corner octagon panel inset 30 px; HUD labels in corners; name 46 px triple-stack centered y=150; role 16 px cyan letterspaced; tagline 13 px pink. Divider: pink neon line + glowing traveling dot. About card: cut-corner card, `// STATUS: ONLINE`, name, role, @user, `// open to …`. Skills: neon icons with duplicated blurred copy for glow.

**Animation:**
Three stacked name layers (pink/cyan/white); pink+cyan offset ±3 px constantly; glitch burst every 4 s for ~120 ms via animateTransform translate keyTimes 0.92–1. Divider dot travels 0→1000 in 2.6 s.

**Text content:** placeholders `YOUR_NAME`, `YOUR_ROLE`, `YOUR_TAGLINE`, `YOUR_STATUS`. Banner shows only name/tagline/role (no design name). No email addresses in SVG.

**Output:** only the SVG code per file, each in its own fenced block labelled with the file name.
