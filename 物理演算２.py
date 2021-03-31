import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from scipy.integrate import solve_ivp

G=9.8
L=1.0
def derivs(t,state):
    dydt=np.zeros_like(state)#連立微分方程式の定型文
    dydt[0]=state[1]
    dydt[1]=-1*G/L*math.sin(state[0])
    return dydt

t_span=[0,20]#測定時間
dt=0.05
t=np.arange(t_span[0],t_span[1],dt)#arrange(1,5)→[1,2,3,4,5]
th1=90.0#[deg/s]
w1=0.0#[deg/s]
state=np.radians([th1,w1])#radians　度→ラジアン

sol=solve_ivp(derivs,t_span,state,t_eval=t)
theta=sol.y[0,:]

print(np.shape(sol.y))

x=L*np.sin(theta)#配列の時はnumpyを用いる
y=-L*np.cos(theta)

#fig,ax=plt.subplots()
fig=plt.figure()
ax=fig.add_subplot(111)

line,=ax.plot([],[],"o-",linewidth=2)

def animate(i):
    thisx = [0, x[i]]
    thisy = [0, y[i]]

    line.set_data(thisx, thisy)
    return line,

ani = FuncAnimation(fig, animate, frames=np.arange(0, len(t)), interval=25, blit=True)
#animation=ani.FuncAnimation(fig,animate,frame=ni.atange(0,len(t)),interval=25,blit=True)
ax.set_xlim(-L,L)
ax.set_ylim(-L,L)
ax.set_aspect('equal')
ax.grid()
plt.show()