#!/usr/bin/env python



# File Docstring
"""Audio

This is the Audio class. It manages the layout
and use of the sound, channels, music, etc."""



# Import Materials
import os

import pygame
from pygame.locals import *



# Audio Class
class audio(object):
	"""The Audio class; to handle sound management."""

	assetpath = 'data\\asset\\'
	channel = None
	song = None

	def __init__(self):
		"""Initialize the Audio system."""

		# Make sure the Mixer is ready.
		if not pygame.mixer or not pygame.mixer.get_init():
			self.loadMixer()

		# Played sounds return a Channel object. These are like "layers" for sounds.
		# You can play sounds into a specific channel with: Channel().play(Sound())
		# Channels are generated and handled as necessary by the mixer on their own,
		# and there are 8 by default, but this allows for finer control of the sounds played.
		# (For example, using stereo-pan on a specific channel because the sound
		# was generated at a specific location on the screen.)
		if audio.channel is None:
			audio.channel = {
				'music': self.newChannel(0),
				'c1': self.newChannel(1)
			}

		# Below stores the music files as Sound() objects for use.
		if audio.song is None:
			audio.song = {
				'testsong': self.loadFile('testsong.ogg')
			}

	def loadMixer(self, fq=44100, sz=16, ms=2, bf=4096):
		"""Shuts down and restarts the mixer with new settings."""
		# fq = Frequency
		# sz = Size (-sz are signed samples.)
		# ms = Mono/Stereo (1 for Mono, or 2 for Stereo.)
		# bf = Buffer (Value must always be a power of 2.)
		pygame.mixer.quit()
		pygame.mixer.init(fq, sz, ms, bf)



	def loadFile(self, filename):
		"""Returns a Sound class. Used for either sound effects or music."""
		filepath = os.path.join(audio.assetpath, filename) # Concatenate the file path.
		soundfile = pygame.mixer.Sound(filepath)           # Retrieve the Sound file as a Sound() object.
  		return soundfile                                   # Return the Sound() object.



	def newChannel(self, channel_id):
		"""Creates a new channel."""
		return pygame.mixer.Channel(channel_id)



	def playChannel(self, channel, item, loops=0, maxtime=0, fade_ms=0):
		"""Plays an item, such as a song or item, into a channel to play."""
		# The 'channel' parameter is the 'key' from the audio.channel dictionary.
		# The 'item' parameter is any Sound() object to play.
		audio.channel[channel].play(item, loops, maxtime, fade_ms)



	def stopChannel(self, channel):
		"""Stops the channel from playing."""
		audio.channel[channel].stop()



	# Auxiliary
	def stereo_pan(self, x_coord, screen_width):
		"""Return volume values for a channel, to enable a stereo-panning effect."""
		right_volume = float(x_coord) / screen_width
		left_volume = 1.0 - right_volume
		return left_volume, right_volume