```
   db     888888  888888  88""Yb  Yb  dY  88b 88   dP"Yb   .dP"Y8
  dPYb    88__      88    88__dP   YbdY   88Yb88  dY   Yb  `Ybo.
 dP__Yb   88""      88    88"Yb     88    88 Y88  Yb   dY    `Y8b
dP""""Yb  888888    88    88  Yb    88    88  Y8   YbodP   '8bodP
```
*A Game Manual*

### Table of Contents
- Downloading the Game
- Starting the game
- Playing the game
- Saving, continuing, and death
- Winning the game
- How to report issues, provide feedback, or donate

### Quick Note
This game comes with all of the source code, as well as the "README.md" which is designed as a development tracker and provides technical information on the game. It *also* contains many spoilers, so please do not read it until after you have played the game. This README manual aims to provide any information that should be needed.

---
### Downloading the Game
From GitHub, you can select Code > Download Zip.

---
### Installing Python3
If you already have Python3 installed and know how to execute .py scripts from the command line, you can skip this section.

If you do not have Python3 installed, you will need to download and install it. There are several ways to do this, I am going to include my personal recommendations here, but the crux of the matter is that you will need to know *how to launch* python3 commands.

In general, I recommend using https://www.python.org/downloads/ to download the official latest release of Python3. The installation process should be straight forward. Once it is installed, restart Terminal or Command Prompt if you have it open, and test it out by executing the command provided.

There are a number of different execution command keywords for python3 depending on your installation and other circumstances, which makes this part a bit annoying, but for sake of ease, I'm just going to use the one I've seen most commonly, which is `python3`, this might be different in your installation, please determine what command is used to execute the python interpreter on your own installation, and substitute that command where you see `python3` below.

---
### Starting the Game
This game is a python script, which means right now it must be run in a Terminal or Command prompt, on a machine running Python3. Extract the zip folder to some location, and then change directory into that location in your Terminal. Then launch the python script from within the "slither" folder.



This should start the game inside your Terminal window. If there is something wrong, you may experience a Python interpreter execution error, and the game will not start. If this happens, please take note of the error and contact me. (See the final section in this manual).

If the text seems to wrap poorly and cuts off words, try increasing the width of your terminal window.

---
### Playing the Game
Running the game should be fairly self-explanatory, but here are the basics:
You create a character by typing in their name, and then allotting stat points to their abilities. Once that process is complete, you will be shown an overview of your characters stats. This same overview is accessible during the game at any time from "Player Menu > View Stats".  

All options are accessible via number key entries. Player Menu is always the last option in the list (the number with the greatest value), and contains constant features like View Stats, or Equipment, or Inventory, and system options such as Save, Quit, and Help.

Movement in the game takes up the top-most action options in any given zone, allowing you to move between zones. Each zone is different, and may have a different number of options for movement, or interacting with the environment.

**Items**
Some zones have objects which can be interacted with. Some of those objects can be taken. Some objects which have been taken can then be used (from within the inventory, or during combat). Some objects can be combined, some can be toggled on or off, some can be equipped. Some objects even function as magical spells, which may be expendable or reusable.

**Gameplay**
The core gameplay loop involves moving through zones, inspecting what that zone contains, interacting with things as you see fit, solving puzzles, and uncovering what happened at the farm. Eventually you may find clues which lead you toward an answer, and pursuing that answer will effectively win you the game. The game's end is not readily accessible without some exploration, though there are multiple ways to get there, all of them involve interacting with the world, and in some cases, solving puzzles.

**Combat**
The game contains combat between the player character and various enemies. Combat is turn based, and designed to give you some options. The goal, however you accomplish it, is to defeat and kill your enemy before it kills you. You enter combat with whatever hit points and items you had at that moment, and when you exit combat, any hit point damage you suffered remains, and your character is then more vulnerable to defeat. It is possible to regain hit points in the game using an item you must discover.

**Magic**
Some items require a certain amount of magic points to use (which might be expended when items are used - depending on the item), while some items will give you more magic points when used; and some items will also require a certain level of INT to use; generally the more powerful the item, the higher level of INT is required. Some magic is expendable and may only be used once, some may be used perpetually, and some may be used as long as you have magic points to spend on them.

**Global Status**
The game uses what is called a Global Status dictionary to keep track of changes to the world, or the player. For instance, if you walk into a room and find an item, and you take that item, then when you walk into the room again, that item will not be there anymore. Every time you enter a zone for the first time also triggers a global status change, so when you revisit zones, their descriptions may be different.

---
### Saving, Continuing, and Death
In any zone (but not during combat) the game's state can be saved (Player Menu > Save Game). This creates a JSON file which contains the active game state, including your character's stats, equipment, inventory, and the current global status of zones and objects.

When you launch the game, you're given the option to start a new game, or to continue from where you left off.

When you die, your game ends, and the application will quit. If you have a save file, you can restart the game from that save, otherwise you can start a new game. It is wise to save often, but especially at strategic moments (after milestones, before combat, etc.)

---
### Winning the Game
Once you have reached the end of the game, you win! Once you win, the game will end, and your achievements will be tallied. Points will be added based on certain accomplishments, and based on the value of items you possess.

### How to report issues, provide feedback, or donate
If you encounter a bug, an issue, or even a typo or spelling error, please take a screenshot of it, and send an email to aetrynos@gmail.com, attaching that screenshot, and explaining in a couple sentences what happened, and what you were doing in game when you encountered the issue.

If you have any other feedback, please send it to aetrynos@gmail.com, I'd love to hear from you about what you think of the game, or ways that the game could be improved moving forward.

If for some reason you feel compelled to donate to this project, you may send donations to aetrynos@gmail.com via PayPal.
