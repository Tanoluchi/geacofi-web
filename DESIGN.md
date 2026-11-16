---
name: Geacofi
description: café, discos y eso…
colors:
  terracota: "#9A4A38"
  bordo: "#783E32"
  ambar: "#BF834E"
  verde: "#445012"
  durazno: "#FBE6C8"
  crema: "#F1E5D9"
  carbon: "#14171B"
  carbon-raised: "#22262C"
  ink: "#23251C"
  ink-muted: "#5B4A40"
  ink-muted-noche: "#D8CFC2"
  status-open: "#7BC67E"
  tostador-komun: "#CFC6EA"
  tostador-momo: "#14171B"
  tostador-motofeca: "#E58A43"
  tostador-pepe: "#445012"
typography:
  hero:
    fontFamily: "Gaegu, \"Comic Sans MS\", cursive"
    fontSize: "128px"
    fontWeight: 700
    lineHeight: 0.82
  h2:
    fontFamily: "Gaegu, \"Comic Sans MS\", cursive"
    fontSize: "88px"
    fontWeight: 700
    lineHeight: 0.82
  h3:
    fontFamily: "Gaegu, \"Comic Sans MS\", cursive"
    fontSize: "52px"
    fontWeight: 700
    lineHeight: 0.9
  card-name:
    fontFamily: "Gaegu, \"Comic Sans MS\", cursive"
    fontSize: "30px"
    fontWeight: 700
    lineHeight: 0.9
  button:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", sans-serif"
    fontSize: "24px"
    fontWeight: 800
    lineHeight: 1
  card-title:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", sans-serif"
    fontSize: "34px"
    fontWeight: 800
    lineHeight: 1
  date:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", sans-serif"
    fontSize: "24px"
    fontWeight: 800
    lineHeight: 1
  lead:
    fontFamily: "Nunito, system-ui, sans-serif"
    fontSize: "20px"
    fontWeight: 400
    lineHeight: "30px"
  body:
    fontFamily: "Nunito, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: "26px"
  item:
    fontFamily: "Nunito, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 800
    lineHeight: "22px"
  small:
    fontFamily: "Nunito, system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: "18px"
  price:
    fontFamily: "\"DM Mono\", ui-monospace, monospace"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "22px"
    fontFeature: "\"tnum\" 1"
  eyebrow:
    fontFamily: "\"DM Mono\", ui-monospace, monospace"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: "18px"
    letterSpacing: "0.1em"
rounded:
  sm: "10px"
  md: "16px"
  lg: "24px"
  xl: "28px"
  pill: "999px"
spacing:
  space-1: "4px"
  space-2: "8px"
  space-3: "12px"
  space-4: "16px"
  space-5: "24px"
  space-6: "32px"
  space-7: "48px"
  space-8: "80px"
components:
  button-primary:
    backgroundColor: "{colors.terracota}"
    textColor: "{colors.durazno}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 24px"
    height: "48px"
  button-ghost:
    backgroundColor: "{colors.durazno}"
    textColor: "{colors.bordo}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: "10px 24px"
    height: "48px"
  card-carta:
    backgroundColor: "{colors.crema}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: "{spacing.space-5}"
  card-carta-noche:
    backgroundColor: "{colors.carbon-raised}"
    textColor: "{colors.crema}"
    rounded: "{rounded.lg}"
    padding: "{spacing.space-5}"
  ticket:
    backgroundColor: "{colors.crema}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "28px"
  pill-horario:
    backgroundColor: "{colors.carbon}"
    textColor: "{colors.durazno}"
    rounded: "{rounded.sm}"
    padding: "8px 14px"
  chip:
    rounded: "{rounded.pill}"
    padding: "4px 7px"
  empty-state:
    backgroundColor: "{colors.crema}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: "24px"
  figurita:
    rounded: "14px"
    padding: "12px"
    width: "205px"
---

# Design System: Geacofi

## Overview

**Creative North Star: "La barra de barrio"**

Geacofi se diseña como la barra del local: la rana atiende, todo está hecho a mano y lo práctico (si está abierto, qué hay en la carta, cómo llegar, el WhatsApp) siempre queda al alcance del brazo. El sistema viene de la dirección de arte C, "Café y eso": la web como un flyer que se mueve, con stickers pegados, fechas de flyer, cinta de texto y un disco que gira. Sabe mucho de café y no se lo toma tan en serio.

