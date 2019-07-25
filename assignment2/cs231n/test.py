# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 08:31:33 2019

@author: qyf11
"""

import numpy as np

a = np.ones([2,2,3])
a[1,1,2] = 3
a[0,0,1] = 4
b = np.mean(a,axis=1)
c = np.mean(a,axis=1)[...,None]
print(a)
print(b)
print(c)