# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:56:12 2021

@author: sophi
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from generateSinusoidal import generateSinusoidal
from generateSquare import generateSquare

'''
Compute fft of signal
Inputs: x (signal), sample_rate_Hz
Outputs: f (frequency of bins), XAbs, XPhase, XRe, XIm (numpy arrays)
'''
def computeSpectrum(x, sample_rate_Hz):
    n = x.size
    # calculate fft (single sided)
    X = np.fft.fft(x)
    X = X[0:int(n/2)]
    
    # calculate magnigute and phase
    XAbs = np.abs(X)
    XPhase = np.angle(X)
    
    # find real and imaginary components
    XRe = X.real
    XIm = X.imag
    
    # calculate frequency array f (single sided)
    f = np.linspace(0,sample_rate_Hz/2,int(n/2), endpoint=False)
    return f,XAbs,XPhase,XRe,XIm


# Sinusoid spectrum
_,sin = generateSinusoidal(1.0, 44100, 400, 0.5, np.pi/2)
f,XAbs,XPhase,XRe,XIm = computeSpectrum(sin, 44100)

plt.figure()
fig,axs = plt.subplots(2)
plt.suptitle('Sinusoid spectrum (f=400, $\phi = \pi/2$)')
axs[0].plot(f,XAbs)
axs[0].set(xlabel='frequency (Hz)', ylabel='Magnitude')
axs[1].plot(f,XPhase)
axs[1].set(xlabel='frequency (Hz)', ylabel='Phase (radians)')

# Export figure
# plt.savefig('results/03-sinusoidSpectrum.png')

plt.show()


# Square spectrum
_, sqr = generateSquare(1.0, 44100, 400, 0.5, 0)
f,XAbs,XPhase,XRe,XIm = computeSpectrum(sqr, 44100)

plt.figure()
fig,axs = plt.subplots(2)
plt.suptitle('Square spectrum, 10 sinusoidals (f=400, $\phi$ = 0)')
axs[0].plot(f,XAbs)
axs[0].set(xlabel='frequency (Hz)', ylabel='Magnitude')
axs[1].plot(f,XPhase)
axs[1].set(xlabel='frequency (Hz)', ylabel='Phase (radians)')

# Export figure
# plt.savefig('results/03-squareSpectrum.png')

plt.show()
