import covasim as cv
import pylab as pl
import numpy as np
import sciris as sc

cv.options.set(dpi=150)
sim = cv.Sim(pop_size=1e3, verbose=0).run()
colors = {k:res.color for k,res in sim.results.items() if isinstance(res, cv.Result)} # colors = cv.get_colors()
d = sc.objdict()
for key in ['cum', 'new', 'n', 'other']:
    d[key] = sc.objdict()

for k,v in colors.items():
    if k.startswith('cum_'):
        d.cum[k] = v
    elif k.startswith('n_'):
        d.n[k] = v
    elif k.startswith('new_'):
        d.new[k] = v
    else:
        d.other[k] = v


pl.figure(figsize=(24,18))

for i,k,colors in d.enumitems():
    pl.subplot(2,2,i+1)
    pl.title(k)
    n = len(colors)
    y = n-np.arange(n)
    # pl.axes([0.25,0.05,0.6,0.9])
    pl.barh(y, width=1, color=colors.values())
    pl.gca().set_yticks(y)
    pl.gca().set_yticklabels(colors.keys())

pl.show()