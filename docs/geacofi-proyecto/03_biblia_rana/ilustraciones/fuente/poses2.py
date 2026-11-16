from rana import *

POSES = {}   # key -> (func, categoria, titulo, uso)


def pose(key, cat, title, use):
    def deco(f):
        POSES[key] = (f, cat, title, use)
        return f
    return deco


# ------------------------------------------------------------ UNIVERSO CAFÉ
@pose('oficial', 'cafe', 'Pose oficial', 'La del logo y el avatar. Hero, favicon, redes.')
def _():
    return Canvas()


@pose('filtrado', 'cafe', 'Preparando un filtrado', 'Pava cuello de cisne sobre V60. Sección filtrados.')
def _():
    cv = Canvas(seed=11)
    remove_cup(cv)
    cv.stroke([(384, 504), (376, 560), (474, 562), (470, 504)], closed=True, clear=True)
    cv.stroke([(470, 514), (498, 520), (496, 550), (472, 554)], jit=1)
    cv.stroke([(388, 538), (428, 542), (466, 538)], w=LW * .6, jit=.8)
    cv.stroke([(354, 452), (402, 504), (452, 504), (498, 452)], closed=True, clear=True)
    cv.stroke([(198, 424), (192, 474), (206, 510), (290, 512), (304, 474), (298, 424)], closed=True, clear=True)
    cv.stroke([(188, 420), (248, 404), (308, 420)], jit=1)
    cv.stroke([(234, 404), (248, 384), (264, 404)], jit=.8)
    cv.stroke([(300, 492), (334, 484), (352, 450), (374, 418), (398, 410)], jit=1)
    cv.stroke([(402, 418), (408, 434), (414, 452)], w=LW * .45, jit=.4)
    cv.hand()
    return cv


@pose('moliendo', 'cafe', 'Moliendo café', 'Molinillo manual. Pantalla de carga: la manija gira.')
def _():
    cv = Canvas(seed=7)
    remove_cup(cv)
    cv.stroke([(186, 440), (182, 494), (184, 550), (240, 555), (296, 550), (298, 494), (294, 440)], closed=True, clear=True)
    cv.stroke([(176, 436), (240, 426), (306, 436)], jit=1)
    cv.stroke([(200, 430), (240, 410), (280, 430)], jit=1)
    cv.stroke([(186, 498), (240, 506), (296, 498)], w=LW * .75)
    cv.stroke([(240, 412), (242, 388)], jit=.6)
    cv.stroke([(238, 388), (300, 382), (346, 378)], jit=.8)
    cv.stroke([(456, 430), (430, 400), (398, 382)], jit=1)
    cv.stroke([(450, 480), (420, 444), (396, 420)], jit=1)
    cv.stroke([(396, 376), (366, 368), (346, 382), (350, 410), (380, 422), (400, 410)], closed=True, clear=True, jit=1)
    cv.stroke([(358, 388), (382, 390)], w=LW * .5, jit=.5)
    cv.stroke([(360, 402), (384, 404)], w=LW * .5, jit=.5)
    cv.stroke([(330, 342), (352, 330), (378, 336)], w=LW * .55, jit=.6)
    cv.hand()
    return cv


@pose('barra', 'cafe', 'Detrás de la barra', 'Recibe con la taza lista. Hero alternativo, "visitanos".')
def _():
    cv = Canvas(pad=(110, 0, 120, 90), seed=21)
    remove_cup(cv, keep_hand=False)
    bar(cv, top=470, x0=-100, x1=650)
    machine(cv, 420, 290, w=180, bar_top=470)
    mug(cv, 270, 392, 1.0)
    cv.hand(at=(205, 398), scale=.8)
    return cv


@pose('espresso', 'cafe', 'Sirviendo un espresso', 'En la barra, con la cafetera. Carta: calientes.')
def _():
    cv = Canvas(pad=(60, 0, 140, 90), seed=23)
    remove_cup(cv, keep_hand=False)
    bar(cv, top=470, x0=-50, x1=670)
    gx, gy = machine(cv, 340, 270, w=200, bar_top=470)
    cv.stroke([(gx - 24, gy + 6), (gx - 70, gy + 10), (gx - 120, gy + 14)], w=LW * 1.4, jit=.8)
    cv.stroke([(gx, gy + 12), (gx + 1, gy + 50)], w=LW * .45, jit=.3)
    espresso_cup(cv, gx, gy + 54, .9)
    cv.hand(at=(gx - 140, gy + 30), scale=.75, rot_=-10)
    return cv


@pose('latte', 'cafe', 'Haciendo latte art', 'Jarrita de leche sobre la taza. Carta: con leche.')
def _():
    cv = Canvas(pad=(60, 0, 80, 90), seed=25)
    remove_cup(cv, keep_hand=False)
    bar(cv, top=470, x0=-50, x1=610)
    bowl(cv, 330, 400, .7, steam=False)
    tip = pitcher(cv, 250, 340, ang=-40)
    cv.stroke([tip, (tip[0] + 10, tip[1] + 30), (318, 404)], w=LW * .45, jit=.4)
    cv.hand(at=(214, 362), scale=.75, rot_=-25)
    return cv


