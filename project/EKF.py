#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 21:05:20 2018

@author: takahiro
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('poster')
from pylab import rcParams

rcParams['figure.figsize'] = 10,7
def random_walker(start_position=0, mean=0, deviation=1, n_steps=99, seed=None):

    if seed is not None:
        np.random.seed(seed=seed)

    move = np.random.normal(loc=mean, scale=deviation, size=n_steps)
    position = np.insert(move, 0, start_position)
    position = np.cumsum(position)

    return position



def add_noise(position, mean=0, deviation=10, seed=None):

    if seed is not None:
        np.random.seed(seed=seed)

    n_observation = len(position)
    noise = np.random.normal(loc=mean, scale=deviation, size=n_observation)
    observation = position + noise

    return observation
class EKF:
    def __init__(self, position1, position2):
        self.z = np.matrix([position1, position2])
        self.length = position1.size 
        self.x = np.zeros(self.length)
        self.A = np.matrix([1])
        self.C = np.matrix([1,1])
        self.G = np.zeros((self.length, 2))
        self.P = np.zeros(self.length)
        self.Q = np.matrix([0.01]) #the covariance of the process noise
        self.R = np.matrix([[0.64, 0], [0, 0.64]]) #the covariance of each value
        self.kalman()
    def prediction(self, i):
        self.x[i] = self.A * self.x[i-1]
        self.P[i] = self.A * self.P[i-1] * self.A.T + self.Q
    def update(self, i):
        self.G[i] = self.P[i] * self.C * np.linalg.inv(self.C.T * self.P[i] * self.C + self.R)    
        self.x[i] = self.x[i] + self.G[i] * ((np.matrix([self.z[0, i], self.z[1, i]])).T - self.C.T * self.x[i])
        self.P[i] = (np.identity(1) - self.G[i] * self.C.T) * self.P[i]
    def kalman(self):
        for i in range(1, self.length):
            self.prediction(i)
            self.update(i)
class MoveAverage:
    def __init__(self, position1, position2):
        self.z = np.array([position1, position2])
        self.length = position1.size 
        self.x = np.zeros(self.length)  
        stacksize = 5 #the length of move average stack
        self.stack1 = np.zeros(stacksize)
        self.stack2 = np.zeros(stacksize)
        self.result()
    def moveaverage(self, i):
        self.stack1 = np.delete(self.stack1, 0)
        self.stack1 = np.append(self.stack1, self.z[0, i])    
        self.stack2 = np.delete(self.stack2, 0)
        self.stack2 = np.append(self.stack2, self.z[1, i])
        self.x[i] = (np.mean(self.stack1) + np.mean(self.stack2)) / 2
    def result(self):
        for i in range(self.length):
            self.moveaverage(i)
        
    
true_position = random_walker(start_position=0, mean=0, deviation=1, n_steps=299, seed=0)
observed_position1 = add_noise(true_position, mean=0, deviation=10, seed=0)
observed_position2 = add_noise(true_position, mean=0, deviation=5, seed=10)
expectedEKF = EKF(observed_position1, observed_position2)
expectedMoveaverage = MoveAverage(observed_position1, observed_position2)
plt.plot(true_position, 'r--', label='True Positions',linewidth=3)
plt.plot(observed_position1, 'y', label='Observed 1st sensor',linewidth=0.5)
plt.plot(observed_position2, 'b', label='Observed 2nd sensor',linewidth=0.5)
plt.plot(expectedEKF.x, 'k', label='Expected by EKF',linewidth=2)
plt.plot(expectedMoveaverage.x, 'g', label='Expected by MoveAve',linewidth=2)
plt.title('Random Walk')
plt.xlabel('time step')
plt.ylabel('position')
plt.legend(loc='best',fontsize=10)
plt.savefig("EKF", dpi=300)
