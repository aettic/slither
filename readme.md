# Slither

The goal of this application is to serve as a playground for building python code and experimenting with the Atom text editor.  

So far, Atom seems to be very versatile.  

## Files

#### main.py
The core of this program, where the python code is written and executed.  

#### zones.py
A file which contains information on all of the zones in the area.  

#### player.py
A core element of the game, generates the actual player object, which is carried forward through the entire game. Houses the globalStatus boolean dictionary, inventory items list, stats, and general save state. Includes a feature to save the game to a json file.

#### item.py
Houses descriptions for all items in the game, organized by itemID. Can contain lots of information, such as what type of object it is, whether it has any magical abilities, or gives a boost to armor or damage, etc.

#### creature.py
Creates creature objects to be used for combat. Includes elements like HP, item drops, weapons, etc.

#### npc.py
Used to generate non-player character objects which can be interacted with, including dialogue options, and globalStatus booleans which can allow for choices to seriously affect the way the game plays.

## Planning the game
Like with Bloodborne java, there will be a player character object which is passed through to each of the sections of the game. Each section will be governed by switch:case, and will trigger a zone. Each zone (like rooms in Bloodborne) will contain items, descriptions, and any interactive features. The player character will contain information relevant to the player's stats, and items, etc. But will also contain the global status dictionary so that rooms can remain consistent.

## The Slither Engine so far
This is a zork-like text-based adventure game. It contains a global status system to track world changes consistently. It uses a numbered option based system for acting. The story is homebrew High Fantasy, taking place in a land called Aetrynos. Distinct from Javaborne, this game is designed with a single "doSomething()" function which can handle all locations and all actions. This, paired with the system of selection and options rooted inside the player's active zone itself allows for a smooth, single system which can handle and parse many different things. The engine utilizes object-oriented-programming to handle creating the necessary entities and objects which interact in the game (Player, creature, items, zones, etc.)

## To Do (Development)
- [x] Create a useItem method in player.py (now contains equip, toggle, and spell)
- [x] Actually use item.py before getting too carried away
- [x] Test save state works
- [x] Build load state function
- [x] build combat system
- [x] build magic system
- [x] build creature objects for combat
- [x] Complete location globalStatus entries
- [x] Organize globalStatus entires

- [ ] Create a combine(item, item) method
- [ ] Construct a puzzle using items (Alcohol, alchemical stuff, blowing something up?)
- [ ] Put a Grue in Dark spots (cellar, loft) (Add Dark timer - 2 rounds))
- [ ] Finish combat options
- [ ] Complete Beast itemDrops
- [ ] Write out the rest of the zones
- [ ] Create more globalStatus entries as needed
- [ ] Write out the story more thoroughly in a secret canon piece.
- [ ] Fix problem with globalStatus not updating properly (still need to identify)
- [ ] Build NPC objects with interactive dialogue capacity (model after combat)




## Story
You are a friend of Alys, a stargazing farmer from the countryside town of Almyth. Alys has sent word to you, asking you to come to her farm and see what she has been working on. She seemed both desperate and excited. It was a suspicious letter, but not out of the realm of possibility from her.

When you arrive at her farm, you find that she is gone. Where did Alys go?

For weeks, Alys had been on the verge of unlocking the secrets of an entrance to the Faewilds, or the Underworld which is located very near to her farm. In fact it's located inside her corn field. However, it's not always there. This entrance is a spiral staircase leading underground, but it simply does not always exist. It can only be seen or experienced with the proper alignment of the stars. One of these alignments happened within the last few weeks, and Alys stumbled upon this entrance by accident. She ventured in, and found herself caught in the mystical and timeless world of the Fairies and the Goblins. They did not take too kindly to her presence, and chased her out.

This prompted Alys to work tirelessly on figuring out what alignment caused this entrance to manifest tangibly in her world, and what she could do magically to open it once again. This was a dangerous game she began playing, and it cost her her son's life. He was killed by Goblins who ransacked her farm, and stole her animals. Dareth was her only son, and helped her considerably on the farm. The night of the same day that the Goblins attacked, she was spirited away by elementals and fae, and taken down into their Underworld. There, she is a prisoner, experiencing that mystical and unforgiving place of insanity without the reliable rising and setting of the sun.

You must explore her abandoned farm, and discover clues that lead to finding and opening the gate, and venture into the Underworld to rescue her.

## Gameplay

#### Act I (In Development)
**The Farm**
Explore the farmland, including the fields, the house, the barn, and smaller buildings to find clues about what might have happened to Alys, and where she might have gone. If one explores the cornfield before finding the proper opening, they will not be able to solve the maze.

Dev objectives: Clues in cryptic notes, puzzles involving items, hidden things which require creative exploration, an actual solvable but difficult maze.

#### Act II (Dreaming)
**The Underworld**
Upon entering the staircase, one is transported down into the underworld. This will start out as caves, which in and of themselves will be maze-like. Various things can be found in these caves, from tools and magical items, to history and notes, to secret tunnels, etc. And eventually one may discover the threshold that marks the true descent into the underworld.

#### Act III (Dreaming)
**The Fairy City**
The cave opens up into a grand hollow world, complete with artificial light from a sun that never sets - just circles around the illusory horizon endlessly. Fauna and flora dot the landscape, as does a thriving but foreign fairy world. There is a small fairy city to explore and get lost in, it is dangerous, but exploration provides more unique options for combat and for interacting with the world around you (magical elements like Darkvision, etc.) Alys is being held hostage in a fairy jail near the far end of the city. She can be rescued once discovered, as long as one has found the required tools and tricks, or made the right friends.
