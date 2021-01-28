# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:40:12 2021

@author: sophi
"""

# Imports
from loadSoundFile import loadSoundFile
from crossCorr import crossCorr
from scipy.signal import find_peaks


'''
Function to estimate snare position within drum loop track
Inputs: filepaths to snare sample and drum loop (string)
Output: locations in samples (list)
'''

def findSnarePosition(snareFilename, drumloopFilename):
    # Load both audio files
    x = loadSoundFile(snareFilename)
    y = loadSoundFile(drumloopFilename)
    
    # Compute correlation
    z = crossCorr(x, y)
    
    # Find correlation maxima
    snareLoc, _ = find_peaks(z, height=1e11)
    snareLoc = snareLoc.tolist()
    
    return snareLoc


# Call function
Loc = findSnarePosition('snare.wav', 'drum_loop.wav')

# Save in text file
f = open("results/02-snareLocation.txt", "w")
for number in Loc:
    f.write('%s\n' % number)
f.close()