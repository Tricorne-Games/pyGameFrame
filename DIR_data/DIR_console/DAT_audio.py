#!/usr/bin/env python





# File Docstring
"""Console: Audio

This is the Audio class. It manages the layout
and use of the sound, channels, music, etc."""





# Import Materials
import os
import pygame
from pygame.locals import *


# Audio Class
class audio(object):
    """The Audio class; to handle sound management."""
    def __init__(self, channelcount=8):
        """Initialize the Audio system."""
        pass
    
        # Played sound effects return a Channel object.
        # You can play sounds in a specific channel with: Channel().play(Sound())
        #
        # Music is only played one file at a time, as it streams.
        # It is treated differently from channel-based sounds.
            

    def loadFile(self, sndmus, filename):
        """Returns a 'Sound' or 'Music' class."""
        
        class NoneSound(object):
            """A dummy class, if a file cannot be loaded."""
            def play(self):
                """Do nothing, in place of playing."""
                pass
        try:
            if not pygame.mixer or not pygame.mixer.get_init():
                print("NOTICE: pygame.mixer not detected! Loading NoneSound()...")
                return NoneSound()
            if sndmus == 'SND':
                soundfile = pygame.mixer.Sound(filename)
            elif sndmus == 'MUS':
                soundfile = pygame.mixer.music.load(filename)
            return soundfile
        except:
            print("ERROR - Problem loading file:", filename, " - Loading NoneSound()...")
            return NoneSound()

    def reloadMixer(self, fq=44100, sz=16, ms=2, bf=4096):
        """Shuts down and restarts the mixer with new settings."""
        # fq = Frequency
        # sz = Size (-sz are signed samples.)
        # ms = Mono/Stereo (1 for Mono, or 2 for Stereo.)
        # bf = Buffer (Value must always be a power of 2.)
        pygame.mixer.quit()
        pygame.mixer.init(fq, sz, ms, bf)
    
    def stereo_pan(self, x_coord, screen_width):
        """Return volume values for a channel, to enable a stereo-panning effect."""
        right_volume = float(x_coord) / screen_width
        left_volume = 1.0 - right_volume
        return left_volume, right_volume
