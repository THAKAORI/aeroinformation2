#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 09:52:40 2018

@author: 1194751660
"""

from numpy import sin, cos, pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from scipy.integrate import odeint

def ode(f, t):
    theta1, dtheta1, theta2, dtheta2 = f
    dtheta1dt = (M2 * G * sin(theta2) * cos(theta2 - theta1)
            + M2 * L1 * (dtheta1 ** 2) * sin(theta2 - theta1) * cos(theta2 - theta1)
            + M2 * L2 * (dtheta2 ** 2) * sin(theta2 - theta1)
            - (M1 + M2) * G * sin(theta1)) / (M1 * L1 + M2 * L1 * (sin(theta2 - theta1) ** 2))
    dtheta2dt = (-(M1 + M2) * L1 * (dtheta1 ** 2) * sin(theta2 - theta1)
            - (M1 + M2) * G * sin(theta2)
            - M2 * L2 * (dtheta2 ** 2) * sin(theta2 - theta1) * cos(theta2 - theta1)
            + (M1 + M2) * G * sin(theta1) * cos(theta2 - theta1)) / (M1 * L2 + M2 * L2 * (sin(theta2 - theta1) ** 2))
    return [dtheta1, dtheta1dt, dtheta2, dtheta2dt]

G  = 9.8            # [m/s^2]  gravitational acceleration
THETA1_0 =  0.1      # [radian] initial theta
THETA2_0 =  0.1   # [radian] initial theta
V1_0 = 0            # [m/s]    initial velocity
V2_0 = 0            # [m/s]    initial velocity
L1 =  1             # [m]      length of pendulum
L2 =  1             # [m]      length of pendulum
M1 =  1             # [kg]     mass
M2 =  1             # [kg]     mass
DURATION = 10       # [s]      duration time
INTERVAL = 0.05     # [s]      interval time

f_0 = [THETA1_0, V1_0/L1, THETA2_0, V2_0/L2]
t = np.arange(0, DURATION + INTERVAL, INTERVAL)

sol = odeint(ode, f_0, t)
theta1, theta2 = sol[:, 0], sol[:, 2]

x1 = L1 * sin(theta1)
y1 = - L1 * cos(theta1)
x2 = x1 + L2 * sin(theta2)
y2 = y1 - L2 * cos(theta2)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim = [-L1 - L2, L1 + L2], ylim = [-L1 - L2, L1 + L2])
ax.grid()

line, = plt.plot([], [], 'ro-', animated = True)

time_template = 'time = %.1fs'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def init():
    time_text.set_text('')
    return line, time_text

def update(i):
    next_x = [0, x1[i], x2[i]]
    next_y = [0, y1[i], y2[i]]
    line.set_data(next_x, next_y)

    time_text.set_text(time_template % (i * INTERVAL))
    return line, time_text

FRAME_INTERVAL = 1000 * INTERVAL # [msec] interval time between frames
FPS = 1000/FRAME_INTERVAL        # frames per second
ani = FuncAnimation(fig, update, frames=np.arange(0, len(t)),
                    interval=FRAME_INTERVAL, init_func=init, blit=True)

plt.show()
ani.save('double_pendulum.mp4', fps=FPS, extra_args=['-vcodec', 'libx264'])
ani.save('double_pendulum.gif', writer='imagemagick', fps=FPS)