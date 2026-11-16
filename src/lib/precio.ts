/** 5500 -> "$ 5.500" (pesos enteros, punto de miles). Sin precio: "[a confirmar]". */
export function formatPrecio(pesos?: number | null): string {
  if (pesos == null) return '[a confirmar]';
  if (!Number.isInteger(pesos) || pesos < 0) throw new RangeError(`precio inválido: ${pesos}`);
  return `$ ${String(pesos).replace(/\B(?=(\d{3})+(?!\d))/g, '.')}`;
}
