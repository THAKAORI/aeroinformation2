#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:53:41 2018

@author: 1194751660  03-180341
"""
def len_sort():
    words=[line.strip() for line in open('words.txt').readlines()]
    words.sort(key=lambda x: -len(x))
    for i in range(10):
        print(i+1,':',words[i],':',len(words[i]))

def clen_search():
    words=[line.strip() for line in open('words.txt').readlines()]
    common_len=(list(map(lambda x: (list(map(lambda x: len(x),words))).count(x),range(22)))).index(max(list(map(lambda x: (list(map(lambda x: len(x),words))).count(x),range(22)))))
    print('Most appeared word length is',common_len)

def alpha_search():
    words=[line.strip() for line in open('words.txt').readlines()]
    words_list=','.join(words)
    for i in range(ord('a'),ord('z')+1):
        print(chr(i),'is',words_list.count(chr(i)))
    
def len_sort2():
    words=[line.strip() for line in open('words.txt').readlines()]
    words.sort(key=lambda x: -len(x))
    i=0
    while 1:
        for j in range(ord('a'),ord('z')+1):
            if(words[i].count(chr(j)))>1:
                break
            elif(j==ord('z')):
                print('no duplication word is',words[i])
                return 0;
        i+=1 
        
def all_exec():
    len_sort()
    print('\n')
    clen_search()
    print('\n')
    alpha_search()
    print('\n')
    len_sort2()

all_exec()