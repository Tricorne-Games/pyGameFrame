#!/usr/bin/env python3

"""scn_d

This file is a test scene.

This one is used specifically for
testing user events."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from bases import Scene
from uevents import uEvent





# TEST SCENE
class SceneD(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.testvar = 0
        self.color = (127, 127, 127)
    def process(self, events):
        print(events)
        for evt in events:
            if evt.type == USEREVENT:
                if evt.spec == 'Test':
                    self.color = (255, 255, 255)
    def update(self):
        print(self.testvar)
        if self.testvar <= 99:
            self.testvar += 1
        if self.testvar == 100:
            self.testvar += 1
            pygame.event.post(uEvent['Test'])
        if self.testvar <= 101:
            pass
    def render(self, display):
        display.fill(self.color)
