#!/usr/bin/python

# Slither v0.1

# --- Brainstorming goals for this project --- #

    ### Slither can be just about anything, and in fact it can be multiple things. I want to be able to use it for playing around and experimenting with Python in particular. As such, I should create an initial program idea.

    ### A Game
    # My first idea is to create a small graphical game, such as worm / snake, because I've always wanted to do something that like, and never actually done it. Plus it could be more interesting than trying to make, say, a database.

    ### Bloodborne
    # One possible option would be to recreate everything about Javaborne in Python, in other words, basically abandon the Java version and start over in this language. The problem is, while I don't necessarily like Java, the whole point of building that game is to learn Java. So I will probably not do this. I don't want to ruin the steam on that project either.

    # Zorklike
    # However, another text based adventure game - and even one with a graphical component would be pretty interesting. I think I'm going to do this.


import sys
import player

def printArgs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))


def doSomething(pc):
    zoneStart = pc.zone.zoneID
    print(pc.zone.summary)

    while(zoneStart == pc.zone.zoneID):

        print("")
        for i in pc.zone.options:
            print(f"{pc.zone.options.index(i) + 1}: {i}")
        # print(pc.zone.options)
        print("\nWhat do you do?");
        choice = int(input())

        whatHappens = pc.zone.selection[choice]
        for key in whatHappens:
            if(key == "do"):
                print(whatHappens[key])
            elif(key == "takeItem"):
                pc.inventory[whatHappens[key]] = pc.zone.items[whatHappens[key]]
                pc.zone.items.pop(whatHappens[key])
                pc.globalStatus[f"{whatHappens[key]} taken"] = True
                break
            elif(key == "moveTo"):
                pc.zone.zoneID = whatHappens[key]
            elif(key == "pack"):
                print(whatHappens[key])
                for item in pc.inventory:
                    print(f"\n{item}:")
                    print(pc.inventory[item]["description"])
            else:
                print("Invalid selection.")
                break

        # print(pc.inventory)
        # print(pc.zone.zoneID)


def gameloop(pc):
    running = pc.isAlive
    while(running):

        if(pc.zone.zoneID == 0):
            print("The carriage drops you off, and the dust drifts thoughtlessly into the air leaving a stream of beige behind the team of horses and their dark wagon as the driver leaves you here alone. It is quiet.")
            doSomething(pc)

        elif(pc.zone.zoneID == 1):
            print("Before you stands a looming farmhouse, drab in its aged appearance. The darkened logs and fogged windows belie the tales of magic and adventure you have heard from your friend who is supposed to live here. You visited once, long ago, but that is now a mere memory, and what lies ahead are the echoes of a recent past, one which you do not remember. Something happened here. Where did she go? You recall the note from your friend which you tucked away in your backpack.")
            doSomething(pc)

        else:
            running = False





### GAME START

def dirtRoadStart(pc):
    continue
    # Introduction, carriage leaves
    # Cycle: Walk toward house, walk north or south (null), pick up hat
    # Item: Fancy Hat
    # GS: Fancy Hat taken

def dirtRoad(pc):
    continue
    # Upon returning to this area later to remove introduction flavor.
    # Cycle: Walk toward house, walk north or south (null), pick up hat
    # Item: Fancy Hat
    # GS: Fancy Hat taken





### FARMHOUSE ROOMS

def farmhouseFront(pc):
    continue
    # Looming farmhouse
    # Cycle: Walk into house, walk to backyard, walk to cornfield, walk back to road

def farmhouseKitchen(pc):
    continue
    # Dark kitchen, remnants of food recently abandoned.
    # Cycle: Closet, Sitting Room, Stairs up, examine signs of struggle
    # GS: Struggle examined

def farmhouseSittingRoom(pc):
    continue
    # Smoldering embers of a fire. A couple books. More signs of struggle. Weapon missing from wall.
    # Cycle: Walk to kitchen, upstairs
    # Item: Books

def farmhouseCloset1(pc):
    continue
    # Small front closet with work clothes and warm clothes (women's)
    # Cycle: Back to kitchen
    # Items: Boots (armor) & gloves (Puzzle item: armor + safely handle dangerous things)
    # GS: Boots taken, Gloves taken

def farmhouseStairsInside(pc):
    continue
    # Leads between first and second floors
    # Cycle: walk up or down the Stairs

def farmhouseHallway(pc):
    continue
    # Open hallway split in two, chest at far End
    # Cycle: Master, Guest, Closet, Storage, examine chest
    # Items in chest: Spellbook (need Int 13)
    # GS: Hallway Chest examined, Spellbook taken

