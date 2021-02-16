# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 21:48:43 2021

@author: sophi
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

'''
Generate Sinusoidal Function
Inputs: amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians
Outputs: t,x numpy arrays (time and signal)
'''
def generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    # create the time array
    numSamples = int(length_secs*sampling_rate_Hz)
    t = np.linspace(0, length_secs, num=numSamples, endpoint=True)
    
    # generate sinusoid (A*sin(wt+ph))
    x = amplitude * np.sin(2*np.pi*frequency_Hz*t + phase_radians)
    
    return t,x


t,x = generateSinusoidal(1.0, 44100, 400, 0.5, np.pi/2)

# Plot sinusoid
plt.figure()
plt.suptitle(r'$x(t) = \mathcal{A}\/\sin(2 \pi f t + \phi)$')
plt.title('A=1.0, f=400 Hz, $\phi = \pi$ /2')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.plot(t[0:int(0.005*44100)],x[0:int(0.005*44100)])

# Export figure
plt.savefig('results/01-sinusoid.png')

plt.show()
