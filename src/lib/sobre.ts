import type { Cafe, Tostador } from './types.ts';

export const TEXTO_SIN_CAFES = 'café de la semana · preguntá en la barra';
/** Poses de rana para figuritas de café (assets en src/assets/rana). */
export const POSES_CAFE = ['filtrado', 'moliendo', 'oficial', 'espresso', 'togo'];

export type Figurita =
  | { tipo: 'cafe'; tostador: Tostador; cafe: Cafe; pose: string }
  | { tipo: 'semana'; tostador: Tostador; texto: string; pose: string };

const MAX_POR_TOSTADOR = 2;
const TAMANO = 5;

function barajar<T>(xs: T[], rng: () => number): T[] {
  const a = [...xs];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

/** 5 figuritas, máx. 2 por tostador, solo en_barra. Un tostador sin cafés aporta la figurita "café de la semana". */
export function elegirSobre(
  tostadores: Tostador[],
  cafes: Cafe[],
  rng: () => number = Math.random,
): Figurita[] {
  const poseAlAzar = () => POSES_CAFE[Math.floor(rng() * POSES_CAFE.length)];
  const pool: Figurita[] = tostadores.flatMap((t): Figurita[] => {
    const suyos = cafes.filter((c) => c.tostador === t.id && c.en_barra);
    if (!suyos.length) return [{ tipo: 'semana', tostador: t, texto: TEXTO_SIN_CAFES, pose: 'espresso' }];
    return suyos.map((cafe) => ({
      tipo: 'cafe', tostador: t, cafe,
      pose: (cafe.pose ?? poseAlAzar()).replace(/^rana-/, ''),
    }));
  });
  const cuenta = new Map<string, number>();
  const elegidas: Figurita[] = [];
  for (const f of barajar(pool, rng)) {
    if (elegidas.length === TAMANO) break;
    const n = cuenta.get(f.tostador.id) ?? 0;
    if (n >= MAX_POR_TOSTADOR) continue;
    cuenta.set(f.tostador.id, n + 1);
    elegidas.push(f);
  }
  return elegidas;
}
