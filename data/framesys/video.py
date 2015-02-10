#!/usr/bin/env python



# File Docstring
"""Video

The device used to display the game's visual elements.

Note that while Pygame can handle the display material by itself,
this object was created to contain some of the essentials in handling
the screen, such as the show() method, which determines the proper
way to show the next frame."""



# Import Materials
import pygame
from pygame.locals import *


# Video Class
class video(object):
	"""The Video class; contains material to help streamline display management."""

	def __init__(self, caption='UNTITLED', size=(800, 600), fps=60):
		"""Initialize the Video system."""
		# Display Attributes
		self.disp = None                                             # Display Window
		self.caption = caption                                       # Caption (Window Title)
		self.icon = ('data\\framesys\\disp_icon.ico', (255, 0, 255)) # Icon
		self.disp_sets = 0                                           # Display Settings (You can also use RESIZABLE or NOFRAME instead of 0.)*
		self.bits = 0                                                # Bit Depth (0 = Desktop Depth)
		self.size = size                                             # Screen Size/Resolution/Dimensions
		self.fps = fps                                               # Framerate (Frames Per Second)

		# NOTE ON RESIZING THE SCREEN
		# Only use RESIZABLE if you absolutely intend to have your game window resizable, and know what you're doing.
		# Locking the window size keeps everything in the window in a constant form, especially if full-screen toggling.
		#
		# To resize, you must pass the VIDEORESIZE event from a scene's event queue as a parameter in resize().
		#
		# Also, the os.environ['SDL_VIDEO_CENTERED'] = '1' in the main game file will have the resized window centered.
		# You can remove this at will, but it was put to help keep the screen centered, especially for the splash-screen.

		# Full-Screen Settings
		self.fs_sets = (FULLSCREEN|HWSURFACE|DOUBLEBUF) # Variable to switch disp_sets quickly and fully.
		self.fs_switch = None # Flag to determine if screen is full or not.
		if self.disp_sets == 0:
			self.fs_switch = False
		elif self.disp_sets != 0:
			self.fs_switch = True
		# You can also use:
		# pygame.display.get_surface().get_flags() & pygame.FULLSCREEN
		# But using a boolean switch that's automated in toggling may help.



	def splashscreen(self, seconds=2):
		"""Start a temporary splash screen for set amount of seconds. Call and kill before using build()."""
		IMG_splash = pygame.image.load('data\\framesys\\splashscreen.png')
		RCT_splash = IMG_splash.get_rect()
		splash = pygame.display.set_mode(RCT_splash.size, NOFRAME)
		pygame.mouse.set_visible(False)
		splash.blit(IMG_splash, (0, 0))
		pygame.display.update()
		pygame.time.wait(seconds * 1000)
		pygame.display.quit()
		del IMG_splash, RCT_splash
		pygame.display.init()                                      # Resumes pygame.display to continue.



	def mainscreen(self):
		"""Start the main screen."""
		self.disp = pygame.display.set_mode(self.size, self.disp_sets, self.bits) # Activate Display
		pygame.display.set_caption(self.caption)                                  # Set Caption
		pygame.display.set_icon(self.icon_data(self.icon[0], self.icon[1]))       # Set Icon
		self.size = self.disp.get_size()                                          # Set Size
		self.rect = self.disp.get_rect()                                          # Set Rect
	# The method below is used strictly for the method above. It sets up the window icon.
	def icon_data(self, icon_name, colorkey=(255, 0, 255)):
		"""Prepares an icon to use on the display window's corner."""
		icon_image = pygame.image.load(icon_name)                   # Icon Image (Surface)
		icon_done = pygame.Surface((32, 32))                        # New Surface
		icon_done.set_colorkey(colorkey)                            # Transparency Colorkey
		for x in range(32):                                         # X Coordinate Pixels
			for y in range(32):                                     # Y Coordinate Pixels
				icon_done.set_at((x, y), icon_image.get_at((x, y))) # Transfer Pixels
		return icon_done                                            # Return Value



	# Active Methods
	def render(self, spgr, changerects=None, bg=None, color=(0, 0, 0)):
		"""Main frame-render loop."""
		self.clear(spgr, changerects, bg, color)   # Clear
		self.update(spgr)                          # Update
		rectchanges = self.draw(spgr, changerects) # Draw
		self.show(rectchanges)                     # Show

	def clear(self, spgr, changerects=None, bg=None, color=(0, 0, 0)):
		"""Flush the screen for a new draw."""
		# This first step is best for games that use a static playing area.
		# It clears out only the specific areas where active sprites are located.
		if type(changerects) is list and type(bg) is pygame.Surface:
			for group in spgr:
				group.clear(self.disp, bg)
		# This second step is best for games where everything including the background is animated.
		# It wipes the entire screen surface to one color before putting in new image updates.
		else:
			self.disp.fill(color)

	def update(self, spgr):
		"""Calls update() in each sprite group's sprites."""
		for group in spgr:
			group.update()

	def draw(self, spgr, changerects=None):
		"""Draws the updated sprites."""
		# When using a static background, this forms a list of the rect of every sprite being drawn.
		if type(changerects) is list:
			changerect = []                               # List of rects to change.
			for group in spgr:
				changerects.extend(group.draw(self.disp)) # With each draw, increase the list.
			return changerects
		# Otherwise, if no list will be returned, just draw the sprites in.
		else:
			for group in spgr:
				group.draw(self.disp)
			return None

	def show(self, changerects=None):
		"""Updates the display with new screen information, depending on the display information."""
        # Flip buffers when in full-screen (Same as update(), but useful specifically for full-screen.)
		if self.fs_switch is True or pygame.display.get_surface().get_flags() & pygame.FULLSCREEN:
			pygame.display.flip()
		# If the game is not in full-screen, use update() instead.
		else:
            # Update location-specific sprite rects (if the background will not change).
			if type(changerects) is list:
				pygame.display.update(changerects)
            # Update normally anyway. (Same as flip(); simply updates.)
			else:
				pygame.display.update()



	# Auxiliary Methods
	def toggleFullscreen(self):
		"""Toggles full-screen display."""
		if self.fs_switch is False:
			self.fs_switch = True
			self.disp = pygame.display.set_mode(self.resolution, self.fs_sets, self.bits)
		elif self.fs_switch is True:
			self.fs_switch = False
			self.disp = pygame.display.set_mode(self.resolution, self.disp_sets, self.bits)

	def resize(self, event):
		"""Resizes and redefines the screen."""
		newsize = event.size # New size, from resizing event...
		self.disp = pygame.display.set_mode(newsize, RESIZABLE, self.bits) # New Display Mode
		self.size = self.disp.get_size() # Display Size
		self.rect = self.disp.get_rect() # Display Rect