#!/usr/bin/env python



# File Docstring
"""Game

This is the main script that encapsulates all of the game data,
reads it to prepare for action, and finally renders the game."""



# Game Class
class game(object):
	"""The 'game' class, to encapsulate the game data and system."""

	# Game Information
	name = 'UNTITLED GAME' # Game Name
	version = 'v0'         # Build Version
	date = 'DATE'          # Date the game was made.
	author = 'AUTHOR'      # Creator of the game.

	def __init__(self):
		"""Initialize an instance of the game object. You can pass game-specific variables here."""
		pass

	def console_detail(self):
		output = """UNTITLED GAME - v0
DATE AUTHOR

This is an example of what the console would put out when the game runs.
You can form this and above text however you like.

Alternatively, you can make this file have a .pyw extension instead, and
that will disable the console from popping up before the game."""
		print(output)
		print('')


	def run(self):
		"""Execute and run the game."""

		# Start-Up
		self.console_detail() # The console will not show if this file is a .pyw extension.

		# Initialize Pygame and System Settings
		# This prepares the background settings the game will run with.
		pygame.mixer.pre_init(44100, 16, 2, 4096) # Pygame Sound Mixer Presets (freq, size, mono/stereo, buffer)
		pygame.init()                             # Initialize Pygame Library
		os.environ['SDL_VIDEO_CENTERED'] = '1'    # Center Window Display


		# Framework System Setup
		# This is a dictionary of the different components the game can call on to do its
		# back-end work to help run the game, such as multimedia, framerate, networking, etc.
		#
		# Each of the dictionary values here are all objects inside the 'framesys' folder,
		# and have a specific set of operations as components:
		# VIDEO handles the screen/display.
		# AUDIO handles the sounds/music.
		# JOY handles the joystick/controller systems if the game will use them.
		# SPRITER handles the creation and formatting of sprite graphics.
		# CLOCK handles the Pygame clock system, for things like framerate.
		# FONT handles a system font for basic uses.
		FS = {
			'VIDEO':   video(),
			'AUDIO':   audio(),
			'JOY':     joy(),
			'SPRITER': spriter(),
			'CLOCK':   pygame.time.Clock(),
			'FONT':    pygame.font.SysFont(None, 12)
		}

		# Start Application
		FS['VIDEO'].splashscreen(2)       # Show Splashscreen (OPTIONAL)

		FS['VIDEO'].mainscreen()          # Show Main Screen
		FS['CLOCK'].tick(FS['VIDEO'].fps) # Establish Framerate
		pygame.event.get()                # Purge Event Queue

		# Load Game Assets
		# Prepare all of the game assets before running the game.
		# This makes it so new data, such as sprite instances, are produced
		# without loading them the first time during the game.
		# If this will be a long list, consider using a separate module.
		FS['SPRITER'].loadSpritesheets()
		assetname(FS)

		# Core Loop
		# This starts up the game and keeps it open as an application.
		CL = True # Core Loop Switch
		while CL == True:
			FS['CLOCK'].tick(FS['VIDEO'].fps) # Maintain Framerate
			pygame.event.pump()               # Pump events to prevent lock-up when no events pass.



			# Scene Tree
			# In a game, you are seeing in scenes, such as Main Menu, Character Select, etc.
			# This section of the loop maps the navigation between scenes during the game.
			# For example, a Main Menu scene could be the first scene. When an option is selected,
			# it returns a value or more that this section will interpret to point to the next scene,
			# and with the appropriate data if applicable.
			newscene = SCN_new()                                           # New Scene
			ROU_newscene = newscene.start(FS)                              # Start the scene, wait for a route value.
			if ROU_newscene == 'END SCENE' or ROU_newscene == 'EXIT GAME':
				CL = False                                                 # End the Core Loop immediately.
			else:
				pass



		# Clean-Up
		pygame.quit()     # Close Pygame
		return 'END GAME' # End Run





# Main Program
if __name__ == '__main__':

	# IMPORT GAME RESOURCES
	# Python Standard Packages
	import __init__
	import pickle
	import os
	import sys

	import math
	import random

	import time
	import datetime

	# Third-Party Packages
	import pygame
	from pygame.locals import *

	# Framework System
	from data.framesys.video import *
	from data.framesys.audio import *
	from data.framesys.joy import *
	from data.framesys.spriter import *

	# Game Scenes
	from data.newscene import *

	# Game-Specific Packages
	from data.asset.newasset import *



	# GAME
	game().run() # Start Game
	sys.exit(0)  # Exit Game