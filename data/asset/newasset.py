#!/usr/bin/env python



# File Docstring
"""Asset: NAME

The 'asset' class. An 'asset' in this game framework
is like 'objects' in any other build, such as a hero,
a platform, a player, a tile, an item, a setting, etc.
The reason I used a different name is to keep it away
from any other use of the word 'object'.

===

At your convenience, the 'sprite' class is also included
here. This is so that any and all classes that have some
form of visual representation in graphics work have their
corresponding sprite class. The sprite class only work
the visual element of a class, and are not the class
itself.

Remember to keep the 'img' and 'frm' elements of your sprite
classes handy. This allows for new instances of the sprite
to be called without having to keep working the spriter to
apply the new graphics; as the sprite class will retain the
information, game-wide."""



# Import Materials
import pygame
from pygame.locals import *

from ..framesys.audio import audio






# NOTE:
# Make sure that any asset/sprite __init__ calls only initialize the asset. Nothing else.
# Do not make it so __init__ renders the asset to playable use. This should be separate.
# This allows preparing the assets before the game is fully-loaded, so everything is ready
# the first time through the parent class. This helps from having to fetch information for
# each time a new instance of an asset or its sprite is created.

# Asset Class
class assetname(object):
	"""The Asset class. Describe it here."""

	# Sounds and sprites are written to the main class instead of an instance,
	# because this prevents needing to reload the same data for each instance.
	# Once it's set, the instance can refer to its parent class for data.
	sound = None
	sprite = None

	def __init__(self, fs):
		"""Initialize the class."""

		# Pre-load sounds.
		if assetname.sound is None:
			assetname.sound = {
				'test': fs['AUDIO'].loadFile('testsound.ogg')
			}

		# Pre-load sprite.
		if assetname.sprite is None:
			assetname.sprite = assetname.SPT(fs)


	def testSound(self):
		"""A sample method."""
		# This will play a sound with an automatically-generated Channel() object.
		assetname.sound['test'].play()

	def testMethod(self):
		"""A sample method."""
		print("TEST ASSET METHOD!")



	# If the asset will have a sprite, use this class below.
	# Non-graphic, logical assets (like a "Player" object) may not need this.
	class SPT(pygame.sprite.Sprite):
		"""The Asset's Sprite class."""

		# The same way the asset class has pre-loaded sounds and sprites, the
		# sprite objects themselves will have pre-loaded frames (image sequences),
		# to also ease the need to reload the frames on each instance. This is
		# especially useful when numerous instances of the same asset are made.

		frm = None



		# Main Sprite Functions (__init__ and update)
		def __init__(self, fs):
			"""Initialize the sprite."""
			pygame.sprite.Sprite.__init__(self) # Initialize Sprite Module.

			# All sprites will use "frames". For any sprite object that only uses one image,
			# one frame is all that is needed, and should be Frame 0.
			# The Sprite object as Pygame reads it uses 'self.image' to display a sprite frame,
			# whether static or animated. So the 6th frame of an animation during a cycle should
			# be passed through self.image to be displayed.

			# Pre-load frames.
			initsize = (16, 16) # Sample Frame Size (Change once; read elsewhere.)
			if assetname.SPT.frm is None:
				assetname.SPT.frm = fs['SPRITER'].applyFrames(fs['SPRITER'].spritesheet['cursor'],
																[((1, 1), initsize),
														 		 ((18, 1), initsize),
														 		 ((1, 18), initsize),
														 		 ((18, 18), initsize)],
													 			(255, 0, 255))

			# Standard Attributes (image & rect)
			self.image = assetname.SPT.frm[0]     # The main image displayed.
			self.rect = self.image.get_rect()     # The rect containing the sprite.

			# Auxiliary Attributes (manipulation, animation, etc.)
			self.alpha = 255 # Alpha Channel value for translucency effects.

			# Animation Attributes
			self.cf = 0           # The number to identify a 'current frame'.
			self.pause = 0        # The pause value to delay a frame of animation to the next frame.
			self.delay = 10       # The checkpoint to reset the pause value.



		def update(self):
			"""Update the sprite. This is called in sprite group update calls."""
			self.animate()                             # A sample effect called in updating.
			self.rect.topleft = pygame.mouse.get_pos() # Bring sprite rect to mouse.



		# Other Sprite Functions
		def matchRect(self):
			"""Make sure the sprite's rect matches with the sprite's image."""
			# You can call this code each time there is a change in the sprite image size.
			# This keeps the rect consistent to the image's size when using the rect.
			if self.rect != self.image.get_rect():
				self.rect = self.image.get_rect()

		def animate(self):
			"""Sample method to animate something."""
			self.pause += 1                       # Add to self.pause.
			if self.pause >= self.delay:
				self.pause = 0                    # Reset self.pause.
				self.cf += 1                      # Prepare next frame.
				if self.cf >= len(assetname.SPT.frm):
					self.cf = 0                   # Reset next frame to 0.
			self.image = assetname.SPT.frm[self.cf]        # Turn the sprite image into the frame.
			self.matchRect()