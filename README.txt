pyGameFrame - Game-Building Template (using just Python and Pygame)

Originally created by Santo Ciaravino

Released under Tricorne Games in 2014

---

BEFORE USING THIS PACKAGE, YOU MAY WANT TO GET THE FOLLOWING:

Python 3 - The programming language to write the games with in this template.

http://www.python.org

Pygame - The library you need to run the template and build games with.

http://www.pygame.org

Make sure they are compatible with each other. It's usually safest to get the matching versions.

===DISCLAIMER===

As far as this goes, this package was made to help aid the aspiring game developer to use the popular open-source "Pygame" library. It is free software, both in cost and the ability to reuse it to your needs. You may do as you please with it. Crediting is highly appreciated, but not required.

Because of the universal scope of game development, the material in this package can be modified at the user's will. The whole point of the template is to become the game that the developer wants... Or at least get a better grasp of how Python and Pygame work together, without worrying about the intricate details in the background like setting up the display.

And of course, props to everyone who made Python to be such a great platform for programming.

===GUIDE===

pyGameFrame is built to be exactly what it sounds like: a framework, a template, a skeleton, to quickly develop a game, using Python and Pygame. Through many hours of reading documentation, books, and tutorials, the creator built each piece to automate every essential and reused step so there's no need to keep doing it for every game made. Simply copy, paste, and you now have a foundation to build your next masterpiece. All the code to render a screen is there, all the code to cut a sprite is there, all the code to run a "scene" in your game is there. And from there, you work your magic.

Here's the breakdown. Just ignore the __pycache__ folders, those are just requirements for Python's reading.

1. simplegame.py - This is just a self-contained game, in case your game is practically small enough to not need the modularity the rest of the template has.

2. game.py - If you're writing a much larger game, this is the whole of your game. You double-click this, and it runs whatever else you programmed in the rest of the game, all found in DIR_data. Inside this file, you code the resources the game needs, and the workflow of the scene objects.

3. DIR_data - All your game's resources go here.

4. DIR_console - This is the "engine" of the template. It stores each component to make the back-end stuff run. DAT_audio contains a tool to control your sound system, DAT_joy contains data to run your joystick controls, DAT_video works your display and rendering matters, and DAT_spriter is a unique tool that can cookie-cut images out of a sprite sheet for your sprites. You can still use separate files as you wish.

5. DIR_asset - Your game's "assets", such as levels, characters, objects, sprites, songs, sounds, etc. go here.

6. DAT_scene - Where game.py is the whole of your game, DAT_scene files will make up the parts. A scene is each different section you see in a game, such as "Title" or "Character Select" or even the actual game action itself, whatever you wish to call it. Usually, you use a return value to tell game.py what to do next.

