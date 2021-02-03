# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:50:50 2021

@author: sophi
"""

# Imports
import numpy as np
from scipy import signal
import time as t
from myTimeConv import myTimeConv

'''
Compare output from myTimeConv() with SciPy convolve()
Inputs: x,h signal and impulse response (1D Numpy arrays)
Outputs: m, mean difference (float)
        mabs, mean absolute difference (float)
        stdev, standard deviation of difference (float)
        time, [run_time1, run_time2]
'''
def CompareConv(x,h):
    # get convolution result from both functions and time
    start1 = t.time()
    y1 = myTimeConv(x, h)
    end1 = t.time()
    
    start2 = t.time()
    y2 = signal.convolve(x, h)
    end2 = t.time()
    
    m = np.mean(np.subtract(y1, y2))
    mabs = np.mean(np.abs(np.subtract(y1, y2)))
    stdev = np.std(np.subtract(y1, y2))
    time = np.array([end1-start1, end2-start2])
    return m, mabs, stdev, time