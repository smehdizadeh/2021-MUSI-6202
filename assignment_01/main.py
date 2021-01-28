# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 22:41:21 2021

@author: sophi
"""

# Imports
from crossCorr import crossCorr
from loadSoundFile import loadSoundFile
import matplotlib.pyplot as plt


# Load both audio files
x = loadSoundFile('snare.wav')
y = loadSoundFile('drum_loop.wav')

# Compute correlation
z = crossCorr(x, y)

# Plot correlation
plt.figure()
plt.title('Correlation of snare and drum loop')
plt.xlabel('time (samples)')
plt.ylabel('correlation')
plt.plot(z)

# Export figure
# plt.savefig('results/01-correlation.png')

plt.show()