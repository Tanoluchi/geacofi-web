import numpy as np, potrace
from PIL import Image
def to_mask(img, thr=150):
    a=np.asarray(img.convert('L')).astype(float)
    return a<thr
def trace_svg(mask, color='#14171B', vb=None, scale=1.0):
    bmp=potrace.Bitmap(mask)
    path=bmp.trace(turdsize=6, alphamax=1.1, opticurve=True, opttolerance=0.3)
    parts=[]
    for curve in path:
        sp=curve.start_point; d=f"M{sp.x*scale:.1f},{sp.y*scale:.1f}"
        for seg in curve.segments:
            if seg.is_corner:
                d+=f" L{seg.c.x*scale:.1f},{seg.c.y*scale:.1f} L{seg.end_point.x*scale:.1f},{seg.end_point.y*scale:.1f}"
            else:
                d+=f" C{seg.c1.x*scale:.1f},{seg.c1.y*scale:.1f} {seg.c2.x*scale:.1f},{seg.c2.y*scale:.1f} {seg.end_point.x*scale:.1f},{seg.end_point.y*scale:.1f}"
        parts.append(d+"Z")
    h,w=mask.shape
    vb=vb or f"0 0 {w*scale:.0f} {h*scale:.0f}"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"><path d="{" ".join(parts)}" fill="{color}" fill-rule="evenodd"/></svg>'
