"""Plot exact finite qubit probabilities; no asymptotic data is used."""
from pathlib import Path
from math import comb
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def offline(m):
 return F(1,2**(m-1))*sum((F((m-2*j+1)*(comb(m,j)-(comb(m,j-1) if j else 0)),(m-j+1)*(j+1)) for j in range(m//2+1)),F(0))
def free(m):
 n=m+1;r=m//2;B=[1]
 for j in range(1,r+1):B.append(B[-1]*(n-2*j+2))
 return F(1,2**(m-1))*sum(((F(1,B[l])-(F(1,B[l+1]) if l<r else 0))*sum((F((m-2*j+1)*B[j]) for j in range(l+1)),F(0))/((m-l+1)*(l+1)) for l in range(r+1)),F(0))

root=Path(__file__).resolve().parent
ms=list(range(2,41));s=[offline(m) for m in ms];f=[free(m) for m in ms];b=[F(1,2**(m-1)) for m in ms]
assert all(0<z<=y<=x<=1 for x,y,z in zip(s,f,b))
rows=[{'prefix_m':m,'standalone':str(x),'free':str(y),'blind':str(z)} for m,x,y,z in zip(ms,s,f,b)]
(root/'frontier_values.json').write_text(json.dumps(rows,indent=2)+'\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(10.4,4.7),layout='constrained');fig.set_facecolor('#ffffff');ax.set_facecolor('#ffffff')
ax.semilogy(ms,[float(x) for x in s],color='#233843',lw=2.6,label='Best standalone prefix clustering')
ax.semilogy(ms,[float(x) for x in f],color='#00646c',lw=2.7,label='Best early clustering preserving the next optimum')
ax.semilogy(ms,[float(x) for x in b],color='#a87544',lw=1.8,ls='--',label='Blind prefix guess')
ax.set_xlabel('Prefix specimens m (one further specimen will arrive)');ax.set_ylabel('Complete-prefix success probability')
ax.set_title('Early accuracy under a later optimality requirement',loc='left',fontweight='bold',pad=14)
ax.grid(axis='y',alpha=.18);ax.spines[['top','right']].set_visible(False);ax.set_xlim(2,40)
ax.legend(loc='lower left',frameon=True,facecolor='white',edgecolor='#d6e0e2',fontsize=9)
fig.savefig(root/'frontier.svg')
fig.savefig('/workspace/scratch/252c84ff995c/game/frontier_preview.png',dpi=140)
print(json.dumps({'points':len(ms),'standalone_m2':str(s[0]),'free_m2':str(f[0]),'free_m4':str(f[2]),'inequalities_checked':True}))
