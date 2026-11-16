"""Biblia de la rana v1: todas las poses salen del trazo original vectorizado del logo.
Coordenadas en el sistema del recorte original (540 x 570). La cara, el cuerpo y la mano
son píxeles del dibujo original; lo nuevo se dibuja con trazo de marcador y se vectoriza todo junto."""
import math, random, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
sys.path.insert(0, '/home/claude/geacofi/trace')
from trace import trace_svg

S = 3
LW = 13.5
ORIG = Image.open('/mnt/user-data/uploads/f52262eb-image.png').convert('L')
REF = Image.open('/home/claude/geacofi/trace/frog_ref3x.png')
BASE = np.asarray(REF.convert('L')) < 150
H0, W0 = BASE.shape

# logo "geacofi" (lettering original) a 3x
_t = ORIG.crop((80, 592, 624, 778))
LOGO = np.asarray(_t.resize((_t.width * S, _t.height * S), Image.LANCZOS)) < 150

HAND = [(92, 378), (118, 356), (162, 368), (224, 398), (226, 422), (194, 442), (194, 542), (150, 552), (92, 524)]
HAND_C = (159, 454)
ERASE = [(178, 298), (306, 298), (386, 394), (434, 410), (447, 468), (490, 470), (490, 580), (100, 580), (100, 550)]
EYE_IN = {'l': [(52, 130), (122, 127), (160, 144), (156, 154), (110, 158), (52, 157)],
          'r': [(374, 152), (440, 141), (456, 150), (458, 172), (420, 180), (377, 178)]}
EYE_C = {'l': (100, 145), 'r': (418, 163)}
MOUTH = [(86, 270), (442, 280), (442, 314), (86, 302)]


def catmull(pts, n=14, closed=False):
    p = list(pts)
    p = ([p[-1]] + p + [p[0], p[1]]) if closed else ([p[0]] + p + [p[-1]])
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for k in range(n):
            t = k / n; t2, t3 = t * t, t * t * t
            out.append(tuple(.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * t + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * t2
                                   + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * t3) for j in (0, 1)))
    out.append(p[1] if closed else p[-2])
    return out


def rot(pts, ang, c):
    a = math.radians(ang); ca, sa = math.cos(a), math.sin(a)
    return [(c[0] + (x - c[0]) * ca - (y - c[1]) * sa, c[1] + (x - c[0]) * sa + (y - c[1]) * ca) for x, y in pts]


def mv(pts, dx, dy, s=1.0, c=(0, 0)):
    return [(c[0] + (x - c[0]) * s + dx, c[1] + (y - c[1]) * s + dy) for x, y in pts]


