# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:50:50 2021

@author: sophi
"""

# Imports
import numpy as np


'''
Compare output from myTimeConv() with SciPy convolve()
Inputs: x,h signal and impulse response (1D Numpy arrays)
Outputs: m, mean difference (float)
        mabs, mean absolute difference (float)
        stdev, standard deviation of difference (float)
        time, [run_time1, run_time2]
'''
def CompareConv(x,h):
    return m, mabs, stdev, time