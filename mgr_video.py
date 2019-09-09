#!/usr/bin/env python3

"""mgr_video

This file acts as the Video Manager.
It controls the display and its settings."""

# Import built-in libraries.
import os

# Import supplementary libraries.
import pygame
from pygame.locals import *

# Import local modules.
from uevents import uEvent





# Video Manager
display = None
rect = None
icon = None
iconpath = 'game.ico'
size = (1024, 768)
fps = 60
df = 0 # Delta-Frame - Used for frame-independent motion.
clock = pygame.time.Clock()
bitdepth = 0 # Bit Depth (0 = Desktop Depth)
resize_buffer = None

os.environ['SDL_VIDEO_CENTERED'] = '1'

fs_sets = (
    (FULLSCREEN),
    (FULLSCREEN|HWSURFACE),
    (FULLSCREEN|HWSURFACE|DOUBLEBUF)
)

def showSplashScreen(path, seconds=3):
    """Create a splash screen display."""
    pygame.display.init()
    IMG_splash = pygame.image.load(path)
    RCT_splash = IMG_splash.get_rect()
    splash = pygame.display.set_mode(RCT_splash.size, NOFRAME)
    splash.blit(IMG_splash, (0, 0))
    pygame.display.flip()
    pygame.time.wait(seconds * 1000)
    pygame.display.quit()
    del RCT_splash
    del IMG_splash

def showMainScreen(title):
    """Open up the main screen display."""
    global display, icon, size, rect
    pygame.display.init()
    pygame.display.set_caption(title)
    display = pygame.display.set_mode(size, HWSURFACE|DOUBLEBUF)
    icon = getIconData(iconpath)
    pygame.display.set_icon(icon)
    rect = display.get_rect()

def getIconData(icon_name, size=(32, 32), colorkey=(255, 0, 255), scalekey=(32, 32)):
    """Prepares and returns icon data to use on the frame corner."""
    if size[0] > 32 or size[1] > 32:
        print("WARNING: Given window icon size dimensions are too large.")
        return
    icon_image = pygame.image.load(icon_name)
    icon_rect = icon_image.get_rect()
    icon_done = pygame.Surface(size)
    icon_done.set_colorkey(colorkey)
    for x in range(size[0]):
        for y in range(size[1]):
            icon_done.set_at((x, y), icon_image.get_at((x, y)))
    icon_done = pygame.transform.scale(icon_done, scalekey)
    return icon_done
    
def handleFramerate():
    """Handles the framerate sequence and prepares delta-frame."""
    global clock, fps, df
    dt = float(clock.tick(fps)) # Delta-Time. Also should call clock.tick().
    cap = 1000.0 / fps # Set framerate cap.
    if dt > cap:
        dt = cap
    # Set delta-frame for frame-independent motion.
    df = dt / 1000.0
    # Post a tick event.
    pygame.event.post(uEvent['Tick'])

def showFrame(changerects):
    """Display the newly-rendered frame."""
    if len(changerects) > 0:
        # Update by passing a rectlist for static backgrounds.
        pygame.display.update(changerects)
    else:
        # Flip the buffer.
        pygame.display.flip()

def flushBuffer(color=(0, 0, 0)):
    """Wipes the buffer entirely."""
    display.fill(color)
