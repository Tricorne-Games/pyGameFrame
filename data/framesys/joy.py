#!/usr/bin/env python



# File Docstring
"""Joy

The Joy class manages controllers used
for game input."""



# Import Materials
import pygame
from pygame.locals import *



# Joy Class
class joy(object):
    """The Joy class; to manage controller data for the game."""
    def __init__(self):
        """Initialize the Joy class."""

        # Game Controllers
        self.controller = []
        self.setControllers()

        # Controller Check
        self.checktimer = 0



    def setControllers(self):
        """Set the controller attribute to update the Joystick objects."""
        LST_controllers = []
        if pygame.joystick.get_init():
            if pygame.joystick.get_count() > 0:
                for count in range(pygame.joystick.get_count()):
                    new_controller = pygame.joystick.Joystick(count)
                    new_controller.init()
                    LST_controllers.append(new_controller)
        self.controller = LST_controllers



    def checkControllers(self):
        """Check what controllers are available. Clean up and/or re-enable accordingly."""
        pygame.joystick.quit()
        for each in self.controller:
            del each
        pygame.joystick.init()
        self.setControllers()



    def updateCheck(self):
        """Time a routine check for controllers existing. Call this once every loop iteration."""
        self.checktimer += 1
        if self.checktimer >= 1000:
            self.checkControllers()
            self.checktimer = 0



    def forceDeadzone(self, axis):
        """Returns a value of 0 if the axis parameter passed is too small to consider an event."""
        if abs(float(axis)) < 0.1:
            return 0.0
        else:
            pass