Tiene dos registros. De día, todo vive sobre papel durazno: dibujado, con humor y con aire generoso. De noche, las secciones pasan a carbón y traen la luz baja del local (filtrados, eventos). Alternar los dos al bajar por la página es parte de la experiencia, no un modo oscuro opcional. El ritmo es de pachorra: mucho aire, animaciones lentas y nada que grite "comprá ya".

La identidad ya existe y se respeta. El lettering "geacofi" y la rana salen siempre de los originales vectorizados. Todo lo demás (contornos de marcador, sombras duras, inclinaciones de sticker) existe para que esos dos se sientan en casa.

**Key Characteristics:**
- Dos registros, día en durazno y noche en carbón, alternados por sección.
- Contorno de marcador de 3 px y sombra dura sin desenfoque en todo control y tarjeta.
- Botones inclinados como stickers que se enderezan al pasar el mouse.
- Cuatro familias, cada una con un solo trabajo: manuscrita, condensada itálica, texto y mono.
- La rana como anfitriona, nunca más de dos por pantalla.
- Cultura de vinilo: la carta como lado A y lado B, fechas en estilo flyer, el disco que gira.
- Iconografía dibujada a mano con la misma línea; ninguna librería de íconos.

## Colors

Una paleta cálida de papel, ladrillo y tinta, sacada del Instagram y de la carta impresa del café. Proporción sugerida: durazno 35 · crema 20 · terracota 20 · carbón 15 · bordó 8 · verde 2.

### Primary
- **Terracota de ladrillo**: el acento principal. Botones, títulos manuscritos de día, cinta de texto y pie. Texto durazno encima (5,1:1).

### Secondary
- **Bordó de marcador**: la tinta de los contornos de 3 px y de las sombras duras de stickers y tarjetas. Es el texto del botón secundario.
- **Ámbar de lámpara**: la luz de las fotos. En la interfaz, solo como texto chico, etiquetas y contornos sobre carbón (5,6:1). De noche reemplaza al bordó en los contornos para que se sigan viendo.

### Tertiary
- **Verde de carta impresa**: el color del logo y de la carta en papel. De uso puntual: firma, monocromo de la rana, piezas de marca.

### Neutral
- **Papel durazno**: el fondo de marca, la superficie de día. Es el texto sobre terracota y los títulos de noche.
- **Crema**: tarjetas, ticket, cartel y estados vacíos de día. Es el texto de lectura de noche y la tinta de la rana sobre carbón.
- **Carbón de noche**: superficie de las secciones de noche, tinta de la rana, pastillas de horario y anillo de foco de día.
- **Carbón elevado** (carbon-raised): tarjetas sobre secciones de noche.
- **Tinta de lectura** (ink): texto de párrafo de día (12,7:1 sobre durazno). De noche el texto de lectura es crema (14,7:1).
- **Tinta suave** (ink-muted): descripciones, notas y metadatos de día. De noche pasa a ink-muted-noche.

### Roles por tema

| Rol | Día | Noche |
| --- | --- | --- |
| surface | durazno | carbón |
| surface-raised | crema | carbón elevado |
| ink | tinta de lectura | crema |
| ink-muted | tinta suave | ink-muted-noche |
| heading | terracota | durazno |
| eyebrow | terracota | ámbar |
| border | bordó | ámbar |
| on-accent | durazno | durazno |
| focus | carbón | durazno |

El tema *Noche* se activa con `data-theme="noche"` en cada sección oscura.

### Named Rules
**The Tostador Rule.** Los colores `tostador-*` (lavanda Komún, MOMO en carbón con brillo holográfico, naranja Motofeca, verde Lo de Pepe) existen solo en las figuritas del sobre de cafés y, como puntito chico de identificación, en las pastillas de tostadores. Nunca son relleno en ningún otro lado.

**The Puntito Verde Rule.** `status-open` es solo el puntito de "abierto" en la pastilla de horario. Nunca es texto ni fondo.

**The Ámbar en la Foto Rule.** El ámbar vive en las fotos. En la interfaz es texto chico, etiqueta o contorno sobre carbón, nunca un relleno de día.

## Typography

