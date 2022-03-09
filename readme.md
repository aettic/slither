# Slither

The goal of this application is to serve as a playground for building python code and experimenting with the Atom text editor.  

So far, Atom seems to be very versatile.  

### main.py
The core of this program, where the python code is written and executed.  

### zones.py
A file which contains information on all of the zones in the area.  

### Structure of the game
Like with Bloodborne java, there will be a player character object which is passed through to each of the sections of the game. Each section will be governed by switch:case, and will trigger a zone. Each zone (like rooms in Bloodborne) will contain items, descriptions, and any interactive features. The player character will contain information relevant to the player's stats, and items, etc. But will also contain the global status dictionary so that rooms can remain consistent.  
