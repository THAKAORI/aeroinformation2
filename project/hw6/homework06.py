#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:49:20 2018

@author: 1194751660
"""

import numpy as np

class Marcov():
    def __init__(self):
        self._mat = np.array(np.zeros((9,9)))
        for j in range(9):  
            self._search_s(j)
            for k in range(len(self._side)):
                self._mat[int(self._side[k])][j] = 1/len(self._side)
        self._pt = np.array(np.full(9,1/9)).T
    def _search_s(self,j):
        self._side = np.array([])
        self._side = np.append(self._side,[j])
        if((j-1) in range(0,9) and ((j % 3) != 0)):
            self._side = np.append(self._side,[j-1])
        if((j+1) in range(0,9) and ((j+1) % 3) != 0):
            self._side = np.append(self._side,[j+1])
        if(j-3) in range(0,9):
            self._side = np.append(self._side,[j-3])
        if(j+3) in range(0,9):
            self._side = np.append(self._side,[j+3])
    def _q1(self):
        for i in range(10000):
            self._pt = np.dot(self._mat,self._pt)
        print('Q1 is',self._pt)
    def _q2(self):
        self._lmd,self._V = np.linalg.eigh(self._mat)
        print('Q2 is',self._V[np.argmax(self._lmd)])
    def exec_all(self):
        self._q1()
        self._q2()
        
        
                
marcov=Marcov()
marcov.exec_all()

