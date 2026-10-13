---
name: Bug report
about: Something renders wrong or breaks
title: "[bug] "
labels: bug
---

**Design**
e.g. `07-cyberpunk`

**What happens vs what should happen**

**Where**
Browser + OS, GitHub theme (dark/light), README snippet or screenshot.

**SVG checks**
- [ ] `xmllint --noout file.svg` passes
- [ ] File < 150 KB
- [ ] No `<script>` / `foreignObject` / external hrefs
