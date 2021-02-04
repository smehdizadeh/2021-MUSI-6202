# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:55:41 2021

@author: sophi
"""

# Imports
import numpy as np

'''
Q:  if the length of x is 200, and the length of h is 100, what is
    the length of y = x*h?
A:  200 + 100 - 1 = 299 (assuming discrete convolution)
'''

'''
Sample by sample time domain convolution
Inputs: x,h signal and impulse response (1D Numpy arrays)
Output: y convolution output (1D Numpy array)
'''
def myTimeConv(x,h): 
    # zero pad x
    xPad = np.pad(x, (h.size-1,h.size-1), 'constant', constant_values=(0.0,0.0))
    
    # reflect h about the y axis
    hFlip = np.flip(h)
    
    # initialize y
    convSize = x.size + h.size - 1
    y = np.zeros(convSize)
    
    # compute cross correlation
    for n in range(convSize):
        y[n] = np.sum(np.multiply(hFlip,xPad[n:n + h.size]))
        
    return y