#!/usr/bin/env python



# File Docstring
"""Scene: NAME

This scene file is used as a template to create
different scenes in the game. Describe what it
would do here."""



# Import Materials
import pygame
from pygame.locals import *

from asset.newasset import *



# Scene Class
class SCN_new(object):
	"""The new scene class."""

	def __init__(self):
		"""Initialize and prepare the scene."""

		# Scene Class Attributes
		pass



	def start(self, fs):
		"""Start the scene."""

		# Loop-Local  Variables
		pass

		# Location-Specific Updating
		# LSU is optional! It's good for saving memory on updating the screen in the specific circumstance of a
		# non-animated background, because it simply covers old sprite locations instead of flushing
		# out the entire screen. But its limitation is of course needing a static background to do that. It is
		# perfect for really simple arcade-style games or really retro-inspired games (think Pong).
		# Unless you know what you're doing with it to make a game to run on this technique.
		#
		# To use location-specific updating, you must first have a list ready to collect old rects,
		# then make a dedicated static background, then blit the background to the display surface,
		# and lastly call an update to the display.
		#
		# Don't forget to set up the render() parameters to operate LSU. Otherwise it renders normally.
		LST_rectchange = []                                 # List to store used sprite rects.
		canvas = pygame.Surface(fs['VIDEO'].size).convert() # A background canvas.
		canvas.fill((255, 255, 255))                        # Fill the canvas.
		fs['VIDEO'].disp.blit(canvas, (0, 0))               # Blit the canvas to the display.
		fs['VIDEO'].show()                                  # Show.

		# Sprite Group Dictionary
		# Add the sprites to these directly in later code.
		# Below is a dictionary to simplify pointing to a specific sprite group.
		DIC_spritegroup = {
			'sample': pygame.sprite.RenderUpdates()
		}
		# Sprite Group List
		# This orders the sprite groups in the sprite group dictionary above.
		# 0-N; where 0 is backmost, closest depth to background. N is foremost, closest depth to player.
		LST_spritegroup = [
			DIC_spritegroup['sample']
		] # Sample Group

		# Game Objects
		x = assetname(fs)

		# Prepare Scene
		pygame.mouse.set_visible(False)
		LST_spritegroup[0].add(x.sprite)






		# Scene Loop
		pygame.event.get() # Purge Input Queue
		fs['CLOCK'].tick(fs['VIDEO'].fps)

		SL = True # Scene Loop Switch
		while SL == True:
			# FRAMERATE HANDLING
			# Maintain framerate and variables before handling and executions.
			dt = float(fs['CLOCK'].tick(fs['VIDEO'].fps)) # Lock framerate and return milliseconds since last tick() as delta-time.
			if dt > 1000.0 / fs['VIDEO'].fps:
				dt = 1000.0 / fs['VIDEO'].fps             # Cap delta-time at the maximum amount of milliseconds per frame.
				fs['VIDEO'].df = dt / 1000.0              # Convert delta-time to delta-frame, for frame-independent motion.



			# EVENT HANDLING
			# Invoke any events and changes triggered by the user.
			pygame.event.pump() # Pump event queue to prevent lock-up if no event calls are passed.
			for evt in pygame.event.get():
				if evt.type is QUIT:
					return 'EXIT GAME'
				elif evt.type is KEYDOWN:
					if evt.key == K_ESCAPE:
						SL = False

			keypress = pygame.key.get_pressed()
			if keypress[K_a]:
				# Random method to test the asset.
				x.testMethod()
			elif keypress[K_s]:
				# Test the asset's sound directly.
				# This will play on as many channels that are available as the sound is called.
				x.testSound()
			elif keypress[K_d]:
				# Plays the Sound() object strictly in a specific channel.
				# Because each channel can only play one sound at a time, this clears up when used again.
				fs['AUDIO'].playChannel('c1', assetname.sound['test'])
			elif keypress[K_f]:
				# Plays music in a channel.
				fs['AUDIO'].playChannel('music', fs['AUDIO'].song['testsong'], 3)



			# DATA RENDERING
			# Update game logic, such as a position, an ability, a change, etc.
			pass



			# SCREEN RENDERING
			# Take all image data and place them accordingly.
			fs['VIDEO'].render(LST_spritegroup, LST_rectchange, canvas, color=(127, 127, 127))


		# Clean-Up
		return 'END SCENE' # End