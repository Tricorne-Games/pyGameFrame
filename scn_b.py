#!/usr/bin/env python3

"""scn_b

This file is a test scene.

This one is specifically used for testing
scene swaps and model data manipulation."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from bases import Scene
import model





# TEST SCENE
class SceneB(Scene):
    
    def __init__(self):
        Scene.__init__(self)
        
    def process(self, events):
        for evt in events:
            if evt.type == pygame.KEYDOWN:
                if evt.key == pygame.K_SPACE:
                    self.nextScene = 'A'
                elif evt.key == pygame.K_UP:
                    model.x += 1
                    print(model.x)
                elif evt.key == pygame.K_DOWN:
                    model.x -= 1
                    print(model.x)
                
    def update(self):
        pass
    
    def render(self, display):
        display.fill((0, 255, 0))
