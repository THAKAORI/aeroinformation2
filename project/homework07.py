#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 16:38:56 2018

@author: 1194751660
"""
"""
カオスを実現するためには、初期条件を大きくすれば良い
線形に近似するためには、初期条件を小さくして微小振動をおこせばよい
力学的エネルギーが一定にならないのは、ルンゲクッタ法の誤差と運動エネルギーを求めるときに
下の剛体振り子に近似を行ったためと考えられる
thetaとfaiと、運動エネルギーと位置エネルギーと力学的エネルギーのグラフが生成されます。
"""
import numpy as np
import pylab as py
from numpy import sin, cos ,pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class Dif_eq():
    def __init__(self, theta, fai, dtheta, dfai):
        self.m = 1.0
        self.l = 1.0
        self.g = 9.8
        self.dt = 0.1
        self.T = np.arange(0.0, 30.0, self.dt)
        self.N = self.T.shape[0]
        self.X = np.zeros((self.N, 4))
        self.X[0,:] = [theta,fai,dtheta,dfai]
        self._runge()
        self._energy()
        self._plot()
    def _plot(self):
        py.subplot(211)
        py.plot(self.T, self.X[:,0],'r-',label="theta")
        py.plot(self.T, self.X[:,1],'b-',label="fai")
        py.legend(loc = 'upper left')
        
        py.subplot(212)
        py.plot(self.T, self.K[:],'r-',label="kinetic")
        py.plot(self.T, self.U[:],'b-',label="potential")
        py.plot(self.T, self.E[:],'g-',label="overall")
        py.legend(loc = 'upper left')
        py.suptitle('double_pendulum test')
        py.savefig('double_pendulum.png')
        py.show()
    def _runge(self):
        k1 = np.array(np.zeros(4))
        k2 = np.array(np.zeros(4))
        k3 = np.array(np.zeros(4))
        k4 = np.array(np.zeros(4))
        for i in range(self.N - 1):
            k1 = self._deriv(self.X[i,:])
            k2 = self._deriv(self.X[i,:] + 0.5 * self.dt * k1)
            k3 = self._deriv(self.X[i,:] + 0.5 * self.dt * k2)
            k4 = self._deriv(self.X[i,:] + self.dt * k3)
            self.X[i+1,:] = self.X[i,:] + self.dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    def _deriv(self, X):
        temp = np.array(np.zeros(4))
        A = np.array([[16/3,2 * cos(X[0] - X[1])],[2 * cos(X[0] - X[1]),4/3]])
        right = np.array([(-3 * self.g * sin(X[0]) / self.l) - (2 * sin(X[0] - X[1]) * (X[3]**2)),(-1 * self.g * sin(X[1]) / self.l) + (2 * sin(X[0] - X[1]) * (X[2]**2))])
        temp[0] = X[2]
        temp[1] = X[3]
        temp[2] = np.dot(right, np.linalg.inv(A))[0]
        temp[3] = np.dot(right, np.linalg.inv(A))[1]
        return temp
    def _energy(self):
        self.U = self.l * (1 - cos(self.X[:,0])) * self.g * self.m + 3 * self.l * (1 - cos(self.X[:,0])) * self.g * self.m + self.l * (1 - cos(self.X[:,1])) * self.g * self.m 
        K1 = ((self.l * self.X[:,2])**2) * self.m / 2
        vx2 = self.l * self.X[:,3] * cos(self.X[:,1])
        vy2 = self.l * self.X[:,3] * sin(self.X[:,1])
        x = 2 * self.l * sin(self.X[:,0]) + self.l * sin(self.X[:,1])
        y = -2 * self.l * cos(self.X[:,0]) - self.l * cos(self.X[:,1])
        vx1 = self.X[:,2] * (-y)
        vy1 = self.X[:,2] * x
        K2 = (((vx1 + vx2)**2) + ((vy1 + vy2)**2)) * self.m / 2
        self.K = K1 + K2
        self.E = self.K + self.U

"""
theta = float(input("theta"))
fai = float(input("fai"))
dtheta = float(input("dtheta"))
dfai = float(input("dfaii"))
"""
# If you delete comment out above,you can chage parameter on IPython.
theta = pi / 2
fai = pi / 2 + 0.1
dtheta = 0
dfai = 0
result = Dif_eq(theta,fai,dtheta,dfai)

x1 = 2 * result.l * sin(result.X[:,0])
y1 = -2 * result.l * cos(result.X[:,0])
x2 = x1 + 2 * result.l * sin(result.X[:,1])
y2 = y1 -2 * result.l * cos(result.X[:,1])

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False, xlim = [-4 * result.l, 4 * result.l], ylim = [-4 * result.l, 4 * result.l])
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

    time_text.set_text(time_template % (i * result.dt))
    return line, time_text

FRAME_INTERVAL = 1000 * result.dt # [msec] interval time between frames
FPS = 1000/FRAME_INTERVAL        # frames per second
ani = FuncAnimation(fig, update, frames=np.arange(0, len(result.T)),
                    interval=FRAME_INTERVAL, init_func=init, blit=True)

plt.show()

ani.save('double_pendulum.gif', writer='imagemagick', fps=FPS)
