import { test } from 'node:test';
import assert from 'node:assert/strict';
import { formatPrecio } from './precio.ts';
import { estadoLocal } from './horario.ts';
import { partirEventos, fechaFlyer } from './eventos.ts';
import { elegirSobre, TEXTO_SIN_CAFES } from './sobre.ts';
import type { Cafe, Tostador } from './types.ts';

const H = [{ dias: '[a confirmar]', turnos: ['07:00-13:00', '17:00-21:00'] }];
// hora Argentina (UTC-3) -> instante
const ar = (iso: string) => new Date(`${iso}-03:00`);

test('formatPrecio', () => {
  assert.equal(formatPrecio(5500), '$ 5.500');
  assert.equal(formatPrecio(900), '$ 900');
  assert.equal(formatPrecio(1234567), '$ 1.234.567');
  assert.throws(() => formatPrecio(12.5));
});

test('formatPrecio: sin precio muestra [a confirmar]', () => {
  assert.equal(formatPrecio(undefined), '[a confirmar]');
  assert.equal(formatPrecio(null), '[a confirmar]');
  assert.equal(formatPrecio(5500), '$ 5.500');
  assert.equal(formatPrecio(0), '$ 0');
});

test('estadoLocal en hora de Argentina', () => {
  assert.deepEqual(estadoLocal(H, ar('2026-11-15T09:00:00')), { abierto: true, texto: 'abierto hasta las 13' });
  assert.deepEqual(estadoLocal(H, ar('2026-11-15T13:00:00')), { abierto: false, texto: 'volvemos a las 17' });
  assert.deepEqual(estadoLocal(H, ar('2026-11-15T05:00:00')), { abierto: false, texto: 'volvemos a las 7' });
  assert.deepEqual(estadoLocal(H, ar('2026-11-15T21:00:00')), { abierto: false, texto: 'volvemos mañana a las 7' });
  // 23:30 UTC del 15 = 20:30 en Argentina -> abierto, aunque en UTC ya sería de noche
  assert.equal(estadoLocal(H, new Date('2026-11-15T23:30:00Z')).abierto, true);
});

test('eventos: próximos / ya pasaron', () => {
  const ev = [
    { id: 'a', titulo: 'a', fecha: '2026-02-13', desde: '17:00', hasta: '21:00' },
    { id: 'b', titulo: 'b', fecha: '2026-12-01' },
    { id: 'c', titulo: 'c', fecha: '2026-11-15' },
  ];
  const { proximos, pasados } = partirEventos(ev, ar('2026-11-15T10:00:00'));
  assert.deepEqual(proximos.map((e) => e.id), ['c', 'b']);
  assert.deepEqual(pasados.map((e) => e.id), ['a']);
  assert.equal(fechaFlyer(ev[0]), 'vie 13/2 · 17 a 21');
  assert.equal(fechaFlyer({ id: 'd', titulo: 'd', fecha: '2025-11-23', desde: '16:00' }), 'dom 23/11 · 16 hs');
});

const T: Tostador[] = ['a', 'b', 'c', 'd'].map((id) => ({ id, nombre: id, color: id, tinta: 'carbon' as const }));
const cafe = (t: string, n: number, en_barra = true): Cafe => ({ id: `${t}${n}`, tostador: t, nombre: `${t}${n}`, en_barra });
const CAFES = [...[1, 2, 3, 4].map((n) => cafe('a', n)), ...[1, 2, 3].map((n) => cafe('b', n)), cafe('c', 1), cafe('c', 2, false), cafe('c', 3, false)];

test('sobre: 5 figuritas, máx 2 por tostador, solo en_barra, sin cafés -> café de la semana', () => {
  for (let i = 0; i < 200; i++) {
    const s = elegirSobre(T, CAFES);
    assert.equal(s.length, 5);
    for (const t of T) assert.ok(s.filter((f) => f.tostador.id === t.id).length <= 2);
    for (const f of s) if (f.tipo === 'cafe') assert.equal(f.cafe.en_barra, true);
    assert.equal(new Set(s.map((f) => (f.tipo === 'cafe' ? f.cafe.id : 'semana'))).size, 5);
  }
  const todas = Array.from({ length: 200 }, () => elegirSobre(T, CAFES)).flat();
  const semana = todas.find((f) => f.tipo === 'semana');
  assert.ok(semana && semana.tostador.id === 'd' && semana.texto === TEXTO_SIN_CAFES);
});

test('sobre: normaliza pose rana-* y devuelve menos de 5 si las reglas no alcanzan', () => {
  const [uno] = elegirSobre(T.slice(0, 1), [{ ...cafe('a', 1), pose: 'rana-filtrado' }]);
  assert.ok(uno.tipo === 'cafe' && uno.pose === 'filtrado');
  assert.equal(elegirSobre(T.slice(0, 1), [cafe('a', 1), cafe('a', 2), cafe('a', 3)]).length, 2);
});