class Canvas:
    def __init__(self, pad=(0, 0, 0, 0), seed=1, base=True):
        l, t, r, b = pad
        self.ox, self.oy = l, t
        self.w, self.h = W0 + (l + r) * S, H0 + (t + b) * S
        self.img = Image.new('L', (self.w, self.h), 0)
        if base:
            self.img.paste(Image.fromarray((BASE * 255).astype('uint8')), (l * S, t * S))
        self.d = ImageDraw.Draw(self.img)
        self.r = random.Random(seed)

    def P(self, x, y):
        return ((x + self.ox) * S, (y + self.oy) * S)

    def sc(self, pts):
        return [self.P(x, y) for x, y in pts]

    def clear(self, pts, smooth=False):
        self.d.polygon(self.sc(catmull(pts, closed=True) if smooth else pts), fill=0)

    def ink(self, pts, smooth=True):
        self.d.polygon(self.sc(catmull(pts, closed=True) if smooth else pts), fill=255)

    def dot(self, x, y, r):
        (X, Y) = self.P(x, y); R = r * S
        self.d.ellipse([X - R, Y - R, X + R, Y + R], fill=255)

    def stroke(self, pts, w=LW, closed=False, jit=1.3, clear=False):
        r = self.r
        p = [(x + r.uniform(-jit, jit), y + r.uniform(-jit, jit)) for x, y in pts]
        if clear and closed:
            self.clear(p, smooth=True)
        q = catmull(p, closed=closed)
        ph = r.uniform(0, 6)
        R0 = w * S / 2
        X0, Y0 = self.P(*q[0])
        self.d.ellipse([X0 - R0, Y0 - R0, X0 + R0, Y0 + R0], fill=255)
        for i in range(len(q) - 1):
            ww = w * (0.9 + 0.16 * math.sin(i * 0.23 + ph)) * S
            A, B = self.P(*q[i]), self.P(*q[i + 1])
            self.d.line([A, B], fill=255, width=int(ww))
            rr = ww / 2
            self.d.ellipse([B[0] - rr, B[1] - rr, B[0] + rr, B[1] + rr], fill=255)

    def paste_arr(self, arr, at, scale=1.0, rot_=0, flip=False, clear_blob=True, close_it=14):
        im = Image.fromarray((arr * 255).astype('uint8'))
        if flip:
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
        if scale != 1 or rot_:
            im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.LANCZOS).rotate(rot_, expand=True, resample=Image.BICUBIC)
        ink = np.asarray(im) > 110
        X, Y = self.P(*at)
        ox, oy = int(X - im.width / 2), int(Y - im.height / 2)
        if clear_blob:
            blob = ndimage.binary_fill_holes(ndimage.binary_closing(ink, structure=np.ones((3, 3)), iterations=close_it))
            blob = ndimage.binary_dilation(blob, iterations=2)
            self.img.paste(0, (ox, oy), Image.fromarray((blob * 255).astype('uint8')))
        self.img.paste(255, (ox, oy), Image.fromarray((ink * 255).astype('uint8')))

    def hand(self, at=HAND_C, scale=1.0, rot_=0, flip=False):
        m = Image.new('L', (W0, H0), 0)
        ImageDraw.Draw(m).polygon([(x * S, y * S) for x, y in HAND], fill=255)
        bb = m.getbbox()
        arr = (np.asarray(m.crop(bb)) > 0) & BASE[bb[1]:bb[3], bb[0]:bb[2]]
        self.paste_arr(arr, at, scale, rot_, flip)

    def logo(self, at, scale=0.3, rot_=0):
        self.paste_arr(LOGO, at, scale, rot_, clear_blob=False)

    def svg(self, color='#14171B'):
        a = np.asarray(self.img) > 127
        a = ndimage.binary_opening(a, structure=np.ones((3, 3)), iterations=3)
        return trace_svg(~a, color=color, scale=1 / S)


# ------------------------------------------------------------ piezas reutilizables
def remove_cup(cv, keep_hand=True):
    cv.clear(ERASE)
    cv.stroke([(170, 548), (262, 562), (366, 556), (444, 528), (478, 470)], jit=1.2)
    if not keep_hand:
        cv.clear(HAND)
        cv.stroke([(90, 500), (118, 534), (180, 550)], jit=1.2)


def eyes(cv, l='orig', r='orig'):
    for side, kind in (('l', l), ('r', r)):
        if kind == 'orig':
            continue
        cv.clear(EYE_IN[side])
        cx, cy = EYE_C[side]
        if kind == 'closed':
            cv.stroke([(cx - 34, cy - 2), (cx, cy + 9), (cx + 34, cy - 2)], w=LW * .8, jit=.6)
        elif kind == 'happy':
            cv.stroke([(cx - 32, cy + 8), (cx, cy - 6), (cx + 32, cy + 8)], w=LW * .8, jit=.6)
        elif kind == 'open':
            cv.dot(cx + 4, cy + 2, 8.5)
        elif kind == 'up':
            cv.dot(cx + 10, cy - 6, 7.5)
        elif kind == 'heart':
            x, y = cx + 2, cy + 2
            cv.ink([(x, y + 11), (x - 13, y - 1), (x - 11, y - 9), (x - 4, y - 10), (x, y - 4), (x + 4, y - 10), (x + 11, y - 9), (x + 13, y - 1)])
        elif kind == 'wink':
            cv.stroke([(cx - 34, cy + 2), (cx + 34, cy + 2)], w=LW * .8, jit=.6)
        elif kind == 'low':
            cv.stroke([(cx - 30, cy + 6), (cx + 30, cy + 6)], w=LW * 1.1, jit=.5)


def mouth(cv, kind):
    cv.clear(MOUTH)
    if kind == 'smile':
        cv.stroke([(98, 278), (170, 300), (270, 306), (370, 300), (436, 282)], jit=1.2)
    elif kind == 'o':
        cv.stroke([(258, 284), (246, 296), (256, 312), (276, 312), (284, 296), (274, 284)], closed=True, w=LW * .9, jit=.6)
    elif kind == 'wavy':
        cv.stroke([(130, 292), (190, 282), (250, 296), (310, 282), (370, 296), (420, 288)], jit=1)
    elif kind == 'tongue':
        cv.stroke([(98, 288), (200, 290), (300, 292), (436, 298)], jit=1.2)
        cv.stroke([(296, 296), (300, 318), (322, 322), (326, 298)], w=LW * .8, jit=.6)
    elif kind == 'open':
        cv.stroke([(150, 288), (270, 292), (390, 290), (350, 330), (270, 340), (190, 330)], closed=True, jit=1)


