# Geacofi

> café, discos y eso…

Sistema de diseño del sitio de **Geacofi**, cafetería de especialidad en 9 de Julio 996, Corrientes Capital. Trabaja con cafés de tostadores invitados (Komún, MOMO, La Motofeca y Lo de Pepe) y organiza sets de vinilos, catas y pop-ups. Dirección de arte elegida: **C · Café y eso**, la web como un flyer que se mueve.

Empezá por acá. Las secciones **La rana**, **Datos del sitio** e **Implementación** completan este libro.

## Personalidad

Sabe mucho de café y no se lo toma tan en serio. Seis rasgos guían cada decisión:

| Rasgo | En la interfaz |
| --- | --- |
| pachorra | Ritmo lento, aire generoso, animaciones suaves. Nada grita "comprá ya". |
| sabe, pero no presume | Explicaciones de una línea. Los datos de barista son detalle, nunca barrera. |
| hecho a mano | Lettering manuscrito, la rana dibujada, contornos gruesos con temblor. Sin íconos de librería. |
| humor de barra | Microcopy en minúscula y con voz propia. |
| cultura de vinilo | Disco que gira, carta como lado A y lado B, fechas en estilo flyer. |
| de barrio, con estándar | WhatsApp como canal principal, cómo llegar siempre a mano. |

## Voz y textos

- **Minúsculas** en títulos, botones y nombres de la carta ("ver la carta", "spicy orange"). Mayúsculas solo en etiquetas en mono.
- **Voseo rioplatense**: "pasá", "escribinos", "preguntá en la barra".
- **Diminutivos y guiños** como en la carta: "shot chiquito", "huevito revuelto", "latte pero con hielo".
- **Frases cortas**. Un botón dice exactamente lo que pasa: "escribinos por WhatsApp", no "contacto".
- **No inventar**: precios, horarios y cafés salen de los datos del café. Lo que falta se escribe como `[a confirmar]` hasta tenerlo.

Ejemplos:

| Situación | Sí | No |
| --- | --- | --- |
| Botón principal | ver la carta | Descubrí nuestra propuesta |
| Sin eventos | por ahora no hay eventos anunciados | No se encontraron resultados |
| Fuera de horario | volvemos a las 17 | Cerrado |
| Confirmación | ¡listo! te respondemos pronto | Su mensaje fue enviado con éxito |
| Café rotativo | café de la semana · preguntá en la barra | Producto no disponible |

## Fundamentos visuales

**Dos registros.** De día, todo es papel durazno, dibujado y con humor (`surface` = `durazno`). De noche, secciones carbón que traen la luz baja del local (`surface` = `carbon`, tema *Noche*). Alternarlos al bajar por la página es parte de la experiencia.

**Color.** Proporción sugerida: durazno 35 · crema 20 · terracota 20 · carbón 15 · bordó 8 · verde 2. El ámbar vive en las fotos; en la interfaz solo es texto chico sobre carbón. Los colores `tostador-*` se usan únicamente en las figuritas del sobre de cafés.

**Tipografía.** Cuatro familias de Google Fonts, cada una con un trabajo:
- **Gaegu** (`display`): títulos manuscritos. Solo en tamaños grandes, color `heading`.
- **Barlow Condensed** itálica (`cond`): botones, navegación, fechas y categorías. Es la voz de flyer.
- **Nunito** (`body`): todo lo que se lee.
- **DM Mono** (`mono`): precios, horarios y etiquetas.

El logo **no** es una fuente: es el lettering original, que va siempre como imagen (grupo *Logos*).

**Forma.** Todo control o tarjeta lleva contorno `border-ink` (3 px) en `border` y una sombra dura sin desenfoque (`sticker`, `card`). Los botones se inclinan entre −2° y 2°, como stickers pegados. Radios generosos: `radius-md` en botones, `radius-lg` en tarjetas, `radius-pill` en chips.

**Fotografía.** Clave baja, una sola luz cálida y fondo oscuro, como en el Instagram del café. En la dirección C las fotos van recortadas en círculo con contorno bordó, o como flyers inclinados. Las de Instagram son de baja resolución: para el sitio final hace falta una sesión o los originales.

**Patrones y recursos.** Disco de vinilo (surcos con `repeating-radial-gradient` en carbón), cinta de texto terracota levemente inclinada, destellos de cuatro puntas, papelitos y granos de café.

## Iconografía

No se usan librerías de íconos. Lo poco que hace falta se dibuja con la misma línea gruesa y redondeada (WhatsApp, menú, flecha) en `currentColor`, a 22-28 px. Los íconos de la carta impresa (taza, vaso, sándwich, gotero) se pueden vectorizar del original cuando se necesiten.

## La rana en la interfaz

Es la anfitriona: aparece en el hero (detrás de la barra), en cada página como guía, en los estados vacíos y de carga, y asomándose en el pie. Nunca más de dos ranas en la misma pantalla. Las reglas completas están en la sección **La rana**.

## Movimiento

Liviano y siempre opcional. Con `prefers-reduced-motion: reduce`, todo queda quieto.

| Animación | Duración | Curva |
| --- | --- | --- |
| Disco que gira | 6 s por vuelta, sin fin | linear |
| Rana que respira | 3,2 s, sube 5 px | ease-in-out |
| Cinta de texto | 30 s el recorrido, pausa al pasar el mouse | linear |
| Botón sticker | 150 ms | ease-out |
| Apertura del sobre de cafés | ≈ 2 s en total | cubic-bezier(.2,.8,.2,1) |
| Rana moliendo (carga) | 1,2 s por vuelta de manija | linear |

## Accesibilidad

- Texto a 4,5:1 como mínimo en los dos temas; todos los pares de este sistema lo cumplen.
- Foco visible: `focus` de 3 px con 3-4 px de separación.
- Áreas táctiles de 44 px como mínimo (botones: 48 px).
- La rana decorativa lleva `alt=""`; la que comunica algo (estado vacío, carga) lleva texto real al lado.
- El sobre de cafés tiene una lista de todos los cafés debajo, para lectores de pantalla y para quien no quiera jugar.

## Componentes

Botón sticker · Tarjeta de carta (tracklist) · Figurita de café · Ticket de visita · Estado vacío. Cada uno tiene su vista previa y sus pautas de uso.

## Pendiente con el dueño

Días de apertura · cafés actuales en barra (y los de Lo de Pepe) · próximos eventos · fotos en alta · historia del nombre "gea".
