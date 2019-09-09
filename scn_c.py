#!/usr/bin/env python3

"""scn_c

This file is a test scene.

This one is specifically used for testing
scene swapping errors."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from bases import Scene





# TEST SCENE
class SceneC(Scene):
    
    def __init__(self):
        Scene.__init__(self)
        
    def process(self, events):
        for evt in events:
            if evt.type == pygame.KEYDOWN and evt.key == pygame.K_SPACE:
                self.nextScene = 'NoScene'
                
    def update(self):
        pass
    
    def render(self, display):
        display.fill((255, 0, 0))
