# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:36:40 2021

@author: sophi
"""

# Imports
from computeSpectrum import computeSpectrum
from generateBlocks import generateBlocks
from generateSquare import generateSquare
import numpy as np
import matplotlib.pyplot as plt

'''
Compute fft and generate spectrogram with windowing
Inputs: x,  block_size, hop_size, sampling_rate_Hz, window_type (string)
OUtputs: freq_vector (col vector), time_vector (col vector), magnitude_spectrogram (block_size/2 x N matrix)
'''
def mySpecgram(x,  block_size, hop_size, sampling_rate_Hz, window_type):
    # block the input signal
    time_vector,X = generateBlocks(x, sampling_rate_Hz, block_size, hop_size)
    
    # compute fft of signal blocks
    magnitude_spectrogram = np.zeros((int(block_size/2),time_vector.size))
    for i in range(0,time_vector.size):
        # apply hanning window
        if window_type=='hann':
            X[:,i] = np.multiply(X[:,i],np.hanning(block_size))
       
        freq_vector,magnitude_spectrogram[:,i],_,_,_ = computeSpectrum(X[:,i], sampling_rate_Hz)
        
    # plot spectrogram
    plt.figure()
    plt.pcolor(time_vector, freq_vector, magnitude_spectrogram, shading='auto', cmap='plasma', vmin=0, vmax=800)
    plt.title('Square wave spectrogram using %s window' % window_type)
    plt.xlabel('Time (seconds)')
    plt.ylabel('Frequency (Hz)')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Magnitude')
    return freq_vector,time_vector,magnitude_spectrogram


# square wave spectrogram using rectangular window
_,sqr = generateSquare(1.0, 44100, 400, 0.5, 0)
freq_vector,time_vector,magnitude_spectrogram = mySpecgram(sqr, 2048, 1024, 44100, 'rect')

# Export figure
# plt.savefig('results/04-rectSpectrum.png')

plt.show()

# square wave spectrogram using hanning window
freq_vector,time_vector,magnitude_spectrogram = mySpecgram(sqr, 2048, 1024, 44100, 'hann')

# Export figure
# plt.savefig('results/04-hannSpectrum.png')

plt.show()
