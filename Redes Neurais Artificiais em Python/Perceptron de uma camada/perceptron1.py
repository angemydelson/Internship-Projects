# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 14:16:04 2017

@author: Jones
"""
entradas = [-1, 7, 5]
pesos = [0.8, 0.1, 0]

def soma(e, p):
    s = 0
    for i in range(3):
        #print(entradas[i])
        #print(pesos[i])
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

r = stepFunction(s)
