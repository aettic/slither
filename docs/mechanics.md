# Mechanics
This document features an outline of the general mechanics of Aetrynos.

#### SCENES
The game is played out in scenes, which are the intersection of the player character, any items and features, any entities, and the zone these things exist in. A scene takes place over a number of rounds.

**Rounds**
A Round is defined as the time in between each player-selected option. Interacting with an item takes one round. Moving one zone takes one round. Striking a creature takes one round. Everything that a player can choose to do takes one round, which means once a player chooses an option, a round passes before they can choose another option.

**Zones**
A Zone is the literal space that a scene plays out in. The player can stay in a zone for more than one round. A Round counter can be used for things such as the Grue appearing, or matches burning out. Zones are connected to each other, but can only be reached by those zones that are also connected to them, this way movement is consistent.

**Items**
An item which can be interacted with and typically picked up. Items contain a variety of properties, and can be accessed through the inventory.

**Features**
A feature is any object or characteristic of a zone, typically one that does not move, which may be interactable, or static.

---
### CHARACTERS
The game is comprised of characters interacting with each other and the world around them.

**Player Character**
The Player Character is the focal point of perception for the game, it is from the player character's eyes that the player experiences the game. The player character tracks persistence through the game, including globalStatus booleans, statistics, inventory, and current zone. It is the player character information which is saved.

**Creatures**
A creature is usually a monster, or some kind of enemy character which is engaged in combat with the player character.
- Goblin
- Grue
- Spider
- Slime Cube
- Skeleton
- Hobgoblin
- Troll
- Unique Fae

**NPCs**
A non-player-character, who is interactable in some way; usually through conversation, though trade or combat may also be possible.NPCs exist in a zone, but may move around and be found in other zones. The NPC, like the player character, contains a persistent set of features, including the zone it is in.

---
### ACTIONS
Outlining the basic choices a player has in the game. All actions are depicted as things the player character can do, and usually begin with a verb.

**Movement**
`Walk to the backyard`
All zones include movement options, every zone is connected to at least one other zones. Connections are two-way unless specifically noted as a one way movement (A fall off a cliff or down a hole, walking through an unstable threshold which collapses and prevents return). In a given scene, a player can move to one adjacent zone, so long as it is accessible. These are always the first options in a round. A zone is accessible as long as nothing is preventing movement (such as a locked door). Trying a door will reveal that it is locked, though this will not remove the movement option, but attempting it will once again cause a message to issue, explaining that the movement is impossible.

**Interact**
`Peer through the telescope`
Some features in a zone are interactable, meaning the player can do something with them, this is usually a repeatable option, such as examining something closely, but occasionally it leads to a globalStatus change, which means that it has temporarily or permanently affected the options in that zone (depending on whether the action can be undone).

**Take**
`Take the boots`
Some zones contain items which can be taken and added to the inventory.

**Look around**
`Look around the room`
This option is always available in every zone, and allows the player to more closely examine their surroundings, often revealing details, features, and items which were not readily apparent.

**Player Menu**
This menu is always accessible, regardless of zone, and contains additional options, such as interacting with the player's inventory, or saving the game, quitting, accessing the in-game Help, etc.

---
### SKILLS
Boosted at the very beginning of the game, these four Skills determine Player Character Stats. All Stats begin at 9, and the player has 10 experience points (XP) to spend across these Skills, distributed however they see fit. Any unused XP is saved as XP throughout the game, to be used at level up, or converted to victory points at the end of the game. The higher a Skill's rating, the more effective it is.

**STR - Strength**
A rating of the player character's physical prowess, including their ability to wield large weapons, perform certain tasks, or deal Damage.

**DEX - Dexterity**
A rating of the player character's flexibility, speed, and finesse, which determines their base Defense.

**INT - Intellect**
A rating of the player character's mental abilities, responsible for Magic, and for solving puzzles.

**CON - Constitution**
A rating of the player character's heartiness and fortitude, which determines their HP, and ability to withstand poisons.

---
### STATS
All entities contains Stats, whether a Player Character, a Creature, or an NPC. Not all Stats are shared by all entities, but all of these are relevant to the player character.

**HP**
Separated into both currentHP and maxHP, which determine respectively the remaining, and maximum possible hit points available to the entity.

**Damage**
Used as the base value for generating damage per strike.

**Defense**
Used to reduce incoming damage dealt to the entity.

**Magic**
Used to determine ability to use magical items, including tools, weapons, and spells.

---
### INVENTORY
The player character can hold inventory items that they find throughout the game. Interacting with the inventory is an action that is available in the player menu in all scenes. When the player interacts with an inventory item, its Use is triggered. Based on its Use type, a different effect may happen.

**Item Attributes**
Each item contains several attributes, which define what it is, how it works, and anything else applicable to it. All items share some basic attributes, such as Name, Value, and Description. Boolean values default to False, and are modified to True with any extra applicable attributes added on afterward. Items do not contain all attributes.