**Display Font:** Gaegu (con "Comic Sans MS", cursive)
**Flyer Font:** Barlow Condensed itálica (con "Arial Narrow", sans-serif)
**Body Font:** Nunito (con system-ui, sans-serif)
**Label/Mono Font:** DM Mono (con ui-monospace, monospace)

**Character:** una manuscrita gruesa de marcador para lo que se dice en voz alta, una condensada itálica con voz de flyer para lo que se toca, una redondeada amable para leer y una mono para los números de la barra. Cada familia tiene un solo trabajo.

### Hierarchy
- **Hero** (Gaegu 700, 128px, 0.82): un solo título por página. En celular, 72-76px.
- **H2** (Gaegu 700, 88px, 0.82): títulos de sección. En celular, 56-60px. En el ticket, la dirección va a 64px.
- **H3** (Gaegu 700, 52px, 0.9): títulos de eventos. En el estado vacío, 46px.
- **Card name** (Gaegu 700, 30px, 0.9): nombre del café en la figurita, ≈ 15% de su ancho.
- **Button** (Barlow Condensed 800 itálica, 24px, 1): botones sticker. Navegación a 22px.
- **Card title** (Barlow Condensed 800 itálica, 34px, 1): nombre de categoría en la carta.
- **Date** (Barlow Condensed 800 itálica, 24px, 1): fechas de eventos. Marquesina a 30px.
- **Lead** (Nunito 400, 20px/30px): bajada del hero.
- **Body** (Nunito 400, 17px/26px): párrafos, 65 caracteres por línea como máximo.
- **Item** (Nunito 800, 17px/22px): nombre de ítem de la carta, siempre en minúscula.
- **Small** (Nunito 400, 13px/18px): descripción de ítem y notas al pie.
- **Price** (DM Mono 400, 16px/22px, cifras tabulares): precios, con el formato `$ 5.500`.
- **Eyebrow** (DM Mono 500, 13px/18px, 0.1em, MAYÚSCULA): etiquetas sobre títulos y en horarios.

### Named Rules
**The Minúscula Rule.** Títulos, botones y nombres de la carta van en minúscula ("ver la carta", "spicy orange"). Las mayúsculas existen solo en las etiquetas en mono.

**The Lettering No Es Fuente Rule.** El logo "geacofi" es el lettering original y va siempre como imagen (carbón sobre durazno o crema, crema sobre terracota o carbón, bordó en piezas de eventos). Espacio libre de la altura de la "g" y 90px de ancho como mínimo. Nunca se compone con Gaegu ni con otra fuente.

**The Gaegu Grande Rule.** Gaegu solo va en tamaños grandes (30px para arriba) y en color `heading`. Lo que se lee va en Nunito.

## Layout

El espacio sigue una escala de 4 a 80px (space-1 a space-8). Cada sección es una banda de ancho completo con su tema: 80px de padding vertical en escritorio y 50px en celular. El margen lateral es de 24px en escritorio y de 18px en la práctica en celular (16px como mínimo). Los bloques de una sección se separan 32px y las columnas grandes, 48px. Las tarjetas llevan 24px de padding.

El ritmo es generoso: aire de sobra y una idea por bloque. El diseño es mobile first, porque el visitante principal mira desde el celular. Las figuritas del sobre de cafés miden 205px en escritorio y entre 110 y 150px en celular, con 12px de separación. Las áreas táctiles son de 44px como mínimo y los botones, de 48px.

## Elevation & Depth

La profundidad es de papel pegado, no de luz. No hay sombras difusas: toda elevación es una sombra dura sin desenfoque, desplazada abajo a la derecha en el color del contorno, como un sticker con su borde impreso. De noche la sombra de las tarjetas pasa a terracota. La única sombra translúcida es `drop`, para figuritas y flyers sueltos que parecen apoyados sobre la mesa.

### Shadow Vocabulary
- **Sticker chico** (`box-shadow: 4px 4px 0 #783E32`): botón de menú, WhatsApp flotante y chips grandes.
- **Sticker** (`box-shadow: 5px 5px 0 #783E32`): botón sticker en reposo.
- **Sticker despegado** (`box-shadow: 8px 8px 0 #783E32`): botón al pasar el mouse.
- **Tarjeta** (`box-shadow: 8px 8px 0 #783E32`): tarjetas de la carta. El ticket lleva 10px.
- **Tarjeta de noche** (`box-shadow: 8px 8px 0 #9A4A38`): tarjetas sobre carbón.
- **Apoyado** (`box-shadow: 6px 8px 0 rgba(20,23,27,0.28)`): figuritas y flyers sueltos.

