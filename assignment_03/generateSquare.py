# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:19:10 2021

@author: sophi
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt
from generateSinusoidal import generateSinusoidal

'''
Generate Square wave Function
Inputs: amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians
Outputs: t,x numpy arrays (time and signal)
'''
def generateSquare(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians):
    # generate fundamental and time vector
    t,x = generateSinusoidal(amplitude, sampling_rate_Hz, frequency_Hz, length_secs, phase_radians)
    
    # generate harmonics and add
    for n in range(3,21,2):
        _,xnew = generateSinusoidal((1/n)*amplitude, sampling_rate_Hz, n*frequency_Hz, length_secs, phase_radians)
        x = x + xnew
        
    # scale for amplitude
    x = (4/np.pi)*x
    return t,x


t,x = generateSquare(1.0, 44100, 400, 0.5, 0)

# Plot square wave
plt.figure()
plt.suptitle('Square wave using 10 sinusoidals')
plt.title('A=1.0, f=400 Hz, $\phi$ = 0')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.plot(t[0:int(0.005*44100)],x[0:int(0.005*44100)])

# Export figure
# plt.savefig('results/02-square.png')

plt.show()
