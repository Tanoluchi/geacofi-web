/** 5500 -> "$ 5.500" (pesos enteros, punto de miles). */
export function formatPrecio(pesos: number): string {
  if (!Number.isInteger(pesos) || pesos < 0) throw new RangeError(`precio inválido: ${pesos}`);
  return `$ ${String(pesos).replace(/\B(?=(\d{3})+(?!\d))/g, '.')}`;
}