def farmhouseCloset2(pc):
    continue
    # Small closet with more clothes
    # Cycle: Back to Hallway

def farmhouseMasterBedroom(pc):
    continue
    # Comfortable bed, fireplace directly above lower floor's fireplace. Chest of belongings (expensive stuff has been taken), more signs of Struggle
    # Cycle: Back to Hallway, to Study
    # Item: (Puzzle Item)
    # GS: Master Chest examined

def farmhouseGuestBedroom(pc):
    continue
    # Smaller bed, towels, sheets, pillows
    # Cycle: Back to Hallway, To Storage

def farmhouseStudy(pc):
    continue
    # Desk with books, chair, and small lantern. Bookshelf. Surprisingly in tact.
    # Cycle: Back to Master Bedroom
    # Items: Lantern, note
    # GS: Lantern taken, note taken

def farmhouseStorage(pc):
    continue
    # Extra sheets, bedspread stuff
    # Cycle: back to Guest bedroom
    # Item: Sheets (puzzle item)
    # GS: Sheets taken

def farmhouseStairsCellar(pc):
    continue
    # Stairs outside protected by a door
    # Cycle: Into Cellar, out to prairieBackyard, open / close the door
    # GS: Door opened (can be closed)

def farmhouseCellar(pc):
    continue
    # Dark, cold, and grey stone. Underground. No light at all. Jarred foods, gunpowder, alchmical ingredients and utensils
    # Cycle: Back to Stairs
    # Items: Gunpowder (puzzel item)
    # GS: Gunpowder taken





### PRAIRIE

def prairieBackyard(pc):
    continue
    # Open, view of scarecrow, leads to all other places (HUB)
    # Cycle: Well, Shed, Outhouse, barnFront, House Front, Cellar stairs, Cornfield

def prairieWell(pc):
    continue
    # Large handbuilt stone well. Tented roof. Rope pulley system for bucket. Water inside.
    # Cycle: Backyard, barnBack, outhouse, shed
    # Item: Bucket of water (puzzle item)
    # GS: Bucket taken

def prairieShedExterior(pc):
    continue
    # Dingy shack with sloped roof
    # Cycle: Enter shed, back to Backyard, Well, Outhouse, BarnFront

def prairieShedInterior(pc):
    continue
    # Filled with tools
    # Cycle: Shed exterior
    # Item: Tool of some kind?

def prairieOuthouse(pc):
    continue
    # It's an outhouse.
    # Cycle: Backyard, Well, Shed





### BARN

def barnFront(pc):
    continue
    # Same materials and style as house, Open windows high up, Large barn doors
    # Cycle: barnInterior, barnBack, Backyard, Well, Shed

def barnInterior(pc):
    continue

def barnLoft(pc):
    continue

def barnBack(pc):
    continue

def barnStable(pc):
    continue




### CORNFIELD


def cornfieldEdge(pc):
    continue

def cornfieldThick(pc):
    continue

def cornfieldTangle(pc):
    continue

def cornfieldMazeStart(pc):
    continue

def cornfieldMaze1(pc):
    continue

def cornfieldMaze2(pc):
    continue

def cornfieldMaze3(pc):
    continue

def cornfieldMaze4(pc):
    continue

def cornfieldMaze5(pc):
    continue

def cornfieldMaze6(pc):
    continue

def cornfieldMaze7(pc):
    continue

def cornfieldMaze8(pc):
    continue

def cornfieldMaze9(pc):
    continue

def cornfieldMazeCenter(pc):
    continue





if __name__ == "__main__":
    # print("Slither! - A Zorklike Game (WIP)");
    print("Testing")
    pc = player.Player()
    playing = True
    while (playing):
        gameloop(pc)
        playing = False





    # printArgs()
    # doSomething()

    # Zorklike (name pending)

    ### Scope:
    # To create a text based adventure game that is contained, and makes use of graphical features while rendering the graphics using ASCII text - just not in a terminal.

    ### Objectives:
    # - Learn to render a window
    # - Learn to output text to that window
    # - Create a small fantasy world
    # - Construct elements and objects for playing the Game
    # - Develop or steal an input method for text based input
    # - Have fun

    ### World / Story creation
    # I've always been partial to high fantasy, sword and sorcery style, with grand adventures. But for this I'd like to start small at least; Zork was one of my favorite text-based adventure games, and I think it provides some decent inspiration. The world felt somewhat large, but also simultaneously condensed and approachable. The house at the beginning always served as a good introduction to the mechanics - it had items, it had some puzzles for getting around / opening the trap door, and it even had a grue in the dark attic.
