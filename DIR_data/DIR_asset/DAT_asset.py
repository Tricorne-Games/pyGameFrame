#!/usr/bin/env python





# File Docstring
"""Asset: NAME

The 'asset' class. An 'asset' in this game framework
is like 'objects' in any other build, such as a hero,
a platform, a player, a tile, an item, a setting, etc.
The reason I used a different name is to keep it away
from any other use of the word 'object'.

===

At your convenience, the 'sprite' class is also included
here. This is so that any and all classes that have some
form of visual representation in graphics work have their
corresponding sprite class. The sprite class only work
the visual element of a class, and are not the class
itself.

Remember to keep the 'img' and 'frm' elements of your sprite
classes handy. This allows for new instances of the sprite
to be called without having to keep working the spriter to
apply the new graphics; as the sprite class will retain the
information, game-wide."""





# Import Materials
import pygame
from pygame.locals import *

from ..DIR_console.DAT_spriter import spriter
from ..DIR_console.DAT_audio import audio





# Asset Class
class asset(object):
    """The Asset class. Describe it here."""
    def __init__(self, c):
        """Initialize the class."""
        # You need an array of sound effects.
        self.sound = c['AUDIO'].loadFile('SND', 'DIR_data\\DIR_asset\\laser.ogg')
        self.spritesheet = c['SPRITER'].setSpritesheet('DIR_data\\DIR_asset\\spritesheet.png')
        
        self.sprite = self.SPT_asset(c, self.spritesheet)


    def method(self):
        """A sample method."""
        self.sound.play()
        print("TEST ASSET METHOD!")


    class SPT_asset(pygame.sprite.Sprite):
        """The Asset's Sprite class."""
        img = None # Pre-load Image to optimize sprite instantiation.
        frm = None # Pre-load Frames to optimize sprite instantiation.

        # Main Sprite Functions (__init__ and update)
        def __init__(self, c, sst):
            """Initialize the sprite."""
            pygame.sprite.Sprite.__init__(self) # Initialize Sprite Module.

            initsize = (16, 16) # Initial size of sprite graphic.

            # Pre-load image and frames.
            if self.img is None: # Still Image
                self.img = c['SPRITER'].applyGraphic(sst, ((1, 1), initsize), (255, 0, 255))
            if self.frm is None: # Frames
                self.frm = c['SPRITER'].applyFrames(sst, [((1, 1), initsize),
                                                          ((18, 1), initsize),
                                                          ((1, 18), initsize),
                                                          ((18, 18), initsize)], (255, 0, 255))

            # Standard Sprite Attributes (image & rect)
            self.image = self.img # The main image represented in each frame.
            self.rect = self.image.get_rect() # The rect containing the sprite.

            # Auxiliary Sprite Attributes (manipulation, animation, etc.)
            self.alpha = 255 # Alpha Channel value for translucency effects.
            self.frame = self.frm # List of Frames from the sheet.
            self.cf = 0 # The number to identify a 'current frame'.
            self.pause = 0 # The pause value to delay a frame of animation to the next frame.
            self.delay = 10 # The checkpoint to reset the pause value.

        def update(self):
            """Update the sprite."""
            self.animate() # A sample effect called in updating.
            self.rect.topleft = pygame.mouse.get_pos() # Bring sprite rect to mouse.


        # Other Sprite Functions
        def animate(self):
            """Sample method to animate something."""
            self.pause += 1 # Add to self.pause.
            if self.pause >= self.delay:
                self.pause = 0 # Reset self.pause.
                self.cf += 1 # Prepare next frame.
                if self.cf >= len(self.frame):
                    self.cf = 0 # Reset next frame to 0.
            self.image = self.frame[self.cf] # Turn the sprite image into the frame.
