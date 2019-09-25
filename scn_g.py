#!/usr/bin/env python3

"""scn_g

This file is a test scene.

This one is used for testing the camera.

Note that this dismisses using sprites and is purely for
testing camera positioning/translating. It uses direct
surface blits instead."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from bases import Scene
from tools import Camera





# TEST SCENE
class SceneG(Scene):
    
    def __init__(self):
        Scene.__init__(self)
        # For this scene, we set up a checkerboard larger than the screen.
        # We also use a "player" surface to test following and clamping.
        self.cam1 = Camera() # Camera
        tilerect = pygame.Rect(0, 0, 50, 50) # A universal tile size.
        surf1 = pygame.Surface(tilerect.size).convert() # First of two colors.
        surf1.fill((255, 0, 0))
        surf2 = pygame.Surface(tilerect.size).convert() # Second of two colors.
        surf2.fill((0, 255, 0))
        self.player = pygame.Surface(tilerect.size).convert() # "Player".
        self.player.fill((0, 0, 255))
        self.playerrect = self.player.get_rect()
        # Create a quick checkerboard worldmap.
        self.worldmap = pygame.Surface((2000, 2000))
        self.wmrect = self.worldmap.get_rect()
        x = 0
        y = 0
        swapcolor = 0
        while y <= self.wmrect.height:
            while x <= self.wmrect.width:
                if swapcolor == 0:
                    self.worldmap.blit(surf1, (x, y))
                    swapcolor += 1
                elif swapcolor == 1:
                    self.worldmap.blit(surf2, (x, y))
                    swapcolor -= 1
                x += tilerect.width
            x = 0
            y += tilerect.height
        # Position the player in an arbitrary coordinate.
        self.playerrect = self.playerrect.move(542, 1022)
        # This variable is for posting the coordinates difference.
        self.wmrenderpos = (0, 0)
        
    def process(self, events):
        # Move player.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.playerrect.move_ip(0, -5)
        if keys[pygame.K_s]:
            self.playerrect.move_ip(0, 5)
        if keys[pygame.K_a]:
            self.playerrect.move_ip(-5, 0)
        if keys[pygame.K_d]:
            self.playerrect.move_ip(5, 0)
                
    def update(self):
        # First check to make sure playerrect doesn't go off map.
        if self.playerrect.bottom >= self.wmrect.bottom:
            self.playerrect.bottom = self.wmrect.bottom
        if self.playerrect.top <= self.wmrect.top:
            self.playerrect.top = self.wmrect.top
        if self.playerrect.left <= self.wmrect.left:
            self.playerrect.left = self.wmrect.left
        if self.playerrect.right >= self.wmrect.right:
            self.playerrect.right = self.wmrect.right
        # Now center the camera on the player.
        self.cam1.rect.center = self.playerrect.center
        # Next, clamp the camera so it also doesn't go off the map.
        # This should allow the character to move freely
        # even if the camera is up against a corner.
        if self.cam1.rect.bottom >= self.wmrect.bottom:
            self.cam1.rect.bottom = self.wmrect.bottom
        if self.cam1.rect.top <= self.wmrect.top:
            self.cam1.rect.top = self.wmrect.top
        if self.cam1.rect.left <= self.wmrect.left:
            self.cam1.rect.left = self.wmrect.left
        if self.cam1.rect.right >= self.wmrect.right:
            self.cam1.rect.right = self.wmrect.right
        # Finally, translate the difference between camera and
        # world coordinates for the render step.
        self.wmrenderpos = self.cam1.translateXY(self.wmrect)
        self.playerrenderpos = self.cam1.translateXY(self.playerrect)
        
    def render(self, display):
        display.fill((0, 0, 0))
        # Blit the worldmap.
        display.blit(self.worldmap, self.wmrenderpos)
        # Blit the player sprite.
        display.blit(self.player, self.playerrenderpos)
