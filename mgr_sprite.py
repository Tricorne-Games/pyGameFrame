#!/usr/bin/env python3

"""mgr_sprite

This file contains the Sprite Manager, which
prepares image files for use inside the Pygame
environment and manages sprites and their groups.

Remember to keep the image and frame elements
of your sprite objects inside the class rather
than the __init__ method. This allows for new
instances of the sprite to be loaded without
having to rework to apply new graphics."""

# Import built-in libraries.
import os

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Sprite Manager
spritesheet = {}
changerects = []

def setSpritesheet(filename, A=False):
    """Load a spritesheet."""
    filepath = os.path.join('', filename)
    if A == True:
        return pygame.image.load(filepath).convert_alpha()
    return pygame.image.load(filepath).convert()

def setColorkey(image, colorkey):
    """Apply a colorkey for transparency."""
    # IF AN ALPHA CHANNEL IS INVOLVED, PUT IT INTO ACCOUNT HERE!
    if colorkey == 0:
        colorkey = image.get_at((0, 0)) # Use top-left pixel.
    image.set_colorkey(colorkey, pygame.RLEACCEL)

def applyGraphic(sourcesheet, rect, colorkey=None, A=False):
    """Apply a graphic."""
    selection = pygame.Rect(rect)
    if A == True:
        graphic = pygame.Surface(selection.size).convert_alpha()
    else:
        graphic = pygame.Surface(selection.size).convert()
    graphic.blit(sourcesheet, (0, 0), selection)
    if colorkey is not None:
        setColorkey(graphic, colorkey)
    return graphic

def applyFrames(sourcesheet, rectList, colorkey=None, A=False):
    """Apply a series of graphics as frames."""
    frames = []
    for rect in rectList:
        frames.append(self.applyGraphic(sourcesheet, rect, colorkey, A))
    return frames
