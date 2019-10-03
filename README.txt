pyGameFrame - Pygame Project Template
By Tricorne Games
9-8-2019

pyGameFrame is a template package designed to help you getting to programming your own games in the Pygame system right away. A lot of the gruntwork is taken care of to ensure the ease of use and to make sure all the properties necessary are assembled together for the most efficient use of the Pygame platform. It is meant to be torn and retooled to your needs without having to write everything from scratch, and for what you do leave alone, everything is specially prepared, such as convert() calls for graphics, a delta-frame variable for frame-independent motion, using an MVC model, a scene management system, a .ico file for your own window corner icon, a "main" script that most games use formally, and more.

This version of pyGameFrame is not much different from its predecessor. The major change is where everything including the game itself was an object that could be instantiated, it is now so that any component where there should ever only be one instance anyway (including the game itself and its managers) have been retooled into being the modules themselves that contain them, for cleanliness (thus a lot less "self" calls and making parameters out of everything).

Here are the files used to make this package:

main.py - The file that calls and executes the game as a main file.

bases.py - Base component objects get defined here.

tools.py - A place for tools to be used such as the included Camera() object, or anything else you want, like algorithms.

game.ico - The icon you see in the top-left corner of the game window, if using a windowed display. The Video Manager has a function that specially prepares this when calling the display window, so all you would really need to change is this icon specifically. Maximum size is 32x32.

game.py - The main game setup and loop function.

mgr_audio.py - The Audio Manager. Anything involving work with the audio, such as channels, music, sound effects, etc. should go here.

mgr_input.py - The Input Manager. Anything involving inputs such as keyboard, mouse, controllers, etc. should go here.

mgr_scene.py - The Scene Manager. Also known as game states, this controls the flow of scenes during runtime. Each scene is a separate object, and this manager files maintains them and their swapping during play.

mgr_sprite.py - The Sprite Manager. This handles the operations to put together spritegroups and spritesheets. Sprite objects themselves should be handled in whatever objects that have their own sprites, whereas this manager prepares those sprites collectively.

mgr_video.py - The Video Manager. This handles the display, framerate, delta-frame variable for frame-independent motion, etc.

model.py - The game model. This is where the game-wide logic is typically stored and manipulated. Scenes A and B demonstrate this by changing a single value that maintains itself between the two scenes.

scn_a - A test scene used to swap between A and B. Also used to test model updates between both scenes.

scn_b - A test scene used to swap between A and B. Also used to test model updates between both scenes.

scn_c - A test scene used to intentionally crash the game if a non-existent scene is called.

scn_d - A test scene for seeing if posting user-defined events work.

scn_e - A test scene for checking sprite group updating.

scn_f - A test scene for checking sprite group updating, using the RenderUpdates group.

scn_g - A test scene for testing camera translation.

spt_a - A test Actor object with a local Sprite object, used in Scenes E and F. It's a square that follows the mouse cursor. Used to represent a sprite and its parent actor object.

splash.png - A sample graphic to demonstrate the use of a splash screen. This is an optional component and can be disabled in the game.py file.

uevents.py - A module containing a dictionary of all user-defined events. Create your own here following the same model as 'Test' and 'Tick'.

server.py - A rudimentary socket server to test with. NOT SECURE - USE AT YOUR OWN RISK!

client.py - A rudimentary client for the socket server. NOT SECURE - USE AT YOUR OWN RISK!

/gui/ - This folder is a boilerplate for a wxPython application, which can be useful to build an editor with.