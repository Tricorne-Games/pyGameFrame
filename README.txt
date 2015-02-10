pyGameFrame
2015 by Tricorne Games



REQUIREMENTS

This system was written in Python 2.7.9, using Pygame 1.9.1 release designed for Python 2.7. You can download each of these at:

www.python.org
www.pygame.org



DISCLAIMER

pyGameFrame is freely usable software, aimed to help aspiring game designers and developers. You may use it and modify it to best suit your needs, including commercial use.

The license included is only to preserve the authorship of this base. It is not required to include it for your games (because this code is designed to get strongly altered to become a game of one's own), but a courtesy credit is highly appreciated.

Credit goes to the people who made Python and Pygame happen, to allow this framework to be built.



ABOUT

pyGameFrame is a template set of Python files written and designed to help the end user develop games in the Python/Pygame environment; with a simple copy-paste preparing your whole project and all of the technical stuff ready to go.

The advantage given is that a lot of the technical clout, such as setting sprites, audio management, and visual setup is all done, and prepared for efficient, streamlined development, so the user can focus on developing the logic and assets of the game instead. Like any Python project, it is also mutable, so it can be torn apart and remodeled to better fit the developer's needs.

First built as "Santo's Pygame Template", it was created by looking through different resources on the Pygame system, including documentation, books, websites, and even pygame-built games, to eventually develop a "consistent" formula that made the most sense with how Pygame works. Two more versions, retitled "pyGameFrame", followed with a bigger clean-up job; the latter included being ported over to Python 3.

In this version, it was decided to use the latest and final version of Python 2 (2.7.9), to allow use of the extensive amount of libraries available to that version, at the time this was programmed. However, it was written with care to make it a less troublesome transition to Python 3, if that is the developer's choice of version to use.



HOW IT WORKS

1. The "game" file starts by first creating a game() object, which encapsulates all of the files found in the /data/ directory.

2. The /data/ directory contains the following, and sends it over for the game() object to initialize:

a. The "scene" files inside /data/ - These are the different scenes you see in each step of the game, such as title screen, main menu, the game action, levels, etc. Other than the back-end gear, scene files make up the meat of your game's activity. This is where most of your coding should happen.

b. /framesys/ - This is the directory that does the back-end work of the game. It handles the audio() manager (controls sound channels, loads sound files, etc.), the video() manager (handles screen updating, splashscreens, fullscreening, etc.), the joy() manager (handles joystick/controller input), and lastly, a custom tool unique to pyGameFrame, called the Spriter(), which manages all of the spritesheets and cookie-cuts the specific sprite surfaces for any assets that need them.

c. /assets/ - This contains two different kinds of assets: your media assets (sounds, graphics, etc.), and your logical assets (player data, etc.).

3. That game() object from the first step now puts all these resources from /data/ in a specific order, between preparing the /framesys/ materials, preloading all of the assets, etc.

4. Finally, that game() object is now called to run (along with all the other prep work in the __name__ == __main__ condition), and thus starts the game loop, awaiting any point the player exits for a clean clean-up.

The idea of this framework is to copy-paste the entire project, and now you have everything you need to begin coding even a basic game with everything you need done to render your game and polished to help you organize. However, you are encouraged to mod it totally as you see fit. For example, maybe you really don't need the joy() manager, or you want to set up a server() manager to have a networked game, or you can have another directory or three inside /data/, such as for save files, utility scripts to handle complex logic inside a scene, etc.