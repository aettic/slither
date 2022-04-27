# Slither

This application started as a playground to test out python development in Atom text editor. It has now become a text-based adventure game engine. There are a lot of plans for what this can become, but I'm trying to take things one bit at a time, and have fun doing it. At present, the scope for completion is to create a demo, which is Act I of a text-based game called Aetrynos, which takes place in the titular world, in a small country-side. There are rough plans for three acts, the latter two of which will hopefully build onto the mechanics of the first act. The first act is called "The Farm", and takes place, you guessed it, on a farm.

---

## Files

#### main.py
The core of this program, where the game code is written and executed.  

#### zones.py
A file which contains information on all of the zones in the area, in the form of Zone() objects.  

#### player.py
A core element of the game, generates the actual player object, which is carried forward through the entire game. Houses the globalStatus boolean dictionary, inventory items list, stats, and general save state. Includes a feature to save the game to a json file. Contains information for combat, using items, and a player menu which includes universal options, which can be used regardless of location (this was to reduce the increasing amount of options in a given zone)

#### item.py
Houses descriptions for all items in the game, organized by itemID. Can contain lots of information, such as what type of object it is, whether it has any magical abilities, or gives a boost to armor or damage, etc. All items share a common set of traits, all of which start as False, and are turned on for individual items based on needs.

#### creature.py
Creates creature objects to be used for combat. Includes elements like HP, descriptions, item drops, weapons, etc., as well as functions for combat.

#### npc.py
Used to generate non-player character objects which can be interacted with, including dialogue options, and globalStatus booleans which can allow for choices to seriously affect the way the game plays.

---

## Planning the game
Like with Bloodborne java, there will be a player character object which is passed through to each of the sections of the game. Each section will be governed by if/else, and will trigger a zone. Each zone (like rooms in Bloodborne) will contain items, descriptions, and any interactive features. The player character will contain information relevant to the player's stats, and items, etc. But will also contain the global status dictionary so that rooms can remain consistent over time.

---

## The Slither Engine so far
This is a zork-like text-based adventure game. It contains a global status system to track world changes consistently. It uses a numbered option based system for actions. The story is homebrew High Fantasy, taking place in a land called Aetrynos. Distinct from Javaborne, this game is designed with a single "doSomething()" function which can handle all locations and all actions. This, paired with the system of selection and options rooted inside the player's active zone itself allows for a smooth, single system which can handle and parse many different things. The engine utilizes object-oriented-programming to handle creating the necessary entities and objects which interact in the game (Player, creature, items, zones, etc.)


---

## Development Progress

#### Priority To Do
DONE

#### Extra To Do
- [ ] Add directions to movement options?
- [ ] Add Scarecrow to descriptions of the garden / prairieBackyard
- [ ] Build a way to light the candles in the study with the matches, so they stay lit
- [ ] Build NPC objects with interactive dialogue capacity (model after combat) (for Act 3)
- [ ] Clean up code redundancy, especially in zones
- [ ] Fix the cornfield options and flavor text
- [ ] Look into combining all possible movements into one function - pc.moveTo(Zone) or something
- [ ] Make the matches expendable, so you only have three
- [ ] Redesign doSomething choices to ALWAYS include moving backwards as number 1
- [ ] Redesign Items so that inventory and everything use actual Item objects, not just the ID
- [ ] Redesign menus to always include a movement option which opens a move menu for each room
- [ ] Write out Cornfield First Time text for all zones

#### Done
- [x] Actually use item.py before getting too carried away
- [x] Alchemical Jar Bomb: Add descriptive information for fragility
- [x] Build load state function
- [x] Build combat system
- [x] Build magic system
- [x] Build creature objects for combat
- [x] Check lighting and timer in the Cellar
- [x] Complete location globalStatus entries
- [x] Complete the Beast itemDrops
- [x] Construct a puzzle using items (Alchemical Powder, Glass Jar, Acrid Solution)
- [x] Create a combine method
- [x] Create a useItem method in player.py (now contains equip, toggle, and spell, and combine)
- [x] Create Dark timer for Grue attack - 2 rounds
- [x] Create end of game / game win screen
- [x] Create Matches timer - 5 rounds
- [x] Design basis for the Maze (20 zones)
- [x] Design paths for each of three mazes
- [x] Design spell(s) for Spellbook
- [x] Design the rest of the journal page ink puzzle
- [x] Finish combat options
- [x] Finish equipment (equip, unequip, with inventory access, also bare fists)
- [x] Finish Jar Bomb spell effects for damage
- [x] Finish Jar Bomb spell effects for environment puzzle
- [x] Finish Manual
- [x] Finish programming the maze
- [x] Fix closet entrance from Master bedroom
- [x] Fix combat health issue (scaling and balance)
- [x] Fix Spells in book
- [x] Fix the barnLoft
- [x] Fix the cellar's descriptions
- [x] Fix the lighting problem in the Study (if matches / lantern lit: dark is True)
- [x] Fix the options for consistency in farmhouseStudy and farmhouseCloset2
- [x] Fix problem with globalStatus not updating properly (had to do with How python uses boolean)
- [x] Make it so having read all three notes reveals the stairs
- [x] Make using the amulet reveal the stairs
- [x] Move Lantern to Shed (Once shed is built, maybe replace lantern with something in study)
- [x] Organize globalStatus entires
- [x] Put a Grue in the Barn Loft
- [x] Put a Grue in Cellar
- [x] Reformat all flavor text and results / separate properly from commands
- [x] Test save state works
- [x] Write out Farmhouse Zones
- [x] Write out Prairie First Time text
  - [x] prairieBackyard first time text
  - [x] prairieOuthouse first time text
  - [x] prairieShedExterior first time text
  - [x] prairieShedInterior first time text
  - [x] prairieWell first time text
