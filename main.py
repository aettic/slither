#!/usr/bin/python

# Slither v0.1 (Work in Progress)

# This file runs the core of the Slither engine, and accesses other adjacent classes.


import sys
from player import Player
from zones import Zone

def printArgs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))


def doSomething(pc):
    zoneStart = pc.zone.zoneID
    print(pc.zone.summary)

    while(zoneStart == pc.zone.zoneID):
        pc.zone = Zone(zoneStart, pc)

        print("")
        for i in pc.zone.options:
            print(f"{pc.zone.options.index(i) + 1}: {i}")
        # print(pc.zone.options)
        print("\nWhat do you do?");

        try:
            choice = int(input())

            whatHappens = pc.zone.selection[choice]
            for key in whatHappens:
                if(key == "do"):
                    print(whatHappens[key])
                elif(key == "takeItem"):
                    pc.inventory[whatHappens[key]] = pc.zone.items.pop(whatHappens[key])
                    pc.globalStatus[f"{whatHappens[key]} taken"] = True
                    break
                elif(key == "moveTo"):
                    pc.zone.zoneID = whatHappens[key]
                elif(key == "pack"):
                    print(whatHappens[key])
                    for item in pc.inventory:
                        print(f"\n{item}:")
                        print(pc.inventory[item]["description"])
                elif(key == "examine"):
                    print(whatHappens[key])
                    pc.globalStatus[f"{whatHappens[key]} examined"] = True
                else:
                    print("Invalid selection.")
                    break
        except ValueError:
            print("Please enter a valid selection.")
        except KeyError:
            print("Please enter a valid selection.")


def gameloop(pc):
    running = pc.isAlive

    # GAME START - should only play when game is launched
    pc.zone = Zone(0, pc)
    while(running):

        # each loop statement will play every time one enters that room. The descriptions should be split in two: first time, and post-acquaintance.



        if(pc.zone.zoneID == 0):  # dirt road
            if (pc.globalStatus["Game Start"] == True):
                print("The carriage drops you off, and the dust drifts thoughtlessly into the air leaving a stream of beige behind the team of horses and their dark wagon as the driver leaves you here alone. It is quiet.")
            else:
                print("The road still lies barren and empty. The dust has settled. North and South the dirt path stretches on. To the West is the farmhouse, and to the East, the open countryside.")
            dirtRoad(pc)
            pc.globalStatus["Game Start"] = False


        ### FARMHOUSE ZONES

        elif(pc.zone.zoneID == 1):
            if (pc.globalStatus["Farmhouse First Time"] == True):
                print("Before you stands a looming farmhouse, drab in its aged appearance. The darkened logs and fogged windows belie the tales of magic and adventure you have heard from your friend Alys, who is supposed to live here. You visited once, long ago, but that is now a mere memory, and what lies ahead are the echoes of a recent past, one which you do not remember. Something happened here. Where did she go? You recall Alys' note, which you tucked have away in your backpack.")
            else:
                print("You stand in front of the farmstead home, darkened with abandon. Behind the farm is a prairie with several structures including a well, an outhouse, a shed, and a large barn. On the far North of the property is a large cornfield.")
            farmhouseFront(pc)
            pc.globalStatus["Farmhouse First Time"] = False

        elif(pc.zone.zoneID == 2):
            if (pc.globalStatus["Kitchen First Time"] == True):
                print("The door creaks open as you enter the kitchen of this home. The dry light of evening gently illuminating a diner table that is still set, plates with only scraps of food left, silverware scattered around, and even on the ground. Past the dining room table is a sitting room, and to the right is a closet door. The far back of this floor is home to a staircase heading upstairs.")
            else:
                print(pc.zone.summary)
            farmhouseKitchen(pc)
            pc.globalStatus["Kitchen First Time"] = False

        elif(pc.zone.zoneID == 3):
            if (pc.globalStatus["Closet1 First Time"] == True):
                print("")
            else:
                print("")
            farmhouseCloset1(pc)
            pc.globalStatus["Closet1 First Time"] = False

        elif(pc.zone.zoneID == 4):
            if (pc.globalStatus["Sitting Room First Time"] == True):
                print("")
            else:
                print("")
            farmhouseSittingRoom(pc)
            pc.globalStatus["Sitting Room First Time"] = False

        elif(pc.zone.zoneID == 5):
            if (pc.globalStatus["StairsInside First Time"] == True):
                print("")
            else:
                print("")
            farmhouseStairsInside(pc)
            pc.globalStatus["StairsInside First Time"] = False

        elif(pc.zone.zoneID == 6):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print("")
            farmhouseHallway(pc)

        elif(pc.zone.zoneID == 7):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print("")
            farmhouseCloset2(pc)

        elif(pc.zone.zoneID == 8):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print("")
            farmhouseMasterBedroom(pc)

        elif(pc.zone.zoneID == 9):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print("")
            farmhouseGuestBedroom(pc)

        elif(pc.zone.zoneID == 5):
            print("")
            farmhouseStudy(pc)

        elif(pc.zone.zoneID == 5):
            print("")
            farmhouseStorage(pc)

        elif(pc.zone.zoneID == 5):
            print("")
            farmhouseStairsCellar(pc)

        elif(pc.zone.zoneID == 5):
            print("")
            farmhouseCellar(pc)

        else:  # kill game
            running = False





