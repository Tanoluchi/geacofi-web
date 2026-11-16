import cairosvg, io, sys, os
from PIL import Image, ImageDraw
from poses2 import POSES, EXPR, Canvas
os.makedirs('v2', exist_ok=True)
only = sys.argv[1:] 
items=[]
for k,(f,cat,t,u) in POSES.items():
    if only and k not in only: continue
    svg=f().svg(); open(f'v2/{cat}_{k}.svg','w').write(svg); items.append((k,svg))
for k,(f,t,n) in EXPR.items():
    if only and ('x_'+k) not in only and 'expr' not in only: continue
    cv=Canvas(seed=3); f(cv); svg=cv.svg(); open(f'v2/expr_{k}.svg','w').write(svg); items.append(('x_'+k,svg))
cell=300; cols=6; rows=(len(items)+cols-1)//cols
S_=Image.new('RGB',(cols*cell,rows*(cell+22)),'#FBE6C8'); d=ImageDraw.Draw(S_)
for i,(k,svg) in enumerate(items):
    im=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=cell*2))); im.thumbnail((cell,cell))
    x,y=(i%cols)*cell,(i//cols)*(cell+22); S_.paste(im,(x,y),im); d.text((x+4,y+cell+4),k,fill='black')
S_.save('sheet2.png'); print(len(items))
