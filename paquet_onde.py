import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from matplotlib.widgets import RadioButtons, Slider

limx = 75
limy = 20

p = 10000
limr = 100

Vg = 1.0
k0 = 1
Vp = Vg
a = 0

X = np.linspace(0, limr, p)
k = np.fft.fftfreq(len(X), limr/p)
A = np.exp(-100*(k-k0)**2)

def omega(Vp, a):

    return Vp*k0 + Vg*(k-k0) + a*(k-k0)**2
    

def f0(A):

    f0 = np.fft.fft(A)
    A0 = np.fft.ifft(f0)

    return np.real(f0)

def propagation(t):

    Ap = np.real(A)*np.exp(1j*omega(Vp, a)*t)
    fp = np.fft.fft(Ap)

    return np.real(fp)


def update(t):

    onde.set_data(X, propagation(t))

    return onde,
    

def init():
    
    onde.set_data(X, f0(A))
    
    return onde,

def choix_variables(val):

    global Vp
    global a

    Vp = sVp.val
    a = sa.val
    

fig=plt.figure()
onde,=plt.plot([],[])
plt.subplots_adjust(left=0.4)
plt.xlim(left=0, right=limx)
plt.ylim(bottom=-limy, top=limy)

axcolor = 'white'

plt.title("Propagation d'un paquet d'onde Gaussien")

axVp = plt.axes([0.03, 0.7, 0.3, 0.03], facecolor=axcolor)
axa = plt.axes([0.03, 0.6, 0.3, 0.03], facecolor=axcolor)
sVp = Slider(axVp, 'Vp', 0, 2.0*Vg, valinit=Vg, valstep=0.01)
sa = Slider(axa, 'a', -2.0*Vg, 2.0*Vg, valinit=0, valstep=0.01)

sVp.on_changed(choix_variables)
sa.on_changed(choix_variables)

anim = anim.FuncAnimation(fig, update, init_func=init, frames=500, interval=5, blit=True)

plt.show()