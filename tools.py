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
import mgr_video





# Camera
class Camera(object):
    """The Camera class."""
    def __init__(self):
        """Initialize the Camera."""
        self.rect = mgr_video.rect # Camera rect should be same dimensions as display rect.

    def translateXY(self, targetrect):
        """Measure the camera's rect from the target's rect, and return the offset."""
        # The top-left corner of rects is usually what's used for blitting.
        # [0] is x, [1] is y.
        newx = self.rect.topleft[0] - targetrect.topleft[0]
        newy = self.rect.topleft[1] - targetrect.topleft[1]
        # Now, this is only the difference. It still needs to be offset from
        # display, which uses Cartesian coordinates, where origin is top-left,
        # Y+ going downward, so we return the negative values for offset.
        return (-newx, -newy)
