import cartaJson from '../data/carta.json';
import cafesJson from '../data/cafes.json';
import eventosJson from '../data/eventos.json';
import localJson from '../data/local.json';
import type { Carta, Cafes, Evento, Local } from './types.ts';

export const carta = cartaJson as Carta;
export const cafes = cafesJson as Cafes;
export const eventos = eventosJson as Evento[];
export const local = localJson as Local;

/** "7:00 → 13:00 · 17:00 → 21:00" (como en el pie de los mockups) */
export const turnosTexto = local.horarios
  .flatMap((h) => h.turnos)
  .map((t) => t.split('-').map((x) => `${Number(x.slice(0, 2))}:${x.slice(3)}`).join(' → '))
  .join(' · ');
