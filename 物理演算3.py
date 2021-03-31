
from numpy import sin, cos
from scipy.integrate import solve_ivp
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import math

M1=10
M2=10
M3=20
K1=50
K2=50
K3=500
L=5

def derivs(t,x):
    dxdt=np.zeros_like(x)
    dxdt[0]=x[1]
    dxdt[1]=-1*(K1+K2)/M1*(x[0]-L)+K2/M1*(x[2]-2*L)
    dxdt[2]=x[3]
    dxdt[3]=K2/M2*(x[0]-L)-(K2+K3)/M2*(x[2]-2*L)+K3/M2*(x[4]-3*L)
    dxdt[4]=x[5]
    dxdt[5]=K3/M3*(x[2]-2*L)-1*K3/M3*(x[4]-3*L)
    return dxdt

t_span=[0,60]
dt=0.05
t=np.arange(t_span[0],t_span[1],dt)
x10=L
dx1dt0=0
x20=2*L
dx2dt0=0
x30=2*L
dx3dt0=0
x=[x10,dx1dt0,x20,dx2dt0,x30,dx3dt0]

sol=solve_ivp(derivs,t_span,x,t_eval=t)
x1=sol.y[0,:]
x2=sol.y[2,:]
x3=sol.y[4,:]

print(np.shape(sol.y))

y=t

fig,ax=plt.subplots()
#ax=fig.add_subplot(111)
line,=ax.plot([],[],"o-",linewidth=2)
line2,=ax.plot([],[],"o-",linewidth=2)
line3,=ax.plot([],[],"o-",linewidth=2)
locus,=ax.plot([],[],"r-",color="blue",linewidth=1)
locus2,=ax.plot([],[],"r-",color="red",linewidth=1)
locus3,=ax.plot([],[],"r-",color="black",linewidth=1)

x1locus=[]
x2locus=[]
x3locus=[]
tlocus=[]
def animate(i):
    #thisx1=[0,x1[i]]
    #thisx2=[0,x2[i]]
    #line.set_data([0,thisx1,thisx2],[0,0,0])
    line.set_data([0,x1[i]],[t[i],t[i]])
    line2.set_data([x1[i],x2[i]],[t[i],t[i]])
    line3.set_data([x2[i],x3[i]],[t[i],t[i]])
    #line.set_data(thisx1,0)

    x1locus.append(x1[i])
    x2locus.append(x2[i])
    x3locus.append(x3[i])
    tlocus.append(t[i])
    locus.set_data(x1locus,tlocus)
    locus2.set_data(x2locus,tlocus)
    locus3.set_data(x3locus,tlocus)
    return line,line2,line3,locus,locus2,locus3

ani = FuncAnimation(fig, animate, frames=np.arange(0, len(t)), interval=25, blit=True)
ax.set_xlim(-0.5*L,6*L)
ax.set_ylim(-0.5*L,12*L)
ax.set_aspect('equal')
ax.grid()
plt.show()