### Named Rules
**The Sin Desenfoque Rule.** El blur de toda sombra es 0. Una sombra difusa o un brillo suave rompe el papel.

**The Se Despega Rule.** La sombra crece cuando el sticker se levanta (hover) y desaparece cuando se pega (presionado). La elevación cuenta el estado.

## Shapes

Las formas son redondeadas y gordas, con trazo de marcador. Todo control o tarjeta lleva contorno de 3px (`border-ink`) en el color `border`: bordó de día, ámbar de noche. Los radios son generosos: 10px en pastillas de horario y fotos dentro de tarjetas, 16px en botones, 24px en tarjetas, 14px en figuritas, 28px en el ticket y el contenedor del hero, y pill en chips, pestañas y etiquetas. Los separadores entre ítems de la carta son punteados de 2px (`border-dash`).

En la dirección C, las fotos van recortadas en círculo con contorno bordó o como flyers inclinados. Los recursos recurrentes son el disco de vinilo (surcos con `repeating-radial-gradient` en carbón), la cinta de texto terracota levemente inclinada, los destellos de cuatro puntas, los papelitos y los granos de café. La portada del sistema (Cover, 960×300px) es una composición fija con esos recursos: losa terracota, tarjeta crema, tira bordó, círculo verde y un disco carbón con surcos durazno de 2px (opacidad 0,18) cada 16px.

### Named Rules
**The Sticker Torcido Rule.** Los botones se inclinan entre −2° y 2°: el principal a −1,5° y el secundario al otro lado, a +1,5°.

## Components

Stickers pegados a mano: inclinados en reposo, se enderezan y se despegan al pasar el mouse, y se pegan al tocarlos.

### Buttons
- **Shape:** rectángulo redondeado (16px) con contorno bordó de 3px, inclinado −1,5°.
- **Primary:** fondo terracota, texto durazno en Barlow Condensed 800 itálica de 24px, padding de 10px por 24px, 48px de alto como mínimo y sombra sticker. Una acción principal por bloque.
- **Hover / Focus:** al pasar el mouse se endereza (`rotate(0) translate(-2px,-2px)`) con sombra sticker despegado, en 150ms ease-out. Presionado se pega (`translate(5px,5px)`, sin sombra). El foco es un anillo de 3px en `focus` con 4px de separación.
- **Ghost / Secondary:** fondo durazno, texto bordó, inclinado al otro lado (+1,5°).
- **Copy:** minúscula, verbo y objeto ("ver la carta", "escribinos por WhatsApp"). El de WhatsApp lleva el ícono de línea a la izquierda. Es un `<a>` si navega y un `<button>` si hace algo en la página.

### Chips
- **Notas del café (figurita):** pastilla (999px) sin contorno, Nunito 800 de 10px/1, padding de 4px por 7px, 4px de separación, hasta 3. Fondo en la tinta de la figurita (carbón o crema) y texto en el color del tostador.
- **Pestañas de categoría y etiquetas sueltas:** pastilla (999px) con contorno, en Barlow Condensed o DM Mono según el contexto. No hay una vista previa que fije sus medidas.

### Cards / Containers (Tarjeta de carta, tracklist)
- **Corner Style:** 24px.
- **Background:** `surface-raised` (crema de día, carbón elevado de noche).
- **Shadow Strategy:** tarjeta (bordó). De noche, tarjeta de noche (terracota).
- **Border:** 3px en `border`.
- **Internal Padding:** 24px.
- **Contenido:** una categoría presentada como el reverso de un disco. El ancho máximo es 420px. El encabezado lleva un disco liso de 50px (carbón con letra durazno de día, terracota de noche) con la letra del lado (A, B, C o + para el bonus track) en Barlow Condensed 800 itálica de 24px, la etiqueta en mono de 11px (0.1em, mayúscula, `ink-muted`) y el nombre en card title con `heading`. Cada fila es una grilla de 28px, 1fr y auto con 10px de separación y 10px de padding vertical. Lleva el número de pista en mono de 13px (terracota de día, ámbar de noche), el nombre en item, la descripción en small con `ink-muted` y el precio en price sin cortes de línea. Los separadores son punteados y el último ítem no lleva.

