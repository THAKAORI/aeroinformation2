#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 08:55:44 2018

@author: 1194751660
"""

def is_power(a,b,n):
    print(abs(a))
    if a==b**n:
        print('The result is',b,'^',n,'=',a,'.')
        return
    elif a<(b**n) or abs(b)<=1:
        print('No answer!')
        return
    
    is_power(a,b,n+1)


b=int(input('Please Enter the base: '))    
a=int(input('Please Enter the powered number: '))

is_power(a,b,0)
