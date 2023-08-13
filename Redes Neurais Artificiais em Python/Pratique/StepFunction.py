# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

def setepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = setepFunction(s)

print("teste")