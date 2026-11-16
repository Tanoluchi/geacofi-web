import type { Evento } from './types.ts';
import { ahoraAR, horaCorta } from './horario.ts';

const DIAS = ['dom', 'lun', 'mar', 'mié', 'jue', 'vie', 'sáb'];
const aMin = (hhmm: string) => Number(hhmm.slice(0, 2)) * 60 + Number(hhmm.slice(3));

/** Próximos (hoy incluido, el más cercano primero) y ya pasaron (el más reciente primero). */
export function partirEventos(eventos: Evento[], now: Date = new Date()) {
  const hoy = ahoraAR(now).fecha;
  const porFecha = (a: Evento, b: Evento) => a.fecha.localeCompare(b.fecha);
  return {
    proximos: eventos.filter((e) => e.fecha >= hoy).sort(porFecha),
    pasados: eventos.filter((e) => e.fecha < hoy).sort((a, b) => porFecha(b, a)),
  };
}

/** "vie 13/2 · 17 a 21" o "dom 23/11 · 16 hs" */
export function fechaFlyer(e: Evento): string {
  const [y, m, d] = e.fecha.split('-').map(Number);
  const dia = DIAS[new Date(Date.UTC(y, m - 1, d)).getUTCDay()];
  const base = `${dia} ${d}/${m}`;
  if (!e.desde) return base;
  const desde = horaCorta(aMin(e.desde));
  return e.hasta ? `${base} · ${desde} a ${horaCorta(aMin(e.hasta))}` : `${base} · ${desde} hs`;
}
