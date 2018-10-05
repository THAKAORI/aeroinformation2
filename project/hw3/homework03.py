#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 08:52:40 2018

@author: 1194751660
"""
import matplotlib.pyplot as plt

def euler(gamma,omega2,delta_t,max_time):
    x=[]
    x.append(1.0)
    delta_x=[]
    delta_x.append(1.0)
    t=0
    delta2_x=[]
    m_t=int(max_time/delta_t)
    
    while t<m_t:
        delta2_x.append((-2.0)*gamma*delta_x[t]-omega2*x[t])
        x.append(delta_x[t]*delta_t+x[t])
        delta_x.append(delta2_x[t]*delta_t+delta_x[t])
        t+=1
    return x

def plot(x,delta_t,max_time): 
    m_t=max_time/delta_t
    r_time=[]
    f_time=[]
    for i in range(5):
        r_time.append(max_time/4*i)
        f_time.append(m_t/4*i)
        i+=1
        
    plt.plot(x)
    plt.xticks(f_time,r_time)
    plt.show()
    
def opt_dumper(omega2,delta_t,max_time):
    gamma=0.0
    delta_gamma=0.01
    while pm_search(euler(gamma,omega2,delta_t,max_time)):
        gamma+=delta_gamma
    print('gamma=',gamma)
    return euler(gamma,omega2,delta_t,max_time)
    
def pm_search(x):
    for i in range(len(x)):
        if x[i]<0:
            return True
        i+=1
    return  False   

def print_imf(gamma,omega2,delta_t,max_time):
    print('gamma=',gamma)
    print('omega^2=',omega2)
    print('accuracy of time=',delta_t)
    print('maximum time(s)=',max_time)
    
"""自由に打ち込めるようにする
gamma=input('gamma=')
omega2=input('omega^2=')
delta_t=input('accuracy of time(default 0.1)=')
max_time=input('maximum time(s)=')
"""
gamma=0.3 #ガンマの項
omega2=1.0 #オメガ二乗の項
delta_t=0.001 #オイラー法の精度少なければ高い
max_time=30 #最大の時間

#オイラー法で問題の条件でグラフを書く
print_imf(gamma,omega2,delta_t,max_time) 
x=euler(gamma,omega2,delta_t,max_time)
plot(x,delta_t,max_time)

#臨界減衰するようなガンマを発見する
y=opt_dumper(omega2,delta_t,max_time)
plot(y,delta_t,max_time)