#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:02:59 2018

@author: 1194751660
"""

def syobon(): #descript a syobon
    print('(´・ω・｀)',end='')

def wait(): #wait about half second
    for i in range(10000000):
        i+=1

def short_wait():
    for i in range(1000000):
        i+=1
        
def many_syobon(): #descript some syobons 
    for i in range(5):
        syobon()
        print('\n')
        wait()
        
def dance_syobon():
    print('\
  ♪　∧,＿∧　　♪\n\
　　 ( ´･ω･) ))\n\
　(( (　つ　ヽ、　　　♪\n\
　　　〉 とノ　)))\n\
　　（__ノ^(＿)\n\
          ')
    wait()
    print('\
       ∧＿,∧　♪\n\
　 (( (･ω･｀ )\n\
♪　 /　⊂　) ))　♪\n\
　　((( ヽつ 〈\n\
　　 (＿)^ヽ__）\n\
          ')   
    wait()
    print('\
♪ 　∧＿∧\n\
　　 (´・ω・`) ))\n\
　(( (　つ　ヽ、\n\
　　　〉 とノ　)))\n\
　　（__ノ^(＿)\n\
          ')
    wait()
    print('\
 ♪　∧,＿∧ ♪\n\
　　（´・ω・｀） ))\n\
　(( (　つ　ヽ、　　　♪\n\
　　　〉 とノ　)))\n\
　　（__ノ^(＿)\n\
          ')
    wait()
    print('\
          ∧_∧\n\
　　　　　　(´・ω・`)\n\
　　　　　　ノ ⊂　) ))\n\
　　　　(( （　ヽつ〈 \n\
　　　　　 (＿)^ヽ__）\n\
          ')
 
def dokodoko():
    for i in range(50):
        print('ﾄﾞｺﾄﾞｺ┗(^o^)┛',end='')
        short_wait()
        
        
def muscle_syobon():
    
    dokodoko()

    for i in range(3):
        wait()
    
    print('\
          .\n\
　∧∧\n\
(´･ω･`)　　　n\n\
⌒｀γ´⌒`ヽ( E)\n\
(　.人 .人　γ /\n\
=(こ/こ/　｀^´\n\
)に/こ(\n\
\n\
　　　　　　 ／ﾌﾌ 　　　　　　 　ム｀ヽ\n\
　　　　　　/ ノ)　　 ∧∧　　　　　）　ヽ\n\
　　　　　ﾞ/ ｜　　(´・ω・`）ノ⌒（ゝ._,ノ\n\
　　　　　/　ﾉ⌒7⌒ヽーく　 ＼　／\n\
　　　　　丶＿ ノ ｡　　 ノ､　　｡|/\n\
　　　　　　　 `ヽ `ー-_人`ーﾉ\n\
　　　　　　　　 丶 ￣ _人"彡ﾉ\n\
　　　　　　　　　ﾉ　　r"十ヽ/\n\
　　　　　　　／｀ヽ _/　十∨\n\
\n\
　　　　　（ 　´・ω）\n\
　　　　γ/　 γ⌒ヽ　（´；ω；｀）　　ｳｯ…\n\
　　　　/ |　　　、 　ｲ（⌒　>>1　⌒ヽ\n\
　　　 .l　|　　　 l 　　}　）ヽ ､_､_,　＼ ＼\n\
　　　 {　 |　　　 ｌ、　´⌒ヽ-"巛(　　/　/\n\
　　　 .＼ |　　　　T """ ――‐‐"＾　（､_ﾉ\n\
　 　 　 　 |　　　　| 　　／　／/　 /\n\
          ')
    
    
syobon()
wait()
many_syobon()
dance_syobon()
muscle_syobon()