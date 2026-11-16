# Datos del sitio

Todo lo que cambia seguido vive en archivos de datos, no en el diseño. El café los edita y el sitio se actualiza solo. Cuatro archivos: `carta.json`, `cafes.json`, `eventos.json` y `local.json`. Si al dueño le resulta más cómodo, cada uno puede ser una pestaña de una planilla de Google publicada como CSV, con las mismas columnas.

## cafes.json — el sobre de figuritas

Los tostadores son fijos; los cafés rotan.

```json
{
  "tostadores": [
    { "id": "komun", "nombre": "Komún Tostadores", "color": "tostador-komun", "tinta": "carbon" },
    { "id": "momo", "nombre": "MOMO", "color": "tostador-momo", "tinta": "crema", "holo": true },
    { "id": "motofeca", "nombre": "La Motofeca", "color": "tostador-motofeca", "tinta": "carbon" },
    { "id": "pepe", "nombre": "Lo de Pepe Tostadores", "color": "tostador-pepe", "tinta": "crema" }
  ],
  "cafes": [
    {
      "id": "momo-rift-guji",
      "tostador": "momo",
      "nombre": "Rift Guji",
      "origen": "Guji, Etiopía",
      "proceso": "Natural",
      "variedad": "Variedades nativas",
      "notas": ["miel", "damascos", "floral"],
      "en_barra": true,
      "pose": "rana-filtrado"
    }
  ]
}
```

| Campo | Obligatorio | Nota |
| --- | --- | --- |
| id | sí | minúsculas y guiones, único |
| tostador | sí | uno de los `id` de tostadores |
| nombre | sí | como lo escribe el tostador |
| origen | no | país o región |
| proceso | no | Lavado, Natural, Honey… |
| variedad | no | |
| notas | no | hasta 3, en minúscula |
| mood | no | para quien lo usa (La Motofeca: Funky, Fusion) |
| en_barra | sí | `false` lo saca del sobre sin borrarlo |
| pose | no | ilustración de la rana; si falta, se elige una al azar |

Reglas del sobre: 5 figuritas, como máximo 2 del mismo tostador, solo cafés con `en_barra: true`. Un tostador sin cafés cargados muestra "café de la semana · preguntá en la barra".

## carta.json

```json
{
  "actualizada": "2026-11-15",
  "categorias": [
    {
      "id": "calientes", "nombre": "calientes", "lado": "Lado A",
      "items": [
        { "nombre": "espresso", "descripcion": "shot chiquito", "precio": 3700, "destacado": true, "pose": "espresso" },
        { "nombre": "latte", "descripcion": "espresso + leche · grande", "precio": 5500, "opciones": ["caramelo", "vainilla", "avellana"] }
      ]
    }
  ]
}
```

| Campo del ítem | Obligatorio | Nota |
| --- | --- | --- |
| nombre | sí | en minúscula, como en la carta |
| descripcion | no | |
| precio | sí | pesos, número entero |
| opciones | no | sabores o variantes |
| destacado | no | `true` lo suma al carrusel "lo que más sale" de la home. Conviene marcar entre 6 y 8 |
| pose | no | pose de la rana que ilustra la tarjeta del carrusel: `espresso`, `latte`, `togo`, `filtrado`, `chemex`, `tomando`, `bandeja` o `moliendo`. Sin `pose`, usa `espresso` |

Precios en pesos, como número entero; el sitio los formatea `$ 5.500` en DM Mono. Categorías actuales: calientes (Lado A), fríos (Lado B), filtrados (Edición especial), salado (Lado C), panadería y pastelería (Bonus track).

## eventos.json

```json
[
  {
    "id": "cafe-y-eso-2026-02",
    "titulo": "café y eso…",
    "fecha": "2026-02-13", "desde": "17:00", "hasta": "21:00",
    "descripcion": "Vinyl set, pop-up de lostclub y feria de vinilos.",
    "flyer": "eventos/cafe-y-eso.webp",
    "reserva": "whatsapp"
  }
]
```

El sitio separa solo: fecha futura → "próximos"; pasada → "ya pasaron". Sin próximos, se muestra el estado vacío con la rana durmiendo.

## local.json

```json
{
  "direccion": "9 de Julio 996", "ciudad": "Corrientes",
  "horarios": [{ "dias": "[a confirmar]", "turnos": ["07:00-13:00", "17:00-21:00"] }],
  "whatsapp": "https://wa.me/message/KFA3BBGBV2PLA1",
  "instagram": "https://instagram.com/geacofi",
  "maps": "https://maps.google.com/?q=9+de+Julio+996+Corrientes"
}
```

La pastilla "abierto / cerrado" del hero se calcula con estos horarios en la zona horaria de Argentina (UTC−3).
