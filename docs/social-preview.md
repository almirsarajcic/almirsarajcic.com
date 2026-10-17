# Website social preview

[Project home](../README.md)

The card uses the website's IBM Plex Sans masters, paper/ink/secondary/sienna tokens and accepted consultant + Kogen-builder positioning. It is link-preview metadata only; it is not a page hero or an X profile banner.

## Source and surface map

| Concern | Owner |
| --- | --- |
| Canonical personal positioning | Consulting `career/public-presence-2026-09-28/profile-fields.json` |
| Editable card copy and layout | `scripts/build-social-preview.py` |
| Licensed font masters | `assets/font-sources/IBMPlexSans-{Regular,SemiBold}.woff2` and accompanying OFL |
| Derived vector | `public/brand/social-preview.svg`, outlined to prevent font substitution |
| Active raster export | `public/brand/social-preview-consultant-kogen.png`, 1280 × 640 |
| Open Graph and X card metadata | `src/layouts/Base.astro`, uses a large-image card and explicit image dimensions/alternative text |
| Prior raster | `public/brand/social-preview.png`, retained for previously cached links |
| Publication route | Existing Cloudflare Git integration; [deployment procedure](deployment.md) |

17 October correction: Almir identified the cropped, outdated image in his pinned X post. The prior metadata requested a square summary thumbnail while supplying a wide image. The replacement retains the website's visual identity and uses existing accepted wording. Preparation is not evidence that X has refreshed the saved post.

## Refresh

Inputs: accepted wording, this repository, Python with `fonttools[woff]`, Node dependencies installed by `npm install`. Keep the Python environment outside iCloud. No new card framework is required for this one static identity card; the repository had an SVG/PNG but no maintained export recipe.

1. Edit copy/layout in `scripts/build-social-preview.py`; preserve the font and colour owners above.
2. Run the script with the prepared Python environment. It writes the outlined SVG and matching PNG using the existing Sharp dependency. A safe-margin check rejects overflowing lines.
3. Inspect the exported image at full size and reduced to a mobile card. Confirm name diacritics, both roles, spacing and legibility. The output is opaque; it uses the same artwork across light/dark platform backgrounds.
4. Run `npm run check` and `npm run build`. Check all generated pages for the intended `og:image`, image dimensions, alternative text and `summary_large_image` value. Confirm that the image resolves in the local build and remains absent from visible page content.
5. Follow the existing review/publication boundary. Keep one commit for the complete positioning refresh when an amendment is authorized; preserve the published tip and use an exact lease for any authorized history rewrite.
6. After deployment, compare live image bytes and metadata with the reviewed build, then inspect an actual saved share card where available. A new filename avoids reusing the old image URL; it does not guarantee an existing post refreshes immediately. Keep any downstream cache limitation explicit, and do not delete/repost a published post just to refresh its card.

On missing dependencies or failed generation, preserve the last export and fix the environment before rebuilding. If the site is correct but a platform still displays a cached card, resume from platform verification without regenerating or repeatedly publishing the same asset. Completion distinguishes checked local source, deployed website metadata and the saved platform card.
