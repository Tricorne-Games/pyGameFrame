#!/usr/bin/env python3

"""bases

This file contains the base classes for objects
used internally, kept separate from any other
files that use them."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Scene Class
class Scene(object):
    """The base Scene class."""
    
    def __init__(self):
        """Initialize the scene."""
        self.name = self.__class__.__name__
        self.nextScene = 'CURRENT'
           
    def process(self, events):
        """Read through events to update."""
        raise NotImplementedError(self.name + " 'process()' method must be defined!")

    def update(self):
        """Update the scene logic."""
        raise NotImplementedError(self.name + " 'update()' method must be defined!")

    def render(self, display):
        """Draw scene data to the screen."""
        raise NotImplementedError(self.name + " 'render()' method must be defined!")



# Actor Class
class Actor(object):
    """The base Actor class."""

    def __init__(self):
        """Initialize the actor."""
        pass
    


# Player Class
class Player(object):
    """The base Player class."""

    def __init__(self, iden):
        """Initialize the player."""
        self.iden = iden
