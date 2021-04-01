from numpy import sin, cos
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import math

M1=50
M2=1000
K1=50
K2=40
C2=20
#p1=math.sqrt(K1/M1)
#p2=math.sqrt(K2/M2)
#myu=p2/p1
#動吸振器に最適なK2,C2を求める
#ita=M2/M1
#K2=((1/(1+ita))*math.sqrt(K1/M1))**2*M2
#C2=math.sqrt(3*K2*M2*ita/2/(1+ita))
L=5
F=10
w=math.sqrt(K1/M1)

def derivs(t,x):
    dxdt=np.zeros_like(x)
    dxdt[0]=x[1]
    dxdt[1]=-1*(K1+K2)/M1*(x[0]-L)+K2/M1*(x[2]-2*L)-C2/M1*(x[1]-x[3])+F/M1*math.cos(w*t)
    dxdt[2]=x[3]
    dxdt[3]=K2/M2*(x[0]-L)-K2/M2*(x[2]-2*L)+C2/M2*(x[1]-x[3])
    return dxdt

t_span=[0,120]
dt=0.5
t=np.arange(t_span[0],t_span[1],dt)
x10=L
dx1dt0=0
x20=2*L
dx2dt0=0
x=[x10,dx1dt0,x20,dx2dt0]

sol=solve_ivp(derivs,t_span,x,t_eval=t)
x1=sol.y[0,:]
x2=sol.y[2,:]

print(np.shape(sol.y))

fig,ax=plt.subplots()
#ax=fig.add_subplot(111)
line,=ax.plot([],[],"o-",linewidth=2)
line2,=ax.plot([],[],"o-",linewidth=2)
locus,=ax.plot([],[],"r-",color="blue",linewidth=1)
locus2,=ax.plot([],[],"r-",color="red",linewidth=1)

x1locus=[]
x2locus=[]
tlocus=[]
def animate(i):
    line.set_data([0,x1[i]],[t[i],t[i]])
    line2.set_data([x1[i],x2[i]],[t[i],t[i]])

    x1locus.append(x1[i])
    x2locus.append(x2[i])
    tlocus.append(t[i])
    locus.set_data(x1locus,tlocus)
    locus2.set_data(x2locus,tlocus)
    return line,line2,locus,locus2

ani = FuncAnimation(fig, animate, frames=np.arange(0, len(t)), interval=25, blit=True)
ax.set_xlim(-4*L,6*L)
ax.set_ylim(-0.5*L,24*L)
ax.set_aspect('equal')
ax.grid()
plt.show()
