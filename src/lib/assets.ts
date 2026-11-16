// URLs de los SVG de la rana y del lettering. Nunca se redibujan: se copiaron tal cual de docs/.
const ranas = import.meta.glob<string>('../assets/rana/*.svg', { eager: true, query: '?url', import: 'default' });
const logos = import.meta.glob<string>('../assets/logos/*.svg', { eager: true, query: '?url', import: 'default' });

export type Pose =
  | 'oficial' | 'barra' | 'filtrado' | 'moliendo' | 'espresso' | 'togo'
  | 'carta' | 'senala' | 'saluda' | 'asoma' | 'dormido' | 'dj' | 'guino'
  | 'latte' | 'chemex' | 'tomando' | 'bandeja';
export type Tinta = 'carbon' | 'crema' | 'verde';

export function ranaUrl(pose: Pose | string, tinta: Tinta = 'verde'): string {
  const url = ranas[`../assets/rana/${pose}-${tinta}.svg`];
  if (!url) throw new Error(`rana sin SVG: ${pose}-${tinta}`);
  return url;
}

/** Lettering "geacofi": carbon, crema o bordo. */
export function logoUrl(tinta: 'carbon' | 'crema' | 'bordo' = 'bordo'): string {
  return logos[`../assets/logos/geacofi-logo-${tinta}.svg`];
}