- [x] Write out Barn First Time text
  - [x] barnBack first time text
  - [x] barnFront first time text
  - [x] barnInterior first time text
  - [x] barnLoft first time text
  - [x] barnStable first time text
- [ ] Write out Cornfield First Time text
  - [x] cornfieldEdge first time text
  - [x] cornfieldMazeCenter first time text
  - [x] cornfieldMaze1 first time text
  - [x] cornfieldTangle first time text
  - [x] cornfieldThick first time text
- [x] Write out Barn Zones
- [x] Write out Cornfield Zones
- [x] Write out Prairie Zones
- [x] Write out the story more thoroughly in a secret canon piece

---


# SPOILERS BELOW


## Puzzles

#### Alchemical Bomb
A glass jar bomb will explode if rolled or dropped into the well.
The jar can only be used once, which means it has to be an optional puzzle.
It can either lead to some special item, information, or a location.
Wherever it leads, if it is central to the story, it must be accessible via other methods.
If it's not pertinent to the story, it can be nearly anything.
Wherever the bomb is used, it should be rolled, and hopefully rolled under some kind of small hole, that's big enough for the jar, and to look through, but too small to enter.

Can also be expended as a strong explosive weapon to kill creatures. Maybe make an optional area in Act 2 or 3 that could utilize it as a puzzle key too; so it's one or the other in a play through.
Written clue to how it might be used?

Drop into the well to explode and dislodge an obstruction, allowing the bucket to be retrieved. It seems that an item was placed in the well. Perhaps Dareth placed it there to keep it safe. The goblins tossed a heavy stone on top, which got jammed halfway down the well shaft. This made it impossible to retrieve the bucket. Examining the well reveals that there is a blockage, and pulling on the rope shows that it does move, but whatever is below is getting stuck on the boulder. The bomb can be shaken and thrown from the Inventory menu when the player is at the well. This will cause it to explode, breaking up the stone.

#### The Corn Maze
Ultimately I want this to feel like an actual maze, requiring a strategy to figure out. I do not want it to be completely random, but I also do not want it to be a one shot path. One way to do this could be to include a few different paths which are randomized and one is chosen when the game is first launched (this would be defined in the player object, so it remains consistent across saves). Perhaps I can make it so the flavor text is distinct as you are progressing through some of them, so it's not all just "Maze", like in Zork.

The cornfield is currently set up like this:
- Edge : Outside the cornfield
- Thick : In the dense corn, but still passable, possible encounter with goblin.
- Tangle : A deeper part of the dense cornfield, movement is difficult. This leads to Maze Start
- Maze Start : The entrance of the maze proper. Leads to three possible, and distinct paths.
- Maze 1 - 9 : Similar, but unique zones where progress is made.
- Maze Center : The Goal, where the corn maze empties out into a crop circle, with a stone staircase leading down into the ground.

Possible Pathways (For further development):

ORANGE: S - 01 - 02 - 04 - 19 - 17 - 15 - 09 - 12 - 13 - 10 - 11 - 16 - 18 - 08 - C
PURPLE: S - 01 - 05 - 06 - 08 - 11 - 10 - 09 - 12 - 15 - 17 - 07 - 04 - 05 - C
GREEN:  S - 01 - 03 - 20 - 06 - 08 - 18 - 16 - 16 - 14 - 13 - 10 - 09 - 07 - C

[27, 28, 29, 31, 46, 44, 42, 36, 39, 40, 37, 38, 43, 45, 35, 48],
[27, 28, 32, 33, 35, 38, 37, 36, 39, 42, 44, 34, 31, 32, 48],
[27, 28, 29, 47, 33, 35, 45, 43, 41, 40, 37, 36, 34, 48]


**Core concept for maze solution - for future development**
The corn maze can be entered from the cornfieldEdge zone, which leads to cornfieldThick, and then cornfieldTangle, where the first glimpse of the Goblin is. Then, continuing, the player will reach cornfieldMazeStart. The only way forward from Start is to 1, always (zone 28), but from that point on there are choices. Depending on which maze path is randomly selected, different walls will be erected, so as to confuse the player, this way it will feel more like a true maze, with dead ends, and perhaps circuitous routes.

The key to progressing is to move FROM a given room into its next room. For instance, in the Orange path, you move from S (0) to 1, and then from 1 to 2 (left), 3 (right), or 5 (up) If  you move to 2, then it progresses, but otherwise it does not. Even if you moved from, say, 1 to 5 to 4 to 2, it will not progress, it has to be from 1 to 2.

