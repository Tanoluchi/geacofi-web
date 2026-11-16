import type { Horario } from './types.ts';

export interface EstadoLocal { abierto: boolean; texto: string }

const AR_OFFSET_MS = -3 * 3600_000; // America/Argentina/Buenos_Aires, sin horario de verano

/** Hora y fecha de pared en Argentina para un instante dado. */
export function ahoraAR(now: Date): { minutos: number; fecha: string; dia: number } {
  const d = new Date(now.getTime() + AR_OFFSET_MS);
  return { minutos: d.getUTCHours() * 60 + d.getUTCMinutes(), fecha: d.toISOString().slice(0, 10), dia: d.getUTCDay() };
}

const DIAS = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

const aMin = (hhmm: string) => {
  const [h, m] = hhmm.split(':').map(Number);
  return h * 60 + m;
};
/** 420 -> "7", 1050 -> "17:30" */
export const horaCorta = (min: number) =>
  min % 60 ? `${Math.floor(min / 60)}:${String(min % 60).padStart(2, '0')}` : String(min / 60);
/** "07:00" -> "7:00" (para mostrar turnos) */
export const horaLarga = (hhmm: string) => `${Number(hhmm.slice(0, 2))}:${hhmm.slice(3)}`;

/** Turnos como [desde, hasta] en minutos, ordenados. `dia` (0 = domingo) filtra por `semana`; sin `semana`, aplica todos los días. */
export function turnosEnMinutos(horarios: Horario[], dia?: number): [number, number][] {
  return horarios
    .filter((h) => dia === undefined || !h.semana || h.semana.includes(dia))
    .flatMap((h) => h.turnos)
    .map((t) => t.split('-').map(aMin) as [number, number])
    .sort((a, b) => a[0] - b[0]);
}

export function estadoLocal(horarios: Horario[], now: Date = new Date()): EstadoLocal {
  if (!turnosEnMinutos(horarios).length) return { abierto: false, texto: 'horarios [a confirmar]' };
  const { minutos, dia } = ahoraAR(now);
  const hoy = turnosEnMinutos(horarios, dia);
  const actual = hoy.find(([d, h]) => minutos >= d && minutos < h);
  if (actual) return { abierto: true, texto: `abierto hasta las ${horaCorta(actual[1])}` };
  const siguiente = hoy.find(([d]) => d > minutos);
  if (siguiente) return { abierto: false, texto: `volvemos a las ${horaCorta(siguiente[0])}` };
  for (let n = 1; n <= 7; n++) {
    const turnos = turnosEnMinutos(horarios, (dia + n) % 7);
    if (turnos.length) {
      const cuando = n === 1 ? 'mañana' : `el ${DIAS[(dia + n) % 7]}`;
      return { abierto: false, texto: `volvemos ${cuando} a las ${horaCorta(turnos[0][0])}` };
    }
  }
  return { abierto: false, texto: 'horarios [a confirmar]' };
}
