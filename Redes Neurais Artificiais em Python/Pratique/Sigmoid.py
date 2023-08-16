#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:23:57 2023

@author: angemydelson
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

a = np.exp(2)
b = sigmoid(10000000)