@pose('togo', 'cafe', 'Café para llevar', 'Vaso con el logo. Pedidos por WhatsApp, "cómo llegar".')
def _():
    cv = Canvas(seed=27)
    remove_cup(cv)
    togo(cv, 262, 352, 1.0)
    cv.hand()
    return cv


@pose('tomando', 'cafe', 'Tomando café', 'Ojos cerrados, disfrutando. Carta, estado "abierto ahora".')
def _():
    cv = Canvas(seed=29)
    remove_cup(cv, keep_hand=False)
    eyes(cv, 'closed', 'closed')
    cv.clear(MOUTH)
    bowl(cv, 300, 262, .8, ang=-22, steam=False)
    steam_(cv, 352, 200, .8)
    cv.hand(at=(220, 318), scale=.85, rot_=-20)
    return cv


@pose('chemex', 'cafe', 'Con la chemex', 'La presenta orgullosa. Sección filtrados, redes.')
def _():
    cv = Canvas(seed=31)
    remove_cup(cv)
    x = 270
    cv.stroke([(x - 70, 340), (x - 14, 430), (x - 76, 548), (x + 76, 548), (x + 14, 430), (x + 70, 340)], closed=True, clear=True)
    cv.stroke([(x - 34, 410), (x - 40, 446), (x + 40, 446), (x + 34, 410)], closed=True, clear=True, w=LW * .85)
    cv.stroke([(x + 30, 426), (x + 60, 436), (x + 50, 452)], w=LW * .6, jit=.5)
    cv.stroke([(x - 60, 510), (x + 60, 510)], w=LW * .6, jit=.6)
    cv.hand(at=(196, 452), scale=.9)
    sparkle(cv, 400, 330, 1)
    return cv


@pose('bandeja', 'cafe', 'Llevando una bandeja', 'Dos cafés en camino. Promos, "pedí en la barra".')
def _():
    cv = Canvas(seed=33)
    remove_cup(cv, keep_hand=False)
    cv.stroke([(110, 430), (270, 420), (440, 430), (430, 452), (270, 446), (118, 452)], closed=True, clear=True)
    espresso_cup(cv, 200, 380, .8)
    espresso_cup(cv, 340, 378, .8)
    cv.hand(at=(150, 506), scale=.8)
    cv.hand(at=(410, 506), scale=.8, flip=True)
    return cv


# ------------------------------------------------------------ INTERACCIÓN DIGITAL
@pose('saluda', 'web', 'Saludando', 'Bienvenida en el hero.')
def _():
    cv = Canvas(pad=(110, 0, 0, 0), seed=41)
    remove_cup(cv, keep_hand=False)
    arm(cv, [(36, 372)], [(0, 300), (-24, 262)], [(66, 400)], [(30, 330), (14, 272)])
    cv.hand(at=(-6, 222), scale=.8, rot_=12)
    cv.stroke([(-78, 196), (-64, 178)], w=LW * .55, jit=.4)
    cv.stroke([(-86, 236), (-66, 232)], w=LW * .55, jit=.4)
    togo(cv, 300, 380, .8)
    cv.hand(at=(366, 470), scale=.7, flip=True)
    return cv


@pose('senala', 'web', 'Señalando', 'Junto a un botón: "ver la carta", "escribinos".')
def _():
    cv = Canvas(pad=(0, 0, 170, 0), seed=43)
    remove_cup(cv)
    togo(cv, 262, 352, 1.0)
    cv.hand()
    arm(cv, [(468, 372)], [(520, 352), (566, 344)], [(470, 420)], [(524, 400), (570, 392)])
    cv.stroke([(610, 352), (668, 346), (672, 364), (612, 372)], closed=True, clear=True, w=LW * .85)
    cv.hand(at=(596, 370), scale=.62, rot_=90, flip=True)
    return cv


@pose('asoma', 'web', 'Asomándose', 'Desde el borde de una sección o al final de la página.')
def _():
    cv = Canvas(pad=(0, 0, 0, 0), seed=45)
    cv.clear([(-10, 326), (560, 326), (560, 600), (-10, 600)])
    cv.stroke([(-4, 334), (180, 330), (360, 336), (544, 331)], jit=1.2)
    cv.hand(at=(150, 330), scale=.7)
    cv.hand(at=(392, 330), scale=.7, flip=True)
    return cv


@pose('cartel', 'web', 'Con el cartel', 'Anuncios: "abierto", promos, eventos.')
def _():
    cv = Canvas(pad=(0, 0, 0, 20), seed=47)
    remove_cup(cv, keep_hand=False)
    cv.stroke([(96, 352), (270, 344), (446, 352), (440, 540), (270, 548), (102, 540)], closed=True, clear=True)
    cv.logo((271, 446), scale=.5)
    cv.hand(at=(110, 452), scale=.75)
    cv.hand(at=(432, 452), scale=.75, flip=True)
    return cv


