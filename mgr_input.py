#!/usr/bin/env python3

"""mgr_input

This file contains the Input Manager, used for
controlling the actions of the game, such as
assigning buttons, joysticks to each player, etc."""

# Import built-in libraries.
pass

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
pass





# Input Manager
controller = []
checktimer = 0

def setControllers():
    """Set the controller attribute to update the Joystick objects."""
    global controller
    LST_controllers = []
    if pygame.joystick.get_init():
        if pygame.joystick.get_count() > 0:
            for count in range(pygame.joystick.get_count()):
                new_controller = pygame.joystick.Joystick(count)
                new_controller.init()
                LST_controllers.append(new_controller)
    controller = LST_controllers

def checkControllers():
    """Check what controllers are available. Clean up and/or re-enable accordingly."""
    pygame.joystick.quit()
    for each in controller:
        del each
    pygame.joystick.init()
    setControllers()

def updateCheck():
    """Time a routine check for controllers existing. Call this once every loop iteration."""
    global checktimer
    checktimer += 1
    if checktimer >= 1000:
        checkControllers()
        checktimer = 0

def forceDeadzone(axis):
    """Returns a value of 0 if the axis parameter passed is too small to consider an event."""
    if abs(float(axis)) < 0.1:
        return 0.0
    else:
        pass