### DIRT ROAD

def dirtRoad(pc):
    pc.zone = Zone(0, pc)
    doSomething(pc)

    pass
    # Upon returning to this area later to remove introduction flavor.
    # Cycle: Walk toward house, walk north or south (null), pick up hat
    # Item: Fancy Hat
    # GS: Fancy Hat taken





### FARMHOUSE ROOMS

def farmhouseFront(pc):
    pc.zone = Zone(1, pc)
    doSomething(pc)

    pass
    # Looming farmhouse
    # Cycle: Walk into house, walk to backyard, walk to cornfield, walk back to road

def farmhouseKitchen(pc):
    pc.zone = Zone(2, pc)
    doSomething(pc)
    pass
    # Dark kitchen, remnants of food recently abandoned.
    # Cycle: Closet, Sitting Room, Stairs up, examine signs of struggle
    # GS: Struggle examined

def farmhouseCloset1(pc):
    pc.zone = Zone(3, pc)
    doSomething(pc)
    pass
    # Small front closet with work clothes and warm clothes (women's)
    # Cycle: Back to kitchen
    # Items: Boots (armor) & gloves (Puzzle item: armor + safely handle dangerous things)
    # GS: Boots taken, Gloves taken

def farmhouseSittingRoom(pc):
    pc.zone = Zone(4, pc)
    doSomething(pc)
    pass
    # Smoldering embers of a fire. A couple books. More signs of struggle. Weapon missing from wall.
    # Cycle: Walk to kitchen, upstairs
    # Item: Books (non removable)
    # GS: Books read

def farmhouseStairsInside(pc):
    pc.zone = Zone(5, pc)
    doSomething(pc)
    pass
    # Leads between first and second floors
    # Cycle: walk up or down the Stairs

def farmhouseHallway(pc):
    pc.zone = Zone(6, pc)
    doSomething(pc)
    pass
    # Open hallway split in two, chest at far End
    # Cycle: Master, Guest, Closet, Storage, examine chest
    # Items in chest: Spellbook (need Int 13)
    # GS: Hallway Chest examined, Spellbook taken

def farmhouseCloset2(pc):
    pc.zone = Zone(7, pc)
    doSomething(pc)
    pass
    # Small closet with more clothes
    # Cycle: Back to Hallway

def farmhouseMasterBedroom(pc):
    pass
    # Comfortable bed, fireplace directly above lower floor's fireplace. Chest of belongings (expensive stuff has been taken), more signs of Struggle
    # Cycle: Back to Hallway, to Study
    # Item: (Puzzle Item)
    # GS: Master Chest examined

def farmhouseGuestBedroom(pc):
    pass
    # Smaller bed, towels, sheets, pillows
    # Cycle: Back to Hallway, To Storage

def farmhouseStudy(pc):
    pass
    # Desk with books, chair, and small lantern. Bookshelf. Surprisingly in tact.
    # Cycle: Back to Master Bedroom
    # Items: Lantern, note
    # GS: Lantern taken, note taken

def farmhouseStorage(pc):
    pass
    # Extra sheets, bedspread stuff
    # Cycle: back to Guest bedroom
    # Item: Sheets (puzzle item)
    # GS: Sheets taken

def farmhouseStairsCellar(pc):
    pass
    # Stairs outside protected by a door
    # Cycle: Into Cellar, out to prairieBackyard, open / close the door
    # GS: Door opened (can be closed)

def farmhouseCellar(pc):
    pass
    # Dark, cold, and grey stone. Underground. No light at all. Jarred foods, gunpowder, alchmical ingredients and utensils
    # Cycle: Back to Stairs
    # Items: Gunpowder (puzzel item)
    # GS: Gunpowder taken





### PRAIRIE

def prairieBackyard(pc):
    pass
    # Open, view of scarecrow, leads to all other places (HUB)
    # Cycle: Well, Shed, Outhouse, barnFront, House Front, Cellar stairs, Cornfield
    # GS: Bloodtrail examined (look)

def prairieWell(pc):
    pass
    # Large handbuilt stone well. Tented roof. Rope pulley system for bucket. Water inside.
    # Cycle: Backyard, barnBack, outhouse, shed
    # Item: Bucket of water (puzzle item)
    # GS: Bucket taken

