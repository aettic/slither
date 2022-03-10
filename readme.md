# Slither

The goal of this application is to serve as a playground for building python code and experimenting with the Atom text editor.  

So far, Atom seems to be very versatile.  

### main.py
The core of this program, where the python code is written and executed.  

### zones.py
A file which contains information on all of the zones in the area.  

### Planning the game
Like with Bloodborne java, there will be a player character object which is passed through to each of the sections of the game. Each section will be governed by switch:case, and will trigger a zone. Each zone (like rooms in Bloodborne) will contain items, descriptions, and any interactive features. The player character will contain information relevant to the player's stats, and items, etc. But will also contain the global status dictionary so that rooms can remain consistent.

### The Slither Engine so far
This is a zork-like text-based adventure game. It contains a global status system to track world changes consistently. It uses a numbered option based system for acting. The story is homebrew High Fantasy, taking place in a land called Corindos. Distinct from Javaborne, this game is designed with a single "doSomething()" function which can handle all locations and all actions. This, paired with the system of selection and options rooted inside the player's active zone itself allows for a smooth, single system which can handle and parse many different things.

### To Do (Development)
- [ ] Create a useItem method in player.py
- [ ] Actually use item.py before getting too carried away
- [ ] Test save state works
- [ ] Build load state function


### Story
