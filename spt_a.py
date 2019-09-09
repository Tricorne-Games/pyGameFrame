#!/usr/bin/env python3

"""spt_a

This file contains a test sprite object
and a test actor to contain it."""

# Import built-in libraries.
import os

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from bases import Actor





# Test Actor Object
class ActorTest(Actor):
    def __init__(self):
        Actor.__init__(self)
        self.sprite = SpriteTest()

# Test Sprite Object
class SpriteTest(pygame.sprite.Sprite):
    frame = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if self.frame == None:
            frame = [pygame.Surface((32, 32)).convert()]
            frame[0].fill((127, 127, 127))
        self.image = frame[0]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
