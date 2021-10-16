import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

path = '/usr/share/matplotlib/mpl-data/fonts/ttf/NanumBarunGothic.ttf'
fontprop = fm.FontProperties(fname=path, size=10)
fontpropTitle = fm.FontProperties(fname=path, size=15)

# print([(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name])

def calcPresentValue(FV,r,t):
    DF = 1/pow(1+r,t)
    return FV*DF

x = np.arange(0,21,1)
plt.plot(x,calcPresentValue(100,0.0,x),label='r=0%')
plt.plot(x,calcPresentValue(100,0.05,x),label='r=5%')
plt.plot(x,calcPresentValue(100,0.1,x),label='r=10%')
plt.plot(x,calcPresentValue(100,0.15,x),label='r=15%')
plt.xticks(x)
plt.xlabel("해(년)",FontProperties=fontprop)
plt.ylabel("100만원의 현재가치",FontProperties=fontprop)
plt.title("미래 100만원에 대한 현재가치",FontProperties=fontpropTitle)
plt.xlim(0,21)
plt.ylim(0,105)
plt.legend()
plt.show()