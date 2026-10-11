"""Generate original analytical SVG figures using only Python's standard library.
Illustrations are objective curves, not measured experiment results.
"""
from pathlib import Path
import math,html
OUT=Path(__file__).resolve().parent/'plots';OUT.mkdir(exist_ok=True)
def plot(name,title,xlabel,ylabel,xmin,xmax,ymin,ymax,curves,verticals=()):
 W,H=900,500;L,R,T,B=90,35,60,90;pw=W-L-R;ph=H-T-B
 X=lambda x:L+(x-xmin)/(xmax-xmin)*pw
 Y=lambda y:T+ph-(y-ymin)/(ymax-ymin)*ph
 parts=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img"><title>{html.escape(title)}</title><rect width="100%" height="100%" fill="white"/>',f'<text x="{W/2}" y="28" text-anchor="middle" font-family="sans-serif" font-size="20">{html.escape(title)}</text>']
 for i in range(6):
  x=xmin+(xmax-xmin)*i/5;y=ymin+(ymax-ymin)*i/5
  parts += [f'<path d="M {X(x)} {T} V {T+ph}" stroke="#eee"/>',f'<path d="M {L} {Y(y)} H {L+pw}" stroke="#eee"/>',f'<text x="{X(x)}" y="{T+ph+24}" text-anchor="middle" font-family="sans-serif">{x:g}</text>',f'<text x="{L-10}" y="{Y(y)+5}" text-anchor="end" font-family="sans-serif">{y:g}</text>']
 for x in verticals:parts.append(f'<path d="M {X(x)} {T} V {T+ph}" stroke="#777" stroke-dasharray="6 4"/>')
 for idx,(label,color,func) in enumerate(curves):
  points=' '.join(f'{X(x):.3f},{Y(func(x)):.3f}' for x in [xmin+(xmax-xmin)*i/400 for i in range(401)])
  parts += [f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="3"/>',f'<text x="{L+15}" y="{T+24+idx*23}" fill="{color}" font-family="sans-serif">{html.escape(label)}</text>']
 parts += [f'<path d="M {L} {T} V {T+ph} H {L+pw}" fill="none" stroke="black"/>',f'<text x="{W/2}" y="{H-27}" text-anchor="middle" font-family="sans-serif">{html.escape(xlabel)}</text>',f'<text transform="translate(23 {H/2}) rotate(-90)" text-anchor="middle" font-family="sans-serif">{html.escape(ylabel)}</text>','</svg>']
 (OUT/name).write_text('\n'.join(parts))
def main():
 clip=lambda r:max(.8,min(1.2,r))
 plot('ppo_clipping.svg','PPO surrogate: fixed advantages; epsilon = 0.2','Current / old probability ratio','Surrogate value (maximize)',0,2,-2,2,[('A = +1','#0077bb',lambda r:min(r,clip(r))),('A = -1','#cc3311',lambda r:min(-r,-clip(r)))],(.8,1,1.2))
 curves=[]
 for beta,color in [(.1,'#0077bb'),(.5,'#cc3311'),(1,'#228833')]:
  curves.append((f'beta = {beta}',color,lambda m,b=beta:math.log1p(math.exp(-b*m))))
 plot('preference_loss.svg','Logistic preference loss: illustrative reference-adjusted margins','Margin m before beta scaling','-log sigmoid(beta * m)',-5,5,0,6,curves,(0,))
 print('Generated two analytical SVG plots; no experimental data used.')
if __name__=='__main__':main()