def bowl(cv, x, y, s=1.0, ang=0, steam=True):
    def T(p):
        return rot(mv(p, 0, 0), ang, (x, y))
    body = [(x - 86 * s, y), (x - 70 * s, y + 60 * s), (x - 20 * s, y + 92 * s), (x + 40 * s, y + 90 * s), (x + 76 * s, y + 50 * s), (x + 88 * s, y + 4 * s)]
    cv.stroke(T([(x + 80 * s, y + 6 * s), (x + 106 * s, y + 18 * s), (x + 86 * s, y + 52 * s)]))
    cv.stroke(T(body), closed=True, clear=True, jit=1.4)
    cv.stroke(T([(x - 86 * s, y), (x, y + 8 * s), (x + 88 * s, y + 4 * s)]), jit=1)
    if steam:
        steam_(cv, x - 10, y - 20, s)


def steam_(cv, x, y, s=1.0):
    cv.stroke([(x, y), (x + 8 * s, y - 16 * s), (x - 2 * s, y - 32 * s), (x + 6 * s, y - 50 * s)], w=LW * .75, jit=.6)
    cv.stroke([(x + 22 * s, y - 4 * s), (x + 30 * s, y - 20 * s), (x + 20 * s, y - 36 * s), (x + 28 * s, y - 54 * s)], w=LW * .75, jit=.6)


def mug(cv, x, y, s=1.0, steam=True):
    """Taza recta con asa; (x,y) = centro de la boca."""
    cv.stroke([(x + 40 * s, y + 14 * s), (x + 66 * s, y + 20 * s), (x + 64 * s, y + 50 * s), (x + 40 * s, y + 56 * s)])
    cv.stroke([(x - 44 * s, y), (x - 40 * s, y + 70 * s), (x - 20 * s, y + 80 * s), (x + 20 * s, y + 80 * s), (x + 40 * s, y + 70 * s), (x + 44 * s, y)], closed=True, clear=True)
    if steam:
        steam_(cv, x - 10, y - 18, s)


def espresso_cup(cv, x, y, s=1.0):
    cv.stroke([(x - 46 * s, y + 46 * s), (x, y + 54 * s), (x + 46 * s, y + 46 * s)], jit=.8)
    cv.stroke([(x + 28 * s, y + 8 * s), (x + 46 * s, y + 12 * s), (x + 44 * s, y + 30 * s), (x + 26 * s, y + 34 * s)], w=LW * .85)
    cv.stroke([(x - 32 * s, y), (x - 28 * s, y + 36 * s), (x, y + 44 * s), (x + 28 * s, y + 36 * s), (x + 32 * s, y)], closed=True, clear=True)


def togo(cv, x, y, s=1.0, logo=True):
    """Vaso para llevar; (x,y) = centro de la tapa."""
    cv.stroke([(x - 46 * s, y + 24 * s), (x - 34 * s, y + 196 * s), (x + 34 * s, y + 196 * s), (x + 46 * s, y + 24 * s)], closed=True, clear=True)
    cv.stroke([(x - 54 * s, y + 24 * s), (x - 48 * s, y), (x + 48 * s, y), (x + 54 * s, y + 24 * s)], closed=True, clear=True)
    cv.stroke([(x - 42 * s, y + 70 * s), (x + 42 * s, y + 70 * s)], w=LW * .7)
    cv.stroke([(x - 38 * s, y + 140 * s), (x + 38 * s, y + 140 * s)], w=LW * .7)
    if logo and s >= .95:
        cv.logo((x + 8 * s, y + 105 * s), scale=0.13 * s)


