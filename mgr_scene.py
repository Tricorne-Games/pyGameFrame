#!/usr/bin/env python3

"""mgr_scene

This file contains the Scene Manager, used for
controlling the flow of game scenes, such as
title screen, pause menus, in-game action,
levels, etc."""

# Import built-in libraries.
pass

# Import supplementary libraries.
pass

# Import local modules.
from scn_a import SceneA # Swap Scene Page 1
from scn_b import SceneB # Swap Scene Page 2
from scn_c import SceneC # Swap Scene Nonexistent
from scn_d import SceneD # User Event Test Scene
from scn_e import SceneE # Test Sprite Groups
from scn_f import SceneF # Test Location-Specific Sprite Updating
from scn_g import SceneG # Test camera scrolling.





# Scene Manager
scene = {}
currentScene = ''
swap = ''

def setScenes():
    """Prepares each of the scenes in the scene dictionary."""
    # NOTE: It is important that this function be called
    # separately, when preparing the game to set up the scenes,
    # rather than explicitly write them in the dictionary above,
    # as scenes may require the display to be initialized to use
    # convert() calls for all surfaces used, including sprites.
    global scene
    scene = {
        'A':SceneA,
        'B':SceneB,
        'C':SceneC,
        'D':SceneD,
        'E':SceneE,
        'F':SceneF,
        'G':SceneG
    }
