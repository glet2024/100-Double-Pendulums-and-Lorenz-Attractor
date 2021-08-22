import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

x, y, z = 0, 1, 10  #setting the initial state of the system

rho, sigma, beta = 28, 10, 8 / 3  #the three parameters Lorenz's model utilizes

t0 = 0  #starting time
tf = 100  #ending time
dt = 0.008  #change in time step
t = np.arange(t0, tf + dt, dt)  #this variable represents temporal changes
n = len(t)


def ODEs(t, r):  #returns an array of the Lorenz equations
    x, y, z = r
    return np.array([sigma * (y - x),  #dx/dt derivative of x with respect to time
                     rho * x - y - x * z,  #dy/dt derivative of y with respect to time
                     x * y - beta * z])  #dz/dt derivative of z with respect to time


def RK4(t, r, f, dt):  #this defines the 4th order Runge-Kutta method
    k1 = dt * f(t, r)
    k2 = dt * f(t + dt / 2, r + k1 / 2)
    k3 = dt * f(t + dt / 2, r + k2 / 2)
    k4 = dt * f(t + dt, r + k3)
    return r + (k1 + 2 * k2 + 2 * k3 + k4) / 6


r = [x, y, z]  #initial state vector for our animation

evol = np.zeros((n, 3))  #represents the evolution of the Lorenz equations/ODEs
evol[0, 0], evol[0, 1], evol[0, 2] = r[0], r[1], r[2]

for i in range(n - 1):
    evol[i + 1] = RK4(t[i], [evol[i, 0], evol[i, 1], evol[i, 2]], ODEs, dt)

fig = plt.figure('Lorenz Attractor', facecolor='k', figsize=(10, 9))
fig.tight_layout()
ax = fig.gca(projection='3d')

def animate(i):  #creating animation
    ax.view_init(-6, -56 + i / 2)
    ax.clear()
    ax.set(facecolor='k')
    ax.set_axis_off()
    #ax.view_init(elev=10, azim=i) #a different way to auto-spin the animation view
    ax.plot(evol[:i, 0], evol[:i, 1], evol[:i, 2], color='white', lw=0.9)

anim = animation.FuncAnimation(fig, animate, np.arange(3000), interval=2, repeat=False)

'''
here is the option to save the simulation as a gif
'''
#f = r"c:\\Users\FILE_LOCATION\LorenzAttractor.gif"
#writergif = animation.PillowWriter(fps=30)
#anim.save(f, writer=writergif)

plt.show()