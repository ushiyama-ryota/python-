import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import math

class Ball():
    max_x=5
    min_x=-5
    max_y=5
    min_y=-5

    def __init__(self,init_x,init_y,v_x,v_y,ball_size,e,dt):
        self.x=init_x
        self.y=init_y
        self.v_x=v_x
        self.v_y=v_y
        self.size=ball_size
        self.e=e
        self.dt=dt

    def state_update(self):
        self.x+=self.v_x*self.dt
        self.y+=self.v_y*self.dt

        if self.x>self.max_x:
            self.x=self.max_x
            self.velocity_x_update()
        elif self.x<self.min_x:
            self.x=self.min_x
            self.velocity_x_update()

        if self.y>self.max_y:
            self.y=self.max_y
            self.velocity_y_update()
        elif self.y<self.min_y:
            self.y=self.min_y
            self.velocity_y_update()

        return self.x,self.y

    def velocity_x_update(self):
        self.v_x=-self.e*self.v_x
    def velocity_y_update(self):
        self.v_y=-self.e*self.v_y

class Drawing():
    def __init__(self,ax):
        self.color=[]
        self.ax=ax
        self.ball_img=ax.plot([],[],color="b")
    def draw_circle(self,center_x,center_y,circle_size=0.01):
        self.circle_x=[]
        self.circle_y=[]
        steps=100

        for i in range(steps):
            self.circle_x.append(center_x+circle_size*math.cos(i*2*math.pi/steps))
            self.circle_y.append(center_y+circle_size*math.sin(i*2*math.pi/steps))

        self.ball_img.set_data(self.circle_x,self.circle_y)
        return self.ball_img

def update_anim(i):
    ball_x,ball_y=ball.state_update()
    ball_img=drawer.draw_circle(ball_x,ball_y)
    return ball_img

fig=plt.figure()

ax=fig.add_subplot(111)

max_x=5
min_x=-5
max_y=5
min_y=-5

ax.set_xlim(min_x,max_x)
ax.set_ylim(min_y,max_y)

ax.set_aspect("equal")

ax.set_xlabel("X[m]")
ax.set_ylabel("Y[m]")

ax.grid(True)
ax.legend()

step_text=ax.text(0.05,0.9,"",transform=ax.transAxes)
ball_img=ax.plot([],[],label="Predicit",color="b")

#    def __init__(self,init_x,init_y,v_x,v_y,ball_size,e,dt):
ball=Ball(0,0,2,3,0.2,1,0.05)
drawer=Drawing(ax)

animation=ani.FuncAnimation(fig,update_anim,interval=1,frames=1000)

plt.show()




