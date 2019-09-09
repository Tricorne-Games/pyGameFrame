#!/usr/bin/env python3

"""uevents

This file contains user-defined events to be
used throughout the game."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Events Dictionary
uEvent = {
    'Test': pygame.event.Event(pygame.USEREVENT, spec='Test'),
    'Tick': pygame.event.Event(pygame.USEREVENT, spec='Tick')
}
