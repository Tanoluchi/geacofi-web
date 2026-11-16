# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Astro, static output. JavaScript only where it is needed (the coffee pack, the mobile menu). Hosting is undecided; the candidates on record are Netlify, Vercel and Cloudflare Pages.

## Users

- **Primary:** a local in Corrientes, usually a regular, on a phone. They want to know whether Geacofi is open right now, what is on the carta, which coffees are on the bar, and how to get there or message the café on WhatsApp.
- **Secondary:** people coming for the events (vinyl sets, cuppings, pop-ups) who want to know what is next and when.

## Product Purpose

The website for Geacofi, a specialty coffee shop at 9 de Julio 996, Corrientes Capital (@geacofi). It answers the practical questions (open or closed, carta, coffees, events, location) in the café's own voice, so a customer recognizes the café immediately and feels they are walking into its world. Success means someone checks the carta or the hours and then walks in or messages on WhatsApp.

## Positioning

Coffee from fixed guest roasters (Komún, MOMO, La Motofeca and Lo de Pepe) with rotating coffees, plus a vinyl culture of record sets, cuppings and pop-ups. The rana from the original logo is the café's host. Tagline: "café, discos y eso…". It knows a lot about coffee and does not take itself too seriously.

## Operating Context

- Four pages: Home, Carta, Eventos, Visitanos. No online ordering or reservations; contact and event bookings go through WhatsApp.
- Opening hours: Monday to Saturday, 07:00–13:00 and 17:00–21:00 (days confirmed by the user on 2026-11-16). The home shows an open/closed indicator computed from these hours in Argentina time (UTC−3).
- Anything that changes often (carta and prices, coffees on the bar, events, hours) lives in data files, never in the design. The model is four sources: `carta`, `cafes`, `eventos`, `local`. See `docs/geacofi-proyecto/05_sistema_de_diseno/2-datos.md`.
- Coffee pack rules: 5 stickers, at most 2 from the same roaster, only coffees that are on the bar. A roaster with no coffees loaded shows "café de la semana · preguntá en la barra".
- Events sort themselves: future dates are "próximos", past ones "ya pasaron". With no upcoming events the page shows the empty state.

## Capabilities and Constraints

- **Open decision:** who maintains the data and how (the owner in Google Sheets published as CSV with automatic rebuilds, or JSON in the repo). Keep the data model the same either way.
- **Open decision:** hosting provider and domain.
- **Pending from the owner:** the coffees currently on the bar (including Lo de Pepe's), upcoming events, high-resolution photos, and the story behind the name "gea".
- Prices are whole pesos, displayed as `$ 5.500`.
- Carta categories as the café names them: calientes (Lado A), fríos (Lado B), filtrados (Edición especial), salado (Lado C), panadería y pastelería (Bonus track).
- Performance target: under 1 MB per page, LCP under 2.5 s on 4G. Google Maps loads only on demand.
- Local SEO: schema.org `CafeOrCoffeeShop` structured data and the café's Google Business profile.

## Brand Commitments

- The "geacofi" lettering is the logo and is always used as an image, never set in a font. Vector files are in `docs/geacofi-proyecto/logos/`.
- The rana is always drawn from the stroke of the original vectorized logo (face, eyes and hand). Never redesign it. Favorite poses: the official pose, making a pour-over, and grinding. Never more than two ranas on one screen. The rules are in `docs/geacofi-proyecto/05_sistema_de_diseno/1-rana.md` and `03_biblia_rana/`.
- Voice: Rioplatense voseo ("pasá", "escribinos", "preguntá en la barra"), lowercase titles, buttons and carta names, short sentences, the diminutives and jokes of the printed carta ("shot chiquito", "huevito revuelto"). A button says exactly what happens: "escribinos por WhatsApp", not "contacto".
- Personality traits: pachorra (relaxed pace), knows but doesn't show off, handmade, bar-counter humor, vinyl culture, neighborhood café with standards.
- Motion is always optional and stops completely under `prefers-reduced-motion: reduce`.

## Evidence on Hand

- Original brief: `docs/geacofi-proyecto/00_referencias/brief-original.txt`.
- Instagram captures (low resolution), the original logo with the rana, and the roasters' logos: `docs/geacofi-proyecto/00_referencias/`.
- Completed stages: brand diagnosis (`01_diagnostico/`), three art directions with direction **C · Café y eso** chosen (`02_direcciones_de_arte/`), the rana bible with 26 SVG/PNG illustrations and their generator code (`03_biblia_rana/`), screens and the coffee-pack prototype (`04_pantallas/`), the design system with tokens and components (`05_sistema_de_diseno/`), and the HTML sources of every sheet (`06_html_fuente/`).
- Real carta items and prices from the printed carta, as recorded in `2-datos.md`. Refresh them before launch.
- **Absent, and must not be fabricated:** current coffees, upcoming events, high-resolution photos, the name's story, testimonials, and press. Missing values are written as `[a confirmar]` until confirmed.

## Product Principles

1. **Never invent.** Prices, hours, coffees and events come only from the café's data. Gaps show as `[a confirmar]`.
2. **The practical answer comes first, in the café's voice.** Open or closed, the carta, how to get there and WhatsApp are always within reach on a phone.
3. **Data, not design, changes week to week.** Rotating coffees and events must update without touching the layout.
4. **The identity already exists.** The rana and the lettering are preserved, never replaced; new work extends the approved bible.
5. **Nothing urgent.** No pushy sales or "buy now" pressure; the site invites people in.

## Accessibility & Inclusion

Mobile-first. Contrast and keyboard navigation are checked before launch, and every animation respects reduced-motion preferences.
