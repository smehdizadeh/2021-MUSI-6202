# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:40:56 2021

@author: sophi
"""

# Imports
import scipy.io as sio
import numpy as np

'''
Function to load audio files
Input: filepath (string)
Output: x 1D numpy array (float)
'''
def loadSoundFile(filename):
    # read audio file and store as ndarray data
    sampRate, data = sio.wavfile.read(filename)
    
    # reduce to 1 channel and convert to float
    x = np.array(data[:,0], dtype=float)
    return x