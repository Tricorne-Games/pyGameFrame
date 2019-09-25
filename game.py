#!/usr/bin/env python3

"""game

This file contains the function that prepares
the game resources and runs the game."""

# Import built-in libraries.
import os
import sys

# Import supplementary libraries.
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
from pygame.locals import *

# Import local modules.
import mgr_video
import mgr_audio
import mgr_input
import mgr_scene
import mgr_sprite

from uevents import uEvent





# Constants
name = "Untitled"
version = 'v0'
date = 'DATE'
author = "AUTHOR"

def showDetailsConsole():
    """A quick text script to display information in the console when starting."""
    # NOTE: This will not show up if the main script is a .pyw file.
    
    global name, version, date, author
        
    output = name + """ - """ + version + """
""" + date + """ """ + author + """

This is an example of what the console would output when the game runs.
You can form this and above text however you like.

Alternatively, you can make the main execution script have a .pyw
extension instead, and that will disable the console from popping up
before the game."""
    print(output)
    print('')    

def run():
    """Run the game."""
    global name

    # Show Details (Console)
    showDetailsConsole()
    
    # Start Pygame
    pygame.init()

    # Splash Screen
    mgr_video.showSplashScreen('splash.png')

    # Prepare Managers
    mgr_video.showMainScreen(name) # Show display.
    mgr_video.clock.tick()
    mgr_audio.preinitMixer()
    mgr_audio.loadMixer()
    mgr_audio.setChannels()
    mgr_audio.setSongs()
    mgr_input.setControllers() # Set up controllers if any.
    mgr_scene.setScenes()
    #mgr_sprite for spritesheets.

    # Starting Scene
    mgr_scene.currentScene = mgr_scene.scene['G']()

    # Core Loop
    loop_active = True
    while loop_active is True:
        # Handle Framerate/Delta-Frame
        mgr_video.handleFramerate()

        # Input Tracking
        mgr_input.updateCheck()

        # Scene Tracking
        if mgr_scene.currentScene.nextScene == 'TERMINATE':
            loop_active = False
        elif mgr_scene.currentScene.nextScene == 'CURRENT':
            pass
        else:
            # NOTE: The game will crash if a non-existent scene is called.
            mgr_scene.swap = mgr_scene.currentScene.nextScene
            mgr_scene.currentScene = mgr_scene.scene[mgr_scene.swap]
            mgr_scene.currentScene.nextScene = 'CURRENT'
            mgr_scene.swap = ''

        # Event Tracking
        pygame.event.pump()
        filtered_events = []
        for eachEvent in pygame.event.get():
            if eachEvent.type == QUIT:
                loop_active = False
            else:
                filtered_events.append(eachEvent)

        # Cycle Scene
        mgr_sprite.changerects = [] # Clear changerects from any scenes that use RenderUpdates.
        mgr_scene.currentScene.process(filtered_events)
        mgr_scene.currentScene.update()
        mgr_scene.currentScene.render(mgr_video.display)
        
        # Display Frame
        mgr_video.showFrame(mgr_sprite.changerects)

    # Close
    pygame.quit()
    sys.exit(0)
