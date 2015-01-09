#!/usr/bin/env python





# File Docstring
"""UNTITLED GAME [v0] <DEBUG>
(c) YEAR AUTHOR"""
print(__doc__)
print('')





# Game Class
class game(object):
    """The 'game' object, to encapsulate the game as an object with assets."""

    def __init__(self):
        """Initialize an instance of the game object."""

        # Game Information
        self.name = 'UNTITLED GAME'
        self.version = '0.0.0'
        self.year = '20XX'
        self.author = 'AUTHOR'
        self.py_version = '3.3.2'

        # Game-Global Constants
        pass

    
    
    def run(self):
        """Execute and run the game."""

        # Initialize Game Resources
        pygame.mixer.pre_init(44100, 16, 2, 4096) # Pygame Mixer Presets (freq, size, mono/stereo, buffer)
        pygame.init() # Initialize Pygame
        os.environ['SDL_VIDEO_CENTERED'] = '1' # Center Displays
        

        # Console Interface Set-Up
        CONSOLE = {'VIDEO':   video((550, 400)),
                   'AUDIO':   audio(),
                   'JOY':     joy(),
                   'SPRITER': spriter(),
                   'CLOCK':   pygame.time.Clock(),
                   'FONT':    pygame.font.SysFont(None, 12)}





        # Core Loop
        CONSOLE['VIDEO'].splashscreen(2) # Splashscreen (OPTIONAL)
        CONSOLE['VIDEO'].build() # Build Screen
        pygame.event.get() # Purge Event Queue
        
        CONSOLE['CLOCK'].tick(CONSOLE['VIDEO'].fps) # Establish Framerate
        CL = True # Core Loop Switch
        while CL == True:
            CONSOLE['CLOCK'].tick(CONSOLE['VIDEO'].fps) # Maintain Framerate
            pygame.event.pump() # Pump events to prevent lock-up when no events pass.

            # Activity/Scene Tree
            newscene = SCN_scene()
            ROU_newscene = newscene.start(CONSOLE)
            if ROU_newscene == 'END SCENE' or ROU_newscene == 'EXIT GAME':
                CL = False
            else:
                pass

        # Clean-Up
        pygame.quit() # Close Pygame
        return 'END GAME' # End Run




        
# Main Program
if __name__ == '__main__':
    
    # IMPORT GAME RESOURCES
    # Python Standard Packages
    import datetime
    import math
    import os
    import pickle
    import random
    import sys
    import time
    
    # Third-Party Packages
    import pygame
    from pygame.locals import *

    # Framework Packages
    from DIR_data.DIR_console.DAT_audio import *
    from DIR_data.DIR_console.DAT_joy import *
    from DIR_data.DIR_console.DAT_video import *

    # Game-Specific Packages
    from DIR_data.DAT_scene import *
    


    # Game
    G = game() # Itemize Game
    G.run() # Run Game
    sys.exit(0) # Complete Exit
