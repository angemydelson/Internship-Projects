#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:33:37 2023

@author: angemydelson
"""
import numpy as np

entradas = np.array([1, 7, 5])
pesos = np.array([0.8, 0.1, 0])

def soma(e, p):
    return e.dot(p)

s = soma(entradas, pesos)

def setepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = setepFunction(s)