### Navigation
- Barlow Condensed 800 itálica de 22px, en minúscula, con el logo a la izquierda (54px de alto). Cada link es de bordó con padding de 10px por 12px, 6px de separación y subrayado de 4px: terracota en la página actual y transparente en el resto. El botón de WhatsApp va al final con 10px de margen, a 20px, sin inclinación y con sombra sticker. En celular, botón de menú con sombra sticker chico. El WhatsApp flotante lleva sticker chico.

### Pastilla de horario
- Fondo carbón, texto durazno en DM Mono de 14px, radio de 10px y padding de 8px por 14px. Muestra "abierto" o "cerrado" con el puntito `status-open`, calculado desde los horarios en hora de Argentina. Fuera de horario dice "volvemos a las 17", no "Cerrado".

### Ticket de visita (signature)
- Fondo crema, contorno de 3px, radio de 28px y sombra dura de 10px, con un ancho máximo de 820px que se parte en dos bloques al achicarse. A la izquierda (28px de padding, 12px entre elementos): la etiqueta "pasá cuando quieras", la dirección en Gaegu de 64px, la ciudad en Barlow Condensed de 24px, los horarios en pastillas y dos botones (escribinos como principal, cómo llegar como secundario). A la derecha: el mapa, de 240px de alto como mínimo, separado por una línea punteada de 3px como un talón (con rayas diagonales durazno y crema de 14px detrás, mientras no carga) y cargado recién al llegar a la sección. La rana saludando puede asomarse arriba a la derecha.

### Figurita de café (signature)
- Una carta del sobre de cafés. Contorno bordó de 3px, radio de 14px (≈ 7% del ancho), padding de 12px y alto de 1,42 veces el ancho; la vista previa mide 200×284px. Fondo con el color de su tostador y tinta carbón o crema según el contraste. Arriba, el tostador en Barlow Condensed 800 itálica de 17px y el número en mono de 11px. Al centro, la rana en una pose de café sobre un panel translúcido de radio 10px y 6% de padding. Abajo, el café en card name de 30px, el origen y el proceso en mono de 11px y hasta 3 notas como chips. En el sobre el ancho manda (`--cw`): el título es 8,5% del ancho, el número 5,5%, el nombre 15% y las notas 5%. Sombra apoyado. El reverso es `#E7C79C` con un borde punteado bordó de 2px y una interrogación terracota en Gaegu. Al pasar el mouse se inclina hasta 22° en 3D con un brillo que sigue al cursor; MOMO lleva brillo holográfico. Al tocarla abre el detalle. Debajo del sobre va siempre la lista completa de cafés en HTML.

### Estado vacío
- Fondo crema, contorno de 3px, radio de 28px, sombra tarjeta y 24px de padding, con un ancho máximo de 720px. La rana (180px de ancho) y el texto van lado a lado con 22px de separación. La rana acorde (siesta para eventos y fuera de horario, asomándose para listas vacías), un título en Gaegu de 46px con `heading`, una línea de 16px que dice qué hacer y un solo botón de salida.
- **Carga:** la rana moliendo con "moliendo…" en Gaegu y la manija animada (1,2s por vuelta, linear).
- **Confirmación:** tira carbón de 360px como máximo, radio de 16px y padding de 10px por 14px, con la rana de 60px guiñando, la etiqueta "confirmación" en mono de 12px y ámbar y "¡listo! te respondemos pronto" en negrita crema, con `role="status"`.

### Cinta de texto
- Una tira terracota de lado a lado, inclinada −1,2°, con 3px de borde bordó arriba y abajo, 12px de padding vertical, margen lateral de −20px y `overflow: hidden`. Adentro, una fila de ancho `max-content` con 34px de separación en Barlow Condensed 800 itálica de 30px, durazno, sin cortes de línea. Alterna palabras de la barra (espresso, filtrados, chipa, roll de canela, vinilos, dirección y horarios) con destellos "✦". La lista va duplicada y la fila se desplaza `translateX(-50%)` en 30s lineal y sin fin, para que el bucle no se note. La pauta del sistema agrega pausa al pasar el mouse. El boceto de la dirección C usa 28s, 34px de texto y 14px de padding.