def prairieShedExterior(pc):
    pass
    # Dingy shack with sloped roof
    # Cycle: Enter shed, back to Backyard, Well, Outhouse, BarnFront

def prairieShedInterior(pc):
    pass
    # Filled with tools
    # Cycle: Shed exterior
    # Item: Tool of some kind?
    # GS: Tool taken

def prairieOuthouse(pc):
    pass
    # It's an outhouse.
    # Cycle: Backyard, Well, Shed





### BARN

def barnFront(pc):
    pass
    # Same materials and style as house, Open windows high up, Large barn doors
    # Cycle: barnInterior, barnBack, Backyard, Well, Shed

def barnInterior(pc):
    pass
    # Floor made of hard packed dirt with scattered hay. A trail of blood leads out of one of the stables. Pitchfork on a support beam. No animals.
    # Cycle: barnFront, barnBack, barnStable, barnLoft
    # Item: Pitchfork (weapon)
    # GS: Pitchfork taken

def barnLoft(pc):
    pass
    # Upper area, accessible by ladder from barnInterior. Stray cat startled and reflexes
    # Cycle: barnInterior
    # GS: Cat fled

def barnBack(pc):
    pass
    # Outside the barn's back door, blood trail passs around the edges of the fields all the way to the cornfieldEdge
    # Cycle: barnInterior, barnStable, prairieBackyard
    # GS: Bloodtrail examined (automatically True)

def barnStable(pc):
    pass
    # The rear of the interior, no animals present, but one stable shows clear signs of a struggle. Bloodtrail leads from the stable out into barnBack, and then prairieBackyard, as well as to cornfieldEdge
    # Cycle: barnBack, barnInterior
    # GS: Bloodtrail examined (automatically True)




### CORNFIELD


def cornfieldEdge(pc):
    pass
    # The south end of the Cornfield, a wall of tall corn. On the far West side, a trail of blood can be seen once Bloodtrail examined is True.
    # Cycle: back to prairieBackyard, or prairieOuthouse, forward to cornfieldThick
    # GS: Bloodtrail examined (look)

def cornfieldThick(pc):
    pass
    # First step into the corn. The corn is thicker and harder to move through
    # Cycle: Back to cornfieldEdge, forward to cornfieldTangle


def cornfieldTangle(pc):
    pass
    # The corn is dense, and tangled, but there is a flash of movement
    # Cycle: Back to cornfieldThick. following the movement leads to cornfieldMazeStart.
    # GS: Flash of movement


def cornfieldMazeStart(pc):
    pass
    # The corn thins out and opens into a clear path, two and a half feet wide. Plenty of space to walk comfortably.
    # Cycle: back to cornfieldTangle, forward to cornfieldMaze1

def cornfieldMaze1(pc):
    pass
    # It becomes apparent that this is a corn maze, because the path branches into a T. Each maze leads to the next, and it's random which one it spits out to
    # Cycle: Right, Forward, Back

def cornfieldMaze2(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Forward, Left, Back

def cornfieldMaze3(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Left, Back

def cornfieldMaze4(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Left 1, Left 2, Back

def cornfieldMaze5(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right 1, Right 2, Back

def cornfieldMaze6(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Forward, Left, Back

def cornfieldMaze7(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Left, Back

def cornfieldMaze8(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right 1, Right 2, Back

def cornfieldMaze9(pc):
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Forward, Left, Back

def cornfieldMazeCenter(pc):
    pass
    # The maze winds up eventually (4 - 15 moves) at the cornfieldMazeCenter, which is an open space. The dirt floor is a perfect circle inside the corn - almost like a crop circle, but in the middle is a spiral staircase leading down. It's important that getting here feels disorienting, and feels like a threshold has been crossed, leading to another world. This change can happen during the above maze instances, gradually. Will need 4 major progression dialogues.
    # Cycle: Back (immediately leads to cornfieldTangle, but coming back here involves going through the maze again). Down the stairs.
    # GS: Staircase examined (look)





if __name__ == "__main__":
    # print("Slither! - A Zorklike Game (WIP)");
    print("Testing")
    pc = Player()
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
    # --- Create a small fantasy world ---
    # - Construct elements and objects for playing the Game
    # - Have fun

    ### World / Story creation
    # I've always been partial to high fantasy, sword and sorcery style, with grand adventures. But for this I'd like to start small at least; Zork was one of my favorite text-based adventure games, and I think it provides some decent inspiration. The world felt somewhat large, but also simultaneously condensed and approachable. The house at the beginning always served as a good introduction to the mechanics - it had items, it had some puzzles for getting around / opening the trap door, and it even had a grue in the dark attic.
