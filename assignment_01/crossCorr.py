# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:36:42 2021

@author: sophi
"""

# Imports
import numpy as np

'''
Cross correlation function
Inputs: x,y numpy arrays (float)
Output: z numpy array (float)
'''
def crossCorr(x,y):
    # determine max value of eta
    maxShift = x.size + y.size + 1
    
    # zero pad y
    yPad = np.pad(y, (x.size,x.size), 'constant', constant_values=(0.0,0.0))
    
    # initialize z
    z = np.zeros(maxShift)
    
    # compute cross correlation
    for eta in range(maxShift):
        for i in range(x.size):
            z[eta] = (x[i] * yPad[i+eta]) + z[eta]

    return z