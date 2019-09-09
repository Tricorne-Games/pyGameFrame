#!/usr/bin/env python3

"""scn_e

This file is a test scene.

This one is specifically used for testing
sprite group rendering."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
import mgr_sprite
import mgr_video
from bases import Scene
from spt_a import ActorTest





# TEST SCENE
class SceneE(Scene):
    
    def __init__(self):
        Scene.__init__(self)
        mgr_video.flushBuffer((127, 0, 127))
        self.spritegroup = [
            pygame.sprite.RenderPlain() # Test Spritegroup
        ]
        self.bg = pygame.Surface(mgr_video.size).convert()
        self.bg.fill((127, 0, 127))
        self.a = ActorTest()
        self.a.sprite.add(self.spritegroup[0])
        
    def process(self, events):
        pass
                
    def update(self):
        pass
    
    def render(self, display):
        # Clear
        for eachGroup in self.spritegroup:
            eachGroup.clear(display, self.bg)

        # Update
        for eachGroup in self.spritegroup:
            eachGroup.update()

        # Draw
        for eachGroup in self.spritegroup:
            eachGroup.draw(display)
