# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:33:36 2021

@author: sophi
"""

# Imports
from myTimeConv import myTimeConv
from loadSoundFile import loadSoundFile
from CompareConv import CompareConv
import numpy as np
import matplotlib.pyplot as plt

############### QUESTION 1 #################
# create DC signal x
x = np.ones(200, dtype=float)

# create triangle impulse response h
h = np.append(np.linspace(0.0, 1.0, num=25, endpoint=False), np.linspace(1.0, 0.0, num=26, endpoint=True))

# convolve x and h
y_time = myTimeConv(x, h)

# plot convolution
plt.figure()
plt.title('Convolution of DC signal and triangle impulse response')
plt.xlabel('time (samples)')
plt.ylabel('amplitude')
plt.plot(y_time)

# Export figure
# plt.savefig('results/01-convolution.png')

plt.show()

############## QUESTION 2 #################
# load audio files
x = loadSoundFile('piano.wav')
h = loadSoundFile(('impulse-response.wav'))

# compare convolution functions
m, mabs, stdev, time = CompareConv(x, h)

# Save in text file
f = open("results/02-comparison.txt", "w")
f.write('m = %s\n' % m)
f.write('mabs = %s\n' % mabs)
f.write('stdev = %s\n' % stdev)
f.write('time = [%s %s]\n' % (time[0],time[1]))
f.close()