- **Basic Attributes**
	- Name: The title or name of the item, how it appears in the inventory list.
	- Description: The long form description of the item, appearing in the list.
	- Value: The Item's worth in victory points / gold.

- **Boolean Attributes**
	- Equippable: A boolean determining whether the item can be equipped.
	- Armor: A boolean determining whether the item is armor (requires Equippable).
	- Weapon: A boolean determining whether the item is a weapon (requires Equippable).
	- Magic: A boolean determining whether the item is magical.
	- Use: Determines whether and how an item can be interacted with. See Use Types below.

- **Extra Attributes**
	- Read: Text to be read when the item is used.
	- Armor Bonus: A boost to the wearer's Defense Stat, and occupies the armor slot.
	- Damage Bonus: A boost to the wielder's Damage Stat, and occupies the weapon slot.
	- Magic Bonus: A boost to the user's Magic Stat.
	- Skill Required: Contains a Skill abbreviation and a value which is required for using the item. Ex. `{"INT": 13}`,  means that the item requires the user to have at least a 13 in INT.
	- Combine: A list of item IDs which represent all other items required to combine with the current item. Ex. Item ID #6 (Bottle of Ink) requires ID #23 (Journal Page), and vice versa. With both, either one of them can be used to activate their combine effect, and create ID #24 (Stained Journal Page).
	- Light Source: A Boolean which determines whether the item sheds light when activated.
	- Spell: Contains a textual description of the magical effect of the item when used.

**Use Types**
- False: No Use ability. This is default.
- Read: Displays a message, used for notes, books, and other items which can be read.
- Equip: Add the item to your Equipment; replaces any item that is currently in that slot.
- Combine: Requires other defined items, when all are present in the inventory, using combine on any of the items involved will combine them all into a new item.
- Spell: Activate a specific magic ability, defined by the item itself.
- Toggle: Turn something on or off.
- Trigger: Activate a one time effect, which does not expend the item.
- Expend: Activate an ability (such as lighting a match) which expends part of the quantity.

---
### LIGHTING
By default, all outdoor areas, and indoor areas with windows are considered well-lit. This means that the player can see, and interact with the room. Everything is assumed to be lit unless it is explicitly dark.

**Dark**
If the room is dark (i.e. there are no windows, or light source), the globalStatus boolean "Dark" is True. By itself, Dark makes it difficult to interact with things in the room, but it is not by itself dangerous.

**Dark Place**
In some cases, certain zones are considered pitch black, and have the additional trait "Dark Place". This is used to determine whether Dark should be enabled when the player enters a zone without a light source.

If a Dark Place is Dark, it is pitch black, and impossible to interact with the surroundings, or any items. If the player tries to look around, they are unable to, and waste a round. If they spend 3 rounds in darkness (trying to look around, using inventory items, etc.) they will encounter a Grue, which will try to kill them.

**Light Sources**
There are a few artificial sources of light in the game:
| Item    | QTY    | Duration      | Use        | Fire |
| ------- | ------ | ------------- | ---------- | ---- |
| Lantern | 1      | Unlimited use | Toggle     | No   |
| Matches | 20     | 3 rounds each | Expend     | Yes  |
| Candle  | 2      | 20 rounds     | Ignite     | Yes  |
| Torch   | 1      | Unlimited     | Ignite     | Yes  |
| Hearth  | Unique | Unlimited     | Stationary | Yes  |

The lantern (which features unlimited rounds of light) is found in Act 1, in the Shed, which requires Darreth's key to unlock. Darreth used this lantern to tend to the animals at night, or scare away raccoons and vermin.

Matches last 3 rounds each, and are expendable. Once they're gone, the player must find more, or find another source of light. They can be extinguished before the 3 rounds are up, but they cannot be recovered. Alys does not smoke, but her son Darreth did, he would use matches to light his hand-rolled cigarettes.

There are two candles in the Dark Below, on different levels, which can each last 20 rounds, and can be put out and relit, but each light requires Fire.

There is a torch in an obscure area on the first layer of The Dark Below (The Caves), which requires Fire to light, but lasts forever, and produces Fire as well. The torch has been burned before, but has most of its wick remaining. It is found on the corpse of an adventurer who became lost in The Caves, and starved to death. A merciful end compared to what the fae might have brought him.

A hearth room lies on the second floor, where a fire burns casually, a reminder of the warmth of civilization in the face of the strange and unknown dark world. The hearth's flame is constant, and provides both light and Fire, but cannot be moved.

---
### FIRE
Fire is needed to activate (ignite) certain items. If fire is present during a round, the globalStatus boolean "Fire" is True. Fire also produces Light. If an item requires Fire for activation, it cannot be activated unless Fire is present in the scene.

Items which utilize Fire for activation:
| Item      | Effect           | Duration    |
| --------- | ---------------- | ----------- |
| Matches   | Light & Fire     | 3 rounds ea |
| Candle    | Light & Fire     | 20 rounds   |
| Torch     | Light & Fire     | Unlimited   |
| Sketch    | Reveal Text      | Once        |
| Gunpowder | Activate puzzle  | Once        |
