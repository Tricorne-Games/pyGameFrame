#!/usr/bin/env python3

"""camera

This file contains a camera class that is used for
games with larger-spanned worlds, such as scrolling
or pseudo-3D.

This is designed to be instantiable, in case the
game calls for more than one camera."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Camera
class Camera(object):
    """The Camera class."""
    def __init__(self):
        """Initialize the Camera."""
        self.xpos = 0
        self.ypos = 0
        self.zpos = 0
        self.width = 0
        self.height = 0
        self.depth = 0
        self.scale = 0

    def project(self):
        # Translate world coordinates into camera coordinates.
        # Then return the projected coordinates.
        # This should be usable for both 2D and pseudo-3D.
        pass
