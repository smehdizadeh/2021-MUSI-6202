# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 20:41:39 2021

@author: sophi
"""

# Imports
import numpy as np

'''
Block input signal
Inputs: x, sample_rate_Hz, block_size, hop_size
Outputs: t (numpy array, time stamps), X (block_size x N matrix of blocks)
'''
def generateBlocks(x, sample_rate_Hz, block_size, hop_size):
    # initialize
    n = x.size
    numBlocks = int(np.ceil(n / hop_size))
    t = np.empty(numBlocks)
    X = np.zeros((block_size,numBlocks))
    
    # iterate through input and split up
    for i in range(0,numBlocks):
        t[i] = i * hop_size / sample_rate_Hz
        if (i*hop_size)+block_size < n:
            X[:,i] = x[(i*hop_size):((i*hop_size)+block_size)]
        else:
            X[0:(n-i*hop_size),i] = x[(i*hop_size):]
    
    return t,X