def bar(cv, top=455, x0=-90, x1=640, logo=True, bottom=640):
    cv.clear([(x0 - 20, top - 6), (x1 + 20, top - 6), (x1 + 20, bottom + 40), (x0 - 20, bottom + 40)])
    cv.stroke([(x0, top), (x0 + 200, top - 3), (x0 + 420, top + 2), (x1, top - 2)], jit=1.4)
    cv.stroke([(x0 + 10, top + 26), (x0 + 260, top + 28), (x0 + 520, top + 24), (x1 - 10, top + 27)], jit=1.4)
    cv.stroke([(x0, top), (x0 + 10, top + 26)], jit=.6)
    cv.stroke([(x1, top - 2), (x1 - 10, top + 27)], jit=.6)
    for xx in (x0 + 10, x1 - 10):
        cv.stroke([(xx, top + 28), (xx + (2 if xx < 0 else -2), bottom)], jit=1)
    if logo:
        cv.logo(((x0 + x1) / 2, top + 100), scale=0.36)


def machine(cv, x, top, w=170, bar_top=455):
    """Cafetera espresso sobre la barra; x = borde izquierdo."""
    cv.stroke([(x, bar_top), (x - 4, top + 20), (x + 10, top), (x + w - 10, top), (x + w + 4, top + 20), (x + w, bar_top)], closed=True, clear=True)
    cv.stroke([(x + 20, top + 30), (x + w - 20, top + 30)], w=LW * .7)
    cv.stroke([(x + w - 40, top + 50), (x + w - 52, top + 64), (x + w - 40, top + 78), (x + w - 28, top + 64)], closed=True, w=LW * .7)
    gx = x + 60
    cv.stroke([(gx - 26, top + 60), (gx - 22, top + 92), (gx + 22, top + 92), (gx + 26, top + 60)], closed=True, clear=True, w=LW * .9)
    cv.stroke([(x + 14, bar_top - 22), (x + w - 14, bar_top - 22)], w=LW * .7)
    return gx, top + 92


def kettle(cv, hx, hy):
    """Pava cuello de cisne; la mano la agarra en (hx,hy)."""
    x = hx + 40
    cv.stroke([(x, hy - 30), (x - 6, hy + 20), (x + 8, hy + 56), (x + 92, hy + 58), (x + 106, hy + 20), (x + 100, hy - 30)], closed=True, clear=True)
    cv.stroke([(x - 10, hy - 34), (x + 50, hy - 50), (x + 110, hy - 34)], jit=1)
    cv.stroke([(x + 36, hy - 50), (x + 50, hy - 70), (x + 66, hy - 50)], jit=.8)
    cv.stroke([(x + 102, hy + 38), (x + 136, hy + 30), (x + 154, hy - 4), (x + 176, hy - 36), (x + 200, hy - 44)], jit=1)
    return (x + 204, hy - 36)


def pitcher(cv, x, y, ang=-30):
    pts = rot([(x - 30, y - 50), (x - 26, y + 40), (x + 30, y + 40), (x + 38, y - 50), (x + 52, y - 62)], ang, (x, y))
    cv.stroke(pts, closed=True, clear=True)
    cv.stroke(rot([(x + 30, y - 30), (x + 56, y - 20), (x + 54, y + 14), (x + 30, y + 20)], ang, (x, y)))
    return rot([(x + 52, y - 62)], ang, (x, y))[0]


def zzz(cv, x, y, s=1.0):
    for i, (dx, dy, k) in enumerate(((0, 0, .7), (34, -38, 1.0))):
        k *= s
        cv.stroke([(x + dx, y + dy), (x + dx + 26 * k, y + dy), (x + dx, y + dy + 26 * k), (x + dx + 26 * k, y + dy + 26 * k)], w=LW * .7, jit=.5)


def sparkle(cv, x, y, s=1.0):
    cv.ink([(x, y - 18 * s), (x + 4 * s, y - 4 * s), (x + 18 * s, y), (x + 4 * s, y + 4 * s), (x, y + 18 * s), (x - 4 * s, y + 4 * s), (x - 18 * s, y), (x - 4 * s, y - 4 * s)], smooth=False)


def heart(cv, x, y, s=1.0):
    cv.ink([(x, y + 16 * s), (x - 18 * s, y - 1 * s), (x - 15 * s, y - 13 * s), (x - 5 * s, y - 14 * s), (x, y - 6 * s), (x + 5 * s, y - 14 * s), (x + 15 * s, y - 13 * s), (x + 18 * s, y - 1 * s)])


def arm(cv, a1, a2, b1, b2):
    """Brazo como dos contornos (borde superior a1->a2 e inferior b1->b2)."""
    cv.stroke(a1 + a2, jit=1)
    cv.stroke(b1 + b2, jit=1)