The way this will be handled is with arrays / lists, and a solid int variable called progress:
The Key path list which dictates what order things will need to go in. Progress will show where the player has reached so far. a "next" variable will show the ID of the next necessary zone. a position variable will track the index of the path key, so it will start at 0 and increment by 1 for each zone in the correct order entered.

When the player enters cornfieldMazeStart, the progress variable becomes 27 (0, start). The Zone presents the player with the option to move forward. If they do, the progress variable is updated to the next number in line, 28 (1), and the "next" variable is updated to the next one in the list.



---

## Style Guide
Various types of information should be laid out consistently.

#### Alerts
All caps, inside double colons, one carriage return, one tab.  
`("\n\t:: ALERT ::")`

#### Notification
All caps, inside scores, one carriage return, one tab.  
`("\n\t# NOTIFICATION #")`

#### Prompts
A chevron immediately following the prompt text, one space after. Appropriate punctuation on prompt. Often phrased as a question.  
`("\nPrompt text: \n> ")`

#### Choices
Numbered, starting with 1, followed by a colon.
Choices should be followed by a prompt, and preceded by a notification.  
Item and zone names should be capitalized.
`("1: Choice")`

#### Descriptions, Results, and Summaries
Appropriate capitalization and punctuation, carriage return before.  
`("\nThis is a sentence.")`  
Summaries should be short, as they will be displayed every time someone enters a space, after the first time. This should include a brief description of the most obvious elements of a space, as well as the immediately accessible zones around it.

First Time text, or initial flavor text, is a longer version of the summary (which includes similar information) which is only displayed once: when the player first enters a space. This can be used for context-related descriptions, such as a one-time event happening, or to describe more specifically moving into a space from the only place you could get to it from. For instance, the inside stairs can only be accessed by the sitting room for the first time, so the First Time text takes that into consideration. But after this, it's possible to arrive there from upstairs or the ground floor, which means the Summary ought to be entrance-agnostic.

Description text does not need to include movement directions; only a thorough description of the zone, and any items / interactables inside it.

---

## Story (MAJOR SPOILERS)
You are a friend of Alys, a stargazing farmer from the countryside town of Almyth. Alys has sent word to you, asking you to come to her farm and see what she has been working on. She seemed both desperate and excited. It was a suspicious letter, but not out of the realm of possibility from her.

When you arrive at her farm, you find that she is gone. Where did Alys go?

For weeks, Alys had been on the verge of unlocking the secrets of an entrance to the Faewilds, or the Underworld which is located very near to her farm. In fact it's located inside her corn field. However, it's not always there. This entrance is a spiral staircase leading underground, but it simply does not always exist. It can only be seen or experienced with the proper alignment of the stars. One of these alignments happened within the last few weeks, and Alys stumbled upon this entrance by accident. She ventured in, and found herself caught in the mystical and timeless world of the Fairies and the Goblins. They did not take too kindly to her presence, and chased her out.

This prompted Alys to work tirelessly on figuring out what alignment caused this entrance to manifest tangibly in her world, and what she could do magically to open it once again. This was a dangerous game she began playing, and it cost her her son's life. He was killed by Goblins who ransacked her farm, and stole her animals. Dareth was her only son, and helped her considerably on the farm. The night of the same day that the Goblins attacked, she was spirited away by elementals and fae, and taken down into their Underworld.

There, she is a prisoner, experiencing that mystical and unforgiving place of insanity without the reliable rising and setting of the sun. She has undergone torture as the Fae scholars try desperately to figure out how she discovered them. She stands resolute, and they aren't happy.

You must explore her abandoned farm, and discover clues that lead to finding and opening the gate, and venture into the Underworld to rescue her.

---

## Gameplay (MAJOR SPOILERS)

#### Act I (In Development)
**The Farm**
Explore the farmland, including the fields, the house, the barn, and smaller buildings to find clues about what might have happened to Alys, and where she might have gone. If one explores the cornfield before finding the proper opening, they will not be able to solve the maze.

#### Act II (Dreaming)
**The Underworld**
Upon entering the staircase, one is transported down into the underworld. This will start out as caves, which in and of themselves will be maze-like. Various things can be found in these caves, from tools and magical items, to history and notes, to secret tunnels, etc. And eventually one may discover the threshold that marks the true descent into the underworld.

#### Act III (Dreaming)
**The Fairy City**
The cave opens up into a grand hollow world, complete with artificial light from a sun that never sets - just circles around the illusory horizon endlessly. Fauna and flora dot the landscape, as does a thriving but foreign fairy world. There is a small fairy city to explore and get lost in, it is dangerous, but exploration provides more unique options for combat and for interacting with the world around you (magical elements like Darkvision, etc. - maybe teleporting? Maybe seeing through walls? Maybe growing in size?) Alys is being held hostage in a fairy jail near the far end of the city. She can be rescued once discovered, as long as one has found the required tools and tricks, or made the right friends.
