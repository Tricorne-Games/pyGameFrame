#!/usr/bin/env python3

"""mgr_audio

This file contains the Audio Manager, used for
manipulating sounds, and any other supplementary
classes related to handling sounds/music."""

# Import built-in libraries.
import os

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Audio Manager
fq = 44100 # Frequency.
sz = 16 # Size; -sz are signed samples.
ms = 2 # Mono/Stereo; 1 for Mono, 2 for Stereo.
bf = 4096 # Buffer; must always be a power of 2.
assetpath = ''

channel = {}
song = {}

def preinitMixer():
    """Set up the audio mixer."""
    global fq, sz, ms, bf
    pygame.mixer.pre_init(fq, sz, ms, bf)

def loadMixer():
    """Sets up the mixer with new settings."""
    global fq, sz, ms, bf
    if checkMixer() == True:
        pygame.mixer.quit()
    pygame.mixer.init(fq, sz, ms, bf)

def checkMixer():
    """Check to see if mixer is present."""
    return pygame.mixer or pygame.mixer.get_init()

def changeFreq(new_fq):
    """Change the Frequency."""
    global fq
    fq = new_fq

def changeSize(new_sz):
    """Change the Size. A negative value means signed samples."""
    global sz
    sz = new_sz

def changeMS(new_ms):
    """Change the Mono/Stereo setting. 1 for Mono, 2 for Stereo."""
    global ms
    if not (new_ms == 1 or new_ms == 2):
        print("WARNING: M/S setting must be 1 for Mono or 2 for Stereo!")
        return
    ms = new_ms

def changeBuffer(new_bf):
    """Change the Buffer. This value must be a power of 2."""
    global bf
    def checkPower(n):
        """Tests the power-of-2 validity of the given number."""
        isValid = None
        n = n / 2
        if n == 2:
            print('VALID')
            isValid = True
        elif n > 2:
            print('CHECKING')
            checkPower(n)
        else:
            print('INVALID')
            isValid = False
        return isValid
    test_bf = checkPower(new_bf)
    if test_bf == True:
        bf = new_bf
    else:
        # Default to 4096.
        print("Setting default buffer to 4096.")
        bf = 4096

def loadFile(filename):
    """Load a sound file."""
    global assetpath
    filepath = os.path.join(assetpath, filename)
    soundfile = pygame.mixer.Sound(filepath)
    return soundfile

def createNewChannel(channel_id):
    """Creates a new channel."""
    return pygame.mixer.Channel(channel_id)

def playChannel(channelopt, item, loops=0, maxtime=0, fade_ms=0):
    """Plays an item, such as a song or sound, into a channel to play."""
    global channel
    channel[channelopt].play(item, loops, maxtime, fade_ms)

def stopChannel(channels):
    """Stops select or all channels from playing.
To ensure the right channels are selected, you must input a list of channels
or use 'ALL' for every present channel."""
    global channel
    if channels == 'ALL':
        for eachChannel in channel:
            eachChannel.stop()
    else:
        for eachChannel in channels:
            channel[eachChannel].stop()

def stereo_pan(x_coord, screen_width):
    """Return volume values for a channel, to enable a stereo-panning effect."""
    right_volume = float(x_coord) / screen_width
    left_volume = 1.0 - right_volume
    return left_volume, right_volume
    
def setChannels():
    """Sets up the channels."""
    global channel
    channel = {
        'music': createNewChannel(0),
        'c1': createNewChannel(1)
    }

def setSongs():
    """Sets up the songs."""
    global song
    song = {
    }
