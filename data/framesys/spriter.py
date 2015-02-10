#!/usr/bin/env python



# File Docstring
"""Spriter

This module contains the spriter class, which can be used
to create and manage sprite graphics. For best results, use
.png files, as they can use alpha channels, and are portable.

Think of the spriter as a machine that is fed a graphic, and it
has the equipment that can cookie-cut the graphic and apply them
wherever necessary in the program; even if it's the entire graphic.

Remember to keep the 'img' and 'frm' elements of your sprite objects
handy. This allows for new instances of the sprite to be called
without having to keep reworking the spriter to apply the new graphics;
as the sprite object will retain the information, game-wide."""



# Import Materials
import os

import pygame
from pygame.locals import *



# Spriter Class
class spriter(object):
	"""The Spriter class; used to manage sprite images."""

	assetpath = 'data\\asset\\'
	spritesheet = None

	def __init__(self):
		"""Initalize the Spriter system."""
		pass


	def setSpritesheet(self, filename, A=False):
		"""Return a spritesheet surface."""

		# Concatenate File Path
		filepath = os.path.join(spriter.assetpath, filename)

		if A == True:
			return pygame.image.load(filepath).convert_alpha() # Make the spritesheet alpha-enabled.
		else:
			return pygame.image.load(filepath).convert()       # Make a normal spritesheet.



	def loadSpritesheets(self):
		"""Prepare all spritesheets. This is used after the video display is set."""
		if spriter.spritesheet is None:
			spriter.spritesheet = {
				'cursor': self.setSpritesheet('testspritesheet.png')
			}



	def setColorkey(self, image, colorkey):
		"""Set a colorkey for transparency. Use (R, G, B) for the colorkey."""
		# IF AN ALPHA CHANNEL IS INVOLVED, PUT IT INTO ACCOUNT HERE!
		if colorkey == 0:
			colorkey = image.get_at((0, 0))           # Set colorkey to Top-Left pixel's color if 0 is passed.
		image.set_colorkey(colorkey, pygame.RLEACCEL) # Establish the colorkey.



	def applyGraphic(self, sst, rect, colorkey=None, A=False):
		"""Return a section of the spritesheet to apply a sprite graphic."""
		selection = pygame.Rect(rect)                                # Selection rect (location/size on spritesheet) to select sprites.
		if A == True:
			graphic = pygame.Surface(selection.size).convert_alpha() # A new alpha graphic surface.
		else:
			graphic = pygame.Surface(selection.size).convert()       # A normal graphic surface.
		graphic.blit(sst, (0, 0), selection)                         # Draw the selected graphic onto the new surface.
		if colorkey is not None:
			self.setColorkey(graphic, colorkey)
		return graphic                                               # Return the graphic.



	def applyFrames(self, sst, rect_list, colorkey=None, A=False):
		"""Return a list of graphics to use for frames."""
		frames = []                                                  # An empty list to hold the frames.
		for rect in rect_list:
			frames.append(self.applyGraphic(sst, rect, colorkey, A)) # Append the graphic to the list.
		return frames                                                # Return the frame list.