@pose('carta', 'web', 'Leyendo la carta', 'Página de la carta, "¿qué pido?".')
def _():
    cv = Canvas(seed=49)
    remove_cup(cv)
    eyes(cv, 'up', 'up')
    cv.stroke([(190, 340), (420, 330), (430, 560), (200, 566)], closed=True, clear=True)
    cv.logo((310, 378), scale=.22)
    for y, x2 in ((430, 400), (466, 380), (502, 396), (536, 370)):
        cv.stroke([(232, y), (x2, y - 4)], w=LW * .6, jit=.6)
    cv.hand()
    return cv


# ------------------------------------------------------------ CREATIVAS
@pose('bolsa', 'creativa', 'Con una bolsa de café', 'Café en grano, "nuestro café", tienda futura.')
def _():
    cv = Canvas(seed=51)
    remove_cup(cv)
    cv.stroke([(200, 360), (190, 560), (400, 560), (390, 360)], closed=True, clear=True)
    cv.stroke([(196, 360), (296, 340), (396, 360), (392, 392), (198, 392)], closed=True, clear=True)
    cv.logo((296, 456), scale=.26)
    for bx in (256, 300, 340):
        cv.stroke([(bx - 12, 512), (bx, 504), (bx + 12, 512), (bx, 520)], closed=True, w=LW * .55, jit=.4)
    cv.hand()
    return cv


@pose('dj', 'creativa', 'DJ con su taza', 'Eventos y "café y eso…". Concepto C.')
def _():
    cv = Canvas(pad=(40, 70, 50, 0), seed=53)
    cv.stroke([(18, 120), (40, 30), (140, -26), (270, -46), (400, -30), (490, 40), (510, 140)], w=LW * 1.25, jit=1)
    cv.stroke([(-14, 96), (-22, 140), (-10, 180), (30, 182), (40, 140), (34, 96)], closed=True, clear=True)
    cv.stroke([(482, 116), (476, 160), (488, 200), (528, 200), (536, 158), (524, 116)], closed=True, clear=True)
    for nx, ny in ((520, 10), (-20, 40)):
        cv.dot(nx, ny + 30, 9)
        cv.stroke([(nx + 8, ny + 28), (nx + 8, ny - 10), (nx + 28, ny)], w=LW * .6, jit=.4)
    return cv


@pose('dormido', 'creativa', 'Siesta con la taza', 'Fuera de horario: "volvemos a las 17".')
def _():
    cv = Canvas(pad=(0, 40, 40, 0), seed=55)
    eyes(cv, 'closed', 'closed')
    zzz(cv, 470, 20, 1.1)
    return cv


@pose('enamorado', 'creativa', 'Enamorado del café', 'Reseñas, "gracias por venir", San Valentín.')
def _():
    cv = Canvas(pad=(0, 0, 30, 0), seed=57)
    eyes(cv, 'heart', 'heart')
    mouth(cv, 'smile')
    heart(cv, 486, 40, .9)
    heart(cv, 520, 96, .65)
    return cv


# ------------------------------------------------------------ EXPRESIONES (sobre la pose oficial)
EXPR = {}


def expr(key, title, note):
    def deco(f):
        EXPR[key] = (f, title, note)
        return f
    return deco


@expr('relajado', 'Relajado (base)', 'El original: ojos entrecerrados con raya gruesa, boca casi recta.')
def _(cv): pass


@expr('feliz', 'Feliz', 'Ojos en arco hacia arriba y boca curvada.')
def _(cv):
    eyes(cv, 'happy', 'happy'); mouth(cv, 'smile')


@expr('sorprendido', 'Sorprendido', 'La raya del ojo se vuelve pupila y la boca una "o".')
def _(cv):
    eyes(cv, 'open', 'open'); mouth(cv, 'o')


@expr('guino', 'Divertido', 'Guiño con el ojo derecho y lengua afuera.')
def _(cv):
    eyes(cv, 'orig', 'wink'); mouth(cv, 'tongue')


@expr('concentrado', 'Concentrado', 'Raya del ojo más baja, boca ondulada y una gotita.')
def _(cv):
    eyes(cv, 'low', 'low'); mouth(cv, 'wavy')
    cv.ink([(478, 70), (488, 96), (480, 108), (468, 102), (470, 90)])


@expr('pensativo', 'Pensativo', 'Pupilas mirando arriba y puntitos.')
def _(cv):
    eyes(cv, 'up', 'up')
    cv.dot(486, 70, 7); cv.dot(508, 44, 9)


@expr('entusiasmado', 'Entusiasmado', 'Pupilas grandes, boca abierta y destellos.')
def _(cv):
    eyes(cv, 'open', 'open'); mouth(cv, 'open')
    sparkle(cv, 40, 40, 1.1); sparkle(cv, 500, 60, .9)
