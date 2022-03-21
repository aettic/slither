# Slither

This application started as a playground to test out python development in Atom text editor. It has now become a text-based adventure game engine. There are a lot of plans for what this can become, but I'm trying to take things one bit at a time, and have fun doing it. At present, the scope for completion is to create a demo, which is Act I of a text-based game called Aetrynos, which takes place in the titular world, in a small country-side. There are rough plans for three acts, the latter two of which will hopefully build onto the mechanics of the first act. The first act is called "The Farm", and takes place, you guessed it, on a farm.



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
- [ ] Alchemical Jar Bomb: Add descriptive information for fragility
- [ ] Build NPC objects with interactive dialogue capacity (model after combat)
- [ ] Construct a puzzle using items (Alchemical Powder, Glass Jar, Acrid Solution)
- [ ] Create more globalStatus entries as needed
- [ ] Design spell(s) for Spellbook
- [ ] Finish combat options
- [ ] Finish equipment (equip, unequip, with inventory access, also bare fists)
- [ ] Finish Jar Bomb spell effects for damage
- [ ] Finish Jar Bomb spell effects for environment puzzle
- [ ] Look into combining all possible movements into one function - pc.moveTo(Zone) or something
- [ ] Move Lantern to Shed (Once shed is built, maybe replace lantern with something in study)
- [ ] Put a Grue in the Barn Loft
- [~] Reformat all flavor text and results / separate properly from commands
- [ ] Write out Prairie First Time text
- [ ] Write out Barn First Time text
- [ ] Write out Cornfield First Time text
- [ ] Write out Prairie Zones
- [ ] Write out Barn Zones
- [ ] Write out Cornfield Zones

## Done
- [x] Actually use item.py before getting too carried away
- [x] Build load state function
- [x] Build combat system
- [x] Build magic system
- [x] Build creature objects for combat
- [x] Check lighting and timer in the Cellar
- [x] Complete location globalStatus entries
- [x] Complete the Beast itemDrops
- [x] Create a combine method
- [x] Create a useItem method in player.py (now contains equip, toggle, and spell, and combine)
- [x] Create Dark timer for Grue attack - 2 rounds
- [x] Create Matches timer - 5 rounds
- [x] Fix closet entrance from Master bedroom
- [x] Fix the cellar's descriptions
- [x] Fix the lighting problem in the Study (if matches / lantern lit: dark is True)
- [x] Fix the options for consistency in farmhouseStudy and farmhouseCloset2
- [x] Fix problem with globalStatus not updating properly (had to do with How python uses boolean)
- [x] Organize globalStatus entires
- [x] Put a Grue in Cellar
- [x] Test save state works
- [x] Write out Farmhouse Zones
- [x] Write out the story more thoroughly in a secret canon piece.



## Puzzles

#### Alchemical Bomb
A glass jar bomb will explode if rolled.
The jar can only be used once, which means it has to be an optional puzzle.
It can either lead to some special item, information, or a location.
Wherever it leads, if it is central to the story, it must be accessible via other methods.
If it's not pertinent to the story, it can be nearly anything.
Wherever the bomb is used, it should be rolled, and hopefully rolled under some kind of small hole, that's big enough for the jar, and to look through, but too small to enter.







## Style Guide
Various types of information should be laid out consistently.

#### Alerts
All caps, inside double colons, one carriage return, one tab. ("\n\t:: ALERT ::")

#### Notification
All caps, inside scores, one carriage return, one tab. ("\n\t# NOTIFICATION #")

#### Prompts
A chevron immediately following the prompt text, one space after. ("\nPrompt text\n> ")

#### Choices
Numbered, starting with 1, following a colon. ("1: Choice")
Choices should be followed by a prompt, and preceded by a notification.

#### Descriptions, Results, and Summaries
Appropriate capitalization and punctuation, carriage return before. ("\nThis is a sentence.")



## Story
You are a friend of Alys, a stargazing farmer from the countryside town of Almyth. Alys has sent word to you, asking you to come to her farm and see what she has been working on. She seemed both desperate and excited. It was a suspicious letter, but not out of the realm of possibility from her.

When you arrive at her farm, you find that she is gone. Where did Alys go?

For weeks, Alys had been on the verge of unlocking the secrets of an entrance to the Faewilds, or the Underworld which is located very near to her farm. In fact it's located inside her corn field. However, it's not always there. This entrance is a spiral staircase leading underground, but it simply does not always exist. It can only be seen or experienced with the proper alignment of the stars. One of these alignments happened within the last few weeks, and Alys stumbled upon this entrance by accident. She ventured in, and found herself caught in the mystical and timeless world of the Fairies and the Goblins. They did not take too kindly to her presence, and chased her out.

This prompted Alys to work tirelessly on figuring out what alignment caused this entrance to manifest tangibly in her world, and what she could do magically to open it once again. This was a dangerous game she began playing, and it cost her her son's life. He was killed by Goblins who ransacked her farm, and stole her animals. Dareth was her only son, and helped her considerably on the farm. The night of the same day that the Goblins attacked, she was spirited away by elementals and fae, and taken down into their Underworld.

There, she is a prisoner, experiencing that mystical and unforgiving place of insanity without the reliable rising and setting of the sun. She has undergone torture as the Fae scholars try desperately to figure out how she discovered them. She stands resolute, and they aren't happy.

You must explore her abandoned farm, and discover clues that lead to finding and opening the gate, and venture into the Underworld to rescue her.



## Gameplay (SPOILERS)

#### Act I (In Development)
**The Farm**
Explore the farmland, including the fields, the house, the barn, and smaller buildings to find clues about what might have happened to Alys, and where she might have gone. If one explores the cornfield before finding the proper opening, they will not be able to solve the maze.

Dev objectives: Clues in cryptic notes, puzzles involving items, hidden things which require creative exploration, an actual solvable but difficult maze.

#### Act II (Dreaming)
**The Underworld**
Upon entering the staircase, one is transported down into the underworld. This will start out as caves, which in and of themselves will be maze-like. Various things can be found in these caves, from tools and magical items, to history and notes, to secret tunnels, etc. And eventually one may discover the threshold that marks the true descent into the underworld.

#### Act III (Dreaming)
**The Fairy City**
The cave opens up into a grand hollow world, complete with artificial light from a sun that never sets - just circles around the illusory horizon endlessly. Fauna and flora dot the landscape, as does a thriving but foreign fairy world. There is a small fairy city to explore and get lost in, it is dangerous, but exploration provides more unique options for combat and for interacting with the world around you (magical elements like Darkvision, etc. - maybe teleporting? Maybe seeing through walls? Maybe growing in size?) Alys is being held hostage in a fairy jail near the far end of the city. She can be rescued once discovered, as long as one has found the required tools and tricks, or made the right friends.
