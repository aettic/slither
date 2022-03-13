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
This is a zork-like text-based adventure game. It contains a global status system to track world changes consistently. It uses a numbered option based system for acting. The story is homebrew High Fantasy, taking place in a land called Aetrynos. Distinct from Javaborne, this game is designed with a single "doSomething()" function which can handle all locations and all actions. This, paired with the system of selection and options rooted inside the player's active zone itself allows for a smooth, single system which can handle and parse many different things. The engine utilizes object-oriented-programming to handle creating the necessary entities and objects which interact in the game (Player, creature, items, zones, etc.)

### To Do (Development)
- [x] Create a useItem method in player.py (now contains equip, toggle, and spell)
- [ ] Create a combine(item, item) method
- [ ] Construct a puzzle using items (Alcohol, alchemical stuff, blowing something up?)
- [x] Actually use item.py before getting too carried away
- [x] Test save state works
- [x] Build load state function
- [x] build combat system
- [x] build magic system
- [x] build creature objects for combat
- [ ] Put a Grue in Dark spots (cellar, loft) (Add Dark timer (Dark True, Darkvision False, Dark Place True - 2 rounds))
- [ ] Finish combat options
- [ ] Complete Beast itemDrops
- [ ] Write out the rest of the zones
- [x] Complete location globalStatus entries
- [x] Organize globalStatus entires
- [ ] Create more globalStatus entries as needed
- [ ] Write out the story more thoroughly in a secret canon piece.
- [ ] Fix problem with globalStatus not updating properly (still need to identify)



### Story
