#!/usr/bin/env python





# File Docstring
"""Scene: NAME

This scene file is used as a template to create
different scenes in the game. Describe what it
would do here."""





# Import Materials
import pygame
from pygame.locals import *

from .DIR_asset.DAT_asset import *





# Scene Class
class SCN_scene(object):
    """The new scene class."""
    def __init__(self):
         """Initialize and prepare."""
         
         # Scene Class Attributes
         pass


    def start(self, c):
        """Start the scene."""
        # Constants
        # Loop-Local Constant Variables
        pass

        # Location-Specific Updating
        # LSU is optional! It's good for saving memory on updating the screen in the specific circumstance of a
        # non-animated background, because it simply covers old sprite locations instead of flushing
        # out the entire screen. But its limitation is of course needing a static background to do that. It is
        # perfect for really simple arcade-style games or really retro-inspired games (think Pong)... Unless
        # you know what you're doing with it to make a really stellar game to run on this performance.
        #
        # To use location-specific updating, you must first have a list ready to collect old rects,
        # then make a dedicated static background (here I made canvas), then blit the background to
        # the display surface, and lastly call an update to the display.
        #
        # Don't forget to set up the render() parameters to operate LSU. Otherwise it renders normally.
        LST_rectchange = [] # Stores used sprite rects.
        canvas = pygame.Surface(c['VIDEO'].size).convert() # A background canvas.
        canvas.fill((255, 255, 255)) # Fill the canvas.
        c['VIDEO'].disp.blit(canvas, (0, 0)) # Blit the canvas to the display.
        c['VIDEO'].show()

        # Sprite Group Dictionary (Add the sprites to these directly; the list below is to put them in order for rendering.)
        DIC_spritegroup = {'sample': pygame.sprite.RenderUpdates()} # Sample Group
        
        # Sprite Group List (Orders the sprite groups in the Sprite Group Dictionary.) [0-N; where 0 is backmost & N is foremost]
        LST_spritegroup = [DIC_spritegroup['sample']] # Sample Group

        # Game Objects
        x = asset(c)

        # Prepare Scene
        pygame.mouse.set_visible(False) # Disable the console mouse visibility for the chapter before the loop.
        LST_spritegroup[0].add(x.sprite)
        





        # Scene Loop
        pygame.event.get() # Purge Input Queue
        c['CLOCK'].tick(c['VIDEO'].fps)
         
        SL = True # Scene Loop Switch
        while SL == True:
            # FRAMERATE HANDLING
            # Maintain framerate and variables before handling and executions.
            dt = float(c['CLOCK'].tick(c['VIDEO'].fps)) # Lock framerate and return milliseconds since last tick() as delta-time.
            if dt > 1000.0 / c['VIDEO'].fps: 
                dt = 1000.0 / c['VIDEO'].fps # Cap delta-time at the maximum amount of milliseconds per frame.
            df = dt / 1000.0 # Convert delta-time to delta-frame, for frame-independent motion.
             
               
            # EVENT HANDLING
            # Invoke any events and changes triggered by the user.
            pygame.event.pump() # Pump event queue to prevent lock-up if no event calls are passed.
            for evt in pygame.event.get():
                if evt.type is QUIT:
                    return 'EXIT GAME'
                elif evt.type is KEYDOWN:
                    if evt.key == K_ESCAPE:
                        SL = False

            keypress = pygame.key.get_pressed()
            if keypress[K_d]:
                x.method()
                        

            # DATA RENDERING
            # Update game logic, such as a position, an ability, a change, etc.
            pass


            # SCREEN RENDERING
            # Take all image data and place them accordingly.
            c['VIDEO'].render(LST_spritegroup, LST_rectchange, canvas, color=(127, 127, 127))
                
             
        # Clean-Up
        return 'END SCENE' # End
