import type { Horario } from './types.ts';

export interface EstadoLocal { abierto: boolean; texto: string }

const AR_OFFSET_MS = -3 * 3600_000; // America/Argentina/Buenos_Aires, sin horario de verano

/** Hora y fecha de pared en Argentina para un instante dado. */
export function ahoraAR(now: Date): { minutos: number; fecha: string } {
  const d = new Date(now.getTime() + AR_OFFSET_MS);
  return { minutos: d.getUTCHours() * 60 + d.getUTCMinutes(), fecha: d.toISOString().slice(0, 10) };
}

const aMin = (hhmm: string) => {
  const [h, m] = hhmm.split(':').map(Number);
  return h * 60 + m;
};
/** 420 -> "7", 1050 -> "17:30" */
export const horaCorta = (min: number) =>
  min % 60 ? `${Math.floor(min / 60)}:${String(min % 60).padStart(2, '0')}` : String(min / 60);
/** "07:00" -> "7:00" (para mostrar turnos) */
export const horaLarga = (hhmm: string) => `${Number(hhmm.slice(0, 2))}:${hhmm.slice(3)}`;

/** Turnos como [desde, hasta] en minutos, ordenados. */
export function turnosEnMinutos(horarios: Horario[]): [number, number][] {
  // shortcut: los días son "[a confirmar]", así que se asume que aplican todos los días; interpretar `dias` cuando el café los confirme.
  return horarios
    .flatMap((h) => h.turnos)
    .map((t) => t.split('-').map(aMin) as [number, number])
    .sort((a, b) => a[0] - b[0]);
}

export function estadoLocal(horarios: Horario[], now: Date = new Date()): EstadoLocal {
  const turnos = turnosEnMinutos(horarios);
  if (!turnos.length) return { abierto: false, texto: 'horarios [a confirmar]' };
  const { minutos } = ahoraAR(now);
  const actual = turnos.find(([d, h]) => minutos >= d && minutos < h);
  if (actual) return { abierto: true, texto: `abierto hasta las ${horaCorta(actual[1])}` };
  const siguiente = turnos.find(([d]) => d > minutos);
  return siguiente
    ? { abierto: false, texto: `volvemos a las ${horaCorta(siguiente[0])}` }
    : { abierto: false, texto: `volvemos mañana a las ${horaCorta(turnos[0][0])}` };
}
