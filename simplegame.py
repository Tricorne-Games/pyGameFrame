#!/usr/bin/env python



# File Docstring
"""Simple Game

This is a one-file project that runs a very simple game framework.
It is best used for only the simplest games, or as a testing ground."""



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

	def run(self):
		"""Execute and run the game."""

		# Set-Up
		pygame.mixer.pre_init(44100, 16, 2, 4096) # Pygame Mixer Presets (freq, size, mono/stereo, buffer)
		pygame.init()                             # Initialize Pygame
		os.environ['SDL_VIDEO_CENTERED'] = '1'    # Center Displays

		# Screen
		SCREEN = pygame.display.set_mode((550, 400))
		RCT_SCREEN = SCREEN.get_rect()
		pygame.display.set_caption(self.name)

		# Terminal
		CLOCK = pygame.time.Clock()
		FPS = 30 # Frames Per Second
		TEXT = pygame.font.SysFont(pygame.font.get_default_font(), 100)

		# Canvas & Flush Tools
		CANVAS = pygame.Surface(SCREEN.get_size()).convert() # Surface to represent a static background.
		CANVAS.fill((255, 255, 255))                         # Colors the Canvas surface.
		FLUSH = pygame.Surface(SCREEN.get_size()).convert()  # Surface that wipes the buffer for full-screen refresh.
		FLUSH.fill((0, 0, 255))                              # Colors the Flush surface.
		LST_rectchange = None                                # Use None = Full-Screen Update / Use [] = Location-Specific Update

		# Sprite Groups
		# This collects your sprites in sprite groups to be called for updates in a sequence.
		#
		# Sprite Key - A simple list of the names for each sprite group to be used as keys in the dictionary.
		# Put these in a specific order for the LST_spritegroup to use, when rendering from back to front.
		# 0-N; where 0 is backmost, closest depth to background. N is foremost, closest depth to player.
		KEY_spritegroup = [
			'sample'
		]
		# Sprite Dictionary - A dictionary of the sprite groups, to simplify calling a specific group by key.
		DIC_spritegroup = {}
		# Sprite List - A List of the groups in the dictionary, to use for sprite updating. Also in specific order.
		LST_spritegroup = []
		# This loop compiles both the DIC and the LST in the order written in KEY.
		for eachkey in KEY_spritegroup:
			DIC_spritegroup[eachkey] = pygame.sprite.RenderUpdates()
			LST_spritegroup.append(DIC_spritegroup[eachkey])





		# Sprites
		class speck(pygame.sprite.Sprite):
			"""A test sprite that follows the cursor and changes color."""
			def __init__(self):
				"""Initialize sprite assets."""
				pygame.sprite.Sprite.__init__(self)
				self.image = pygame.Surface((32, 32)).convert()
				self.rect = self.image.get_rect()

				self.df = 0
				self.speed = 150.0
				self.rgb = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
				self.colorstate = [random.choice(['+', '-']), random.choice(['+', '-']), random.choice(['+', '-'])]

			def update(self):
				"""Update call during rendering."""
				# Test to bring Sprite to mouse position.
				#self.rect.center = pygame.mouse.get_pos()

				# Change sprite's color.
				self.colorchange()

			def colorchange(self):
				"""Change the color of the sprite."""
				for i in range(2):
					newval = self.rgb[i]
					if self.colorstate[i] == '+':
						newval += random.randrange(0, 20)
					elif self.colorstate[i] == '-':
						newval -= random.randrange(0, 20)
					if newval > 255:
						newval = 255
						self.colorstate[i] = '-'
					elif newval < 0:
						newval = 0
						self.colorstate[i] = '+'
					self.rgb[i] = newval
				self.image.fill((self.rgb[0], self.rgb[1], self.rgb[2]))

			def move(self, direction, rate):
				"""Move the sprite."""
				if direction == 'L':
					self.rect = self.rect.move(-self.speed * rate, 0)
				if direction == 'R':
					self.rect = self.rect.move(self.speed * rate, 0)





		# Prepare Scene
		SCREEN.blit(CANVAS, (0, 0)) # Set a surface to the display.

		x = speck()                       # Create a sprite instance.
		x.rect.center = RCT_SCREEN.center # Align sprite.
		LST_spritegroup[0].add(x)         # Add sprite to sprite group.

		pygame.display.update() # Establish and display screen.





		# Core Loop
		pygame.event.get() # Purge Event Queue
		CLOCK.tick(FPS)    # Establish Framerate (for first iteration)

		CL = True # Core Loop Switch
		while CL == True:
			# FRAMERATE HANDLING
			# Maintain framerate and variables before handling and executions.
			dt = float(CLOCK.tick(FPS)) # Lock framerate and return milliseconds since last tick() as delta-time.
			if dt > 1000.0 / FPS:
				dt = 1000.0 / FPS       # Cap delta-time at the maximum amount of milliseconds per frame.
			df = dt / 1000.0            # Convert delta-time to delta-frame, for frame-independent motion.
			# Assign the video() delta-frame to all sprites.
			for eachgroup in LST_spritegroup:
				for eachsprite in eachgroup.sprites():
					eachsprite.df = df


			# EVENT HANDLING
			# Invoke any events and changes triggered by the user.
			pygame.event.pump() # Pump event queue to prevent lock-up if no event calls are passed.
			for evt in pygame.event.get():
				if evt.type is QUIT:
					CL = False
				elif evt.type is KEYDOWN:
					if evt.key == K_ESCAPE:
						CL = False

			keypress = pygame.key.get_pressed()
			if keypress[K_e]:
				x.move('L', df)
			if keypress[K_d]:
				x.move('R', df)


			# DATA HANDLING
			# Apply game logic and changes triggered by the game.
			pass


			# SCREEN RENDERING
			# Take all image data and place them accordingly.

			# Note: Location-Specific Updating is only useful if your background surface
			# is not animated or moving. It does so by only updating specific locations
			# against the background surface as-is instead of flushing the entire screen.
			#
			# In this template file, there is technically no point in using FLUSH, then CANVAS.
			# Both are simply surfaces and they are being applied twice here. Either can easily
			# be used as a flush and background before redrawing sprites. The reason I have both
			# is to demonstrate that using location-specific updating doesn't need a full flush.
			# But it does need a static background underneath the sprites to cleanly render.
			# You can try disabling the first pygame.display.update() before the core loop to see
			# an example of the background area being trailed where the sprite was earlier located.
			#
			# If you blit the FLUSH surface but not the CANVAS surface, you will see the FLUSH
			# surface. If you left both on, only CANVAS will show, because it blits after FLUSH.
			# Ideally, you'd flush everything out before drawing on a buffer first, but there's not
			# much point in doing that if you can place a background surface to start the new frame.

			# - Clear [Wipe the screen to prevent trailing graphics.]
			if type(LST_rectchange) == list:
				for group in LST_spritegroup:
					group.clear(SCREEN, CANVAS)
			else:
				SCREEN.blit(FLUSH, (0, 0))   # Apply FLUSH to buffer.
				#SCREEN.blit(CANVAS, (0, 0)) # Apply CANVAS to buffer.

			# - Update [Incur sprite update calls.]
			for group in LST_spritegroup:
				group.update()

			# - Draw [Blit the new data to the display.] {Draw Back to Front!}
			if type(LST_rectchange) == list:                  # Location-Specific Blitting
				LST_rectchange = []                           # Reset for the new rect changes.
				for group in LST_spritegroup:
					LST_rectchange.extend(group.draw(SCREEN)) # Compile the rect changes and draw accordingly.
			else: # Normal Flush/Draw Blitting
				for group in LST_spritegroup:
					group.draw(SCREEN)

			# - Show [Present the new display.]
			if pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
				pygame.display.flip()                     # Update the screen (flip() is the same as update() but useful for fullscreen).
			else:
				if type(LST_rectchange) == list:
					pygame.display.update(LST_rectchange) # Update the screen, using the location-specific areas.
				else:
					pygame.display.update()               # Update the screen.


		# Clean-Up
		pygame.quit() # Close Pygame
		return 'END'  # End





# Main Program
if __name__ == '__main__':

	# Import Materials
	# Python Standard Packages
	import datetime
	import math
	import os
	import pickle
	import random
	import sys
	import time

	# Third-Party Packages
	import pygame
	from pygame.locals import *

	# Game-Specific Packages
	pass



	# Game
	G = game()  # Itemize Game
	G.run()     # Run Game (until core loop ends)
	sys.exit(0) # Complete Exit
