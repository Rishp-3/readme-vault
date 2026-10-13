# Dark variant

Use `<picture>` so GitHub picks the SVG by visitor theme:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg"/>
  <img alt="Sunset Gradient banner" src="assets/banner.svg"/>
</picture>
```

`assets/banner-dark.svg` is generated for this design. For 13/14/20 the default palettes already read well on both GitHub themes; the dark file is optional — regenerate it with `python3 tools/build.py --only 14` if you need tweaks.