### Disco de vinilo
- Un círculo de 340px en la home (360px en el boceto C) con surcos de `repeating-radial-gradient(circle, #14171B 0 6px, #22262C 6px 8px)`. En el centro, una etiqueta terracota de 122px (130px en el boceto C) con el logo crema. Gira 6s lineal y sin fin. Con `prefers-reduced-motion: reduce` queda quieto. La versión chica de la tarjeta de carta es un disco liso de 50px, sin surcos.

### Sobre de cafés (signature)
- Un sobre de 250×350px centrado en el escenario (600px de alto, con `perspective: 1400px`). El cuerpo (radio de 6px arriba y 18px abajo, contorno bordó de 3px y sombra dura `8px 10px 0` bordó) lleva el color `--pack`, el logo, la rana y la etiqueta en mono de 11px. Un brillo diagonal blanco (22%) lo recorre cada 3,6s. Arriba, una tapa de 40px con perforación de rayas y un corte punteado crema que dice "✂ cortá acá". Debajo, una pastilla crema inclinada −2° con contorno bordó de 3px y sombra de 4px con la indicación (Barlow Condensed 800 itálica de 22px). Flota 3,2s ease-in-out (sube 10px y se mece ±1,5°) y con el mouse arriba, 1,4s; al tocarlo tiembla 0,18s. Las figuritas salen del sobre y giran en 3D (0,35s, `cubic-bezier(.2,.8,.2,1)`). El detalle abre sobre un velo carbón al 70%, en una tarjeta crema de 28px de radio, 26px de padding, sombra de 10px y ancho máximo de 760px, con un botón de cierre redondo de 44px. Con `prefers-reduced-motion: reduce` se frenan la flotación y el brillo y se quitan las transiciones.

### La rana
- Una sola tinta, línea gruesa y temblorosa, sin relleno, sin sombras ni degradés: carbón sobre fondos claros, crema sobre carbón, verde en piezas de marca y bordó en eventos. La cara, los ojos y la mano salen siempre del logo vectorizado. Como SVG, en línea solo si se anima; si no, como `<img>`. La decorativa lleva `alt=""`; la que comunica algo lleva texto real al lado.

### Movimiento
- Disco que gira: 6s por vuelta, linear, sin fin. Rana que respira: 3,2s y sube 5px, ease-in-out. Cinta de texto: 30s el recorrido, linear, con pausa al pasar el mouse. Botón sticker: 150ms ease-out. Apertura del sobre: ≈ 2s, `cubic-bezier(.2,.8,.2,1)`. Con `prefers-reduced-motion: reduce`, todo queda quieto y las figuritas aparecen directo en su lugar.

## Do's and Don'ts

### Do:
- **Do** usar siempre las variables de los tokens (`var(--terracota)`, `var(--radius-md)`), nunca los valores sueltos.
- **Do** alternar secciones de día (durazno) y de noche (carbón, `data-theme="noche"`) al bajar por la página.
- **Do** darle a todo control o tarjeta contorno de 3px en `border` y sombra dura sin desenfoque.
- **Do** mantener el texto a 4,5:1 como mínimo en los dos temas y el foco visible de 3px con 3-4px de separación.
- **Do** dibujar los pocos íconos necesarios (WhatsApp, menú, flecha) con la misma línea gruesa y redondeada, en `currentColor`, de 22 a 28px.
- **Do** usar fotos en clave baja, con una sola luz cálida y fondo oscuro, como en el Instagram del café.
- **Do** escribir `[a confirmar]` donde falte un dato del café.

### Don't:
- **Don't** usar librerías de íconos.
- **Don't** componer el logo "geacofi" con una fuente.
- **Don't** redibujar la cara, los ojos o la mano de la rana, ni ponerle verde realista en el cuerpo, estirarla hasta que aparezca un cuello, usar línea fina, sombras o degradés, ni darle ojos redondos con sonrisa grande como cara base (la vuelve una mascota infantil).
- **Don't** poner más de dos ranas en la misma pantalla.
- **Don't** usar los colores `tostador-*` fuera de las figuritas, ni los logos o el packaging de los tostadores (solo sus nombres).
- **Don't** usar sombras con desenfoque ni brillos suaves en controles y tarjetas.
- **Don't** usar Gaegu en texto de lectura ni por debajo de 30px.
- **Don't** usar ámbar como relleno de día ni `status-open` como texto.
- **Don't** animar nada que no se detenga con `prefers-reduced-motion: reduce`.
