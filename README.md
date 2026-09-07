# almirsarajcic.com

Source for Almir Sarajčić’s public portfolio and career website. The approved page is built with Astro as a static site and published at [almirsarajcic.com](https://almirsarajcic.com).

## Start here

| Need | Location |
| --- | --- |
| Edit the public page | [`src/pages/index.astro`](src/pages/index.astro) |
| Replace the downloadable CV | [`public/Almir_Sarajcic_CV.pdf`](public/Almir_Sarajcic_CV.pdf) |
| Preview locally | Run `npm install`, then `npm run dev` |
| Verify a production build | Run `npm run check` and `npm run build` |
| Publish or change domains | [Cloudflare Pages workflow](docs/deployment.md) |

## Current state

The 7 September redesign uses IBM Plex typography, aligned project rows and a compact masthead. Almir accepted publication of the website and full two-page CV. Responsive behavior, dark theme, metadata, Plausible analytics, CV URL, and canonical apex domain are retained. Cloudflare Pages is the selected production host. Pushes to `master` deploy through Cloudflare’s GitHub integration; branch previews are disabled.

## Folder map

- `src/pages/` — authored site pages.
- `public/` — files copied unchanged to the built site, including the CV.
- `docs/` — maintained production and domain workflow.
- `dist/` — generated production output; not committed.

Career copy and the canonical application CV are maintained in the adjacent JobHunt workspace. Update those owners first when facts or positioning change, then synchronize this repository and verify the public result.

## Design proposal

The [7 September design record](docs/design-proposal.md) records the accepted design. The existing JobHunt career-review Sites project retains the private review; production uses Cloudflare Pages.

## Font and performance maintenance

Licensed full font masters are in `assets/font-sources/`. `scripts/subset-fonts.py` derives Latin/Latin Extended webfonts into `src/assets/fonts/`; run it with Python and fontTools only when font sources or required writing systems change. The normal npm build needs no Python. Astro emits hashed font URLs and minified inline CSS; `public/_headers` gives hashed assets immutable caching. Font licenses accompany both source and public output. Keep Bosnian diacritics, punctuation and arrows in any future subset. The minimal A favicon is owned by `public/favicon.svg`; no separate social card is generated.
