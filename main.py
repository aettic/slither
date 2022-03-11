#!/usr/bin/python

# Slither v0.1 (Work in Progress)

# This file runs the core of the Slither engine, and accesses other adjacent classes.


import sys
from player import Player
from zones import Zone
import math
import json

def printTitle():
    print('\033[33m' + '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▄ █ ███▄██▄ ▄█ ████ ▄▄█ ▄▄▀████ ▄▄▄█ ▄▄▀█ ▄▄▄██▄██ ▄▄▀█ ▄▄██
██▄▄▄▀▀█ ███ ▄██ ██ ▄▄ █ ▄▄█ ▀▀▄████ ▄▄▄█ ██ █ █▄▀██ ▄█ ██ █ ▄▄██
██ ▀▀▀ █▄▄█▄▄▄██▄██▄██▄█▄▄▄█▄█▄▄████ ▀▀▀█▄██▄█▄▄▄▄█▄▄▄█▄██▄█▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ v0.1.3 ▀▀▀▀

   db     888888  888888  88""Yb  Yb  dY  88b 88   dP"Yb   .dP"Y8
  dPYb    88__      88    88__dP   YbdY   88Yb88  dY   Yb  `Ybo.
 dP__Yb   88""      88    88"Yb     88    88 Y88  Yb   dY  , `Y8b
dP""""Yb  888888    88    88  Yb    88    88  Y8   YbodP   8bodP' \n''' + '\033[0m')


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
                elif(key == "save"):
                    print("The game will be saved")
                    pc.saveState()
                else:
                    print("Invalid selection.")
                    break
        except ValueError:
            print("Please enter a valid selection.")
        except KeyError:
            print("Please enter a valid selection.")


def combat(pc, creature):
    combatRunning = True

    # introduce enemy
    print(f"A {creature.type} has appeared, {creature.description}.")

    while(combatRunning):

        # combat selections
        print(f"1 - Strike at the {creature.type}")
        print("2 - Stay on your guard")
        print("3 - Use an item")
        print("4 - Try to scare it off")
        print("5 - Run and hide")

        # take user selection
        print("What do you do?")

        try:
            choice = int(input())
        except ValueError:
            print("Enter a valid input")

def gameloop(pc):
    running = pc.isAlive

    # GAME START - should only play when game is launched
    pc.zone = Zone(pc.zoneID, pc)
    while(running):

        # each loop statement will play every time one enters that room. The descriptions should be split in two: first time, and post-acquaintance.

        ### STARTING ZONE ###-------------------------------------------------------------------- -|

        if(pc.zone.zoneID == 0):  # dirt road
            if (pc.globalStatus["Game Start"] == True):
                print("The carriage drops you off, and the dust drifts thoughtlessly into the air leaving a stream of beige behind the team of horses and their dark wagon as the driver leaves you here alone. It is quiet.")
            else:
                print("The road still lies barren and empty. The dust has settled.")
            dirtRoad(pc)
            pc.globalStatus["Game Start"] = False


        ### FARMHOUSE ZONES ###------------------------------------------------------------------ -|

        elif(pc.zone.zoneID == 1):
            if (pc.globalStatus["Farmhouse First Time"] == True):
                print("Before you stands a looming farmhouse, drab in its aged appearance. The darkened logs and fogged windows belie the tales of magic and adventure you have heard from your friend Alys, who is supposed to live here. You visited once, long ago, but that is now a mere memory, and what lies ahead are the echoes of a recent past, one which you do not remember. Something happened here. Where did she go? You recall Alys' note, which you have tucked away in your backpack.")
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
                print("You pull open the closet door, which squeaks with rusty hinges. Immediately, you spot two pairs of boots on the ground, mud now dried onto the wooden boards underneath. ")
            else:
                print(pc.zone.summary)
            farmhouseCloset1(pc)
            pc.globalStatus["Closet1 First Time"] = False

        elif(pc.zone.zoneID == 4):
            if (pc.globalStatus["Sitting Room First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseSittingRoom(pc)
            pc.globalStatus["Sitting Room First Time"] = False

        elif(pc.zone.zoneID == 5):
            if (pc.globalStatus["StairsInside First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseStairsInside(pc)
            pc.globalStatus["StairsInside First Time"] = False

        elif(pc.zone.zoneID == 6):
            if (pc.globalStatus["Hallway First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseHallway(pc)
            pc.globalStatus["Hallway First Time"] = False

        elif(pc.zone.zoneID == 7):
            if (pc.globalStatus["Closet2 First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseCloset2(pc)
            pc.globalStatus["Closet2 First Time"] = False

        elif(pc.zone.zoneID == 8):
            if (pc.globalStatus["Master Bedroom First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseMasterBedroom(pc)
            pc.globalStatus["Master Bedroom First Time"] = False

        elif(pc.zone.zoneID == 9):
            if (pc.globalStatus["Guest Bedroom First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseGuestBedroom(pc)
            pc.globalStatus["Guest Bedroom First Time"] = False

        elif(pc.zone.zoneID == 10):
            if (pc.globalStatus["Study First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseStudy(pc)
            pc.globalStatus["Study First Time"] = False

        elif(pc.zone.zoneID == 11):
            if (pc.globalStatus["Storage First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseStorage(pc)
            pc.globalStatus["Storage First Time"] = False

        elif(pc.zone.zoneID == 12):
            if (pc.globalStatus["StairsCellar First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseStairsCellar(pc)
            pc.globalStatus["StairsCellar First Time"] = False

        elif(pc.zone.zoneID == 13):
            if (pc.globalStatus["Cellar First Time"] == True):
                print("")
            else:
                print(pc.zone.summary)
            farmhouseCellar(pc)
            pc.globalStatus["Cellar First Time"] = False



        ### PRAIRIE ZONES ###-------------------------------------------------------------------- -|

        elif(pc.zone.zoneID == 14):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print(pc.zone.summary)
            prairieBackyard(pc)
            pc.globalStatus[""] = False

        elif(pc.zone.zoneID == 15):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print(pc.zone.summary)
            prairieWell(pc)
            pc.globalStatus[""] = False

        elif(pc.zone.zoneID == 16):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print(pc.zone.summary)
            prairieShedExterior(pc)
            pc.globalStatus[""] = False

        elif(pc.zone.zoneID == 17):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print(pc.zone.summary)
            prairieShedInterior(pc)
            pc.globalStatus[""] = False

        elif(pc.zone.zoneID == 18):
            if (pc.globalStatus[""] == True):
                print("")
            else:
                print(pc.zone.summary)
            prairieOuthouse(pc)
            pc.globalStatus[""] = False





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

    # Looming farmhouse
    # Cycle: Walk into house, walk to backyard, walk to cornfield, walk back to road

def farmhouseKitchen(pc):
    pc.zone = Zone(2, pc)
    doSomething(pc)

    # Dark kitchen, remnants of food recently abandoned.
    # Cycle: Closet, Sitting Room, Stairs up, examine signs of struggle
    # GS: Struggle examined

def farmhouseCloset1(pc):
    pc.zone = Zone(3, pc)
    doSomething(pc)

    # Small front closet with work clothes and warm clothes (women's)
    # Cycle: Back to kitchen
    # Items: Boots (armor) & gloves (Puzzle item: armor + safely handle dangerous things)
    # GS: Boots taken, Emerald Medallion in box

def farmhouseSittingRoom(pc):
    pc.zone = Zone(4, pc)
    doSomething(pc)

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
    # Items in chest: Spellbook (need Int 12)
    # GS: Hallway Chest examined, Spellbook taken

def farmhouseCloset2(pc):
    pc.zone = Zone(7, pc)
    doSomething(pc)
    pass
    # Small closet with more clothes
    # Cycle: Back to Hallway

def farmhouseMasterBedroom(pc):
    pc.zone = Zone(8, pc)
    doSomething(pc)
    pass
    # Comfortable bed, fireplace directly above lower floor's fireplace. Chest of belongings (expensive stuff has been taken), more signs of Struggle
    # Cycle: Back to Hallway, to Study
    # Item: (Puzzle Item)
    # GS: Master Chest examined

def farmhouseGuestBedroom(pc):
    pc.zone = Zone(9, pc)
    doSomething(pc)
    pass
    # Smaller bed, towels, sheets, pillows
    # Cycle: Back to Hallway, To Storage

def farmhouseStudy(pc):
    pc.zone = Zone(10, pc)
    doSomething(pc)
    pass
    # Desk with books, chair, and small lantern. Bookshelf. Surprisingly in tact.
    # Cycle: Back to Master Bedroom
    # Items: Lantern, note
    # GS: Lantern taken, note taken

def farmhouseStorage(pc):
    pc.zone = Zone(11, pc)
    doSomething(pc)
    pass
    # Extra sheets, bedspread stuff
    # Cycle: back to Guest bedroom
    # Item: Sheets (puzzle item)
    # GS: Sheets taken

def farmhouseStairsCellar(pc):
    pc.zone = Zone(12, pc)
    doSomething(pc)
    pass
    # Stairs outside protected by a door
    # Cycle: Into Cellar, out to prairieBackyard, open / close the door
    # GS: Door opened (can be closed)

def farmhouseCellar(pc):
    pc.zone = Zone(13, pc)
    doSomething(pc)
    pass
    # Dark, cold, and grey stone. Underground. No light at all. Jarred foods, gunpowder, alchmical ingredients and utensils
    # Cycle: Back to Stairs
    # Items: Gunpowder (puzzel item)
    # GS: Gunpowder taken





### PRAIRIE

def prairieBackyard(pc):
    pc.zone = Zone(14, pc)
    doSomething(pc)
    pass
    # Open, view of scarecrow, leads to all other places (HUB)
    # Cycle: Well, Shed, Outhouse, barnFront, House Front, Cellar stairs, Cornfield
    # GS: Bloodtrail examined (look)

def prairieWell(pc):
    pc.zone = Zone(15, pc)
    doSomething(pc)
    pass
    # Large handbuilt stone well. Tented roof. Rope pulley system for bucket. Water inside.
    # Cycle: Backyard, barnBack, outhouse, shed
    # Item: Bucket of water (puzzle item)
    # GS: Bucket taken

def prairieShedExterior(pc):
    pc.zone = Zone(16, pc)
    doSomething(pc)
    pass
    # Dingy shack with sloped roof
    # Cycle: Enter shed, back to Backyard, Well, Outhouse, BarnFront

def prairieShedInterior(pc):
    pc.zone = Zone(17, pc)
    doSomething(pc)
    pass
    # Filled with tools
    # Cycle: Shed exterior
    # Item: Tool of some kind?
    # GS: Tool taken

def prairieOuthouse(pc):
    pc.zone = Zone(18, pc)
    doSomething(pc)
    pass
    # It's an outhouse.
    # Cycle: Backyard, Well, Shed





### BARN

def barnFront(pc):
    pc.zone = Zone(19, pc)
    doSomething(pc)
    pass
    # Same materials and style as house, Open windows high up, Large barn doors
    # Cycle: barnInterior, barnBack, Backyard, Well, Shed

def barnInterior(pc):
    pc.zone = Zone(20, pc)
    doSomething(pc)
    pass
    # Floor made of hard packed dirt with scattered hay. A trail of blood leads out of one of the stables. Pitchfork on a support beam. No animals.
    # Cycle: barnFront, barnBack, barnStable, barnLoft
    # Item: Pitchfork (weapon)
    # GS: Pitchfork taken

def barnLoft(pc):
    pc.zone = Zone(21, pc)
    doSomething(pc)
    pass
    # Upper area, accessible by ladder from barnInterior. Stray cat startled and reflexes
    # Cycle: barnInterior
    # GS: Cat fled

def barnBack(pc):
    pc.zone = Zone(22, pc)
    doSomething(pc)
    pass
    # Outside the barn's back door, blood trail passs around the edges of the fields all the way to the cornfieldEdge
    # Cycle: barnInterior, barnStable, prairieBackyard
    # GS: Bloodtrail examined (automatically True)

def barnStable(pc):
    pc.zone = Zone(23, pc)
    doSomething(pc)
    pass
    # The rear of the interior, no animals present, but one stable shows clear signs of a struggle. Bloodtrail leads from the stable out into barnBack, and then prairieBackyard, as well as to cornfieldEdge
    # Cycle: barnBack, barnInterior
    # GS: Bloodtrail examined (automatically True)




### CORNFIELD


def cornfieldEdge(pc):
    pc.zone = Zone(24, pc)
    doSomething(pc)
    pass
    # The south end of the Cornfield, a wall of tall corn. On the far West side, a trail of blood can be seen once Bloodtrail examined is True.
    # Cycle: back to prairieBackyard, or prairieOuthouse, forward to cornfieldThick
    # GS: Bloodtrail examined (look)

def cornfieldThick(pc):
    pc.zone = Zone(25, pc)
    doSomething(pc)
    pass
    # First step into the corn. The corn is thicker and harder to move through
    # Cycle: Back to cornfieldEdge, forward to cornfieldTangle


def cornfieldTangle(pc):
    pc.zone = Zone(26, pc)
    doSomething(pc)
    pass
    # The corn is dense, and tangled, but there is a flash of movement
    # Cycle: Back to cornfieldThick. following the movement leads to cornfieldMazeStart.
    # GS: Flash of movement


def cornfieldMazeStart(pc):
    pc.zone = Zone(27, pc)
    doSomething(pc)
    pass
    # The corn thins out and opens into a clear path, two and a half feet wide. Plenty of space to walk comfortably.
    # Cycle: back to cornfieldTangle, forward to cornfieldMaze1

def cornfieldMaze1(pc):
    pc.zone = Zone(28, pc)
    doSomething(pc)
    pass
    # It becomes apparent that this is a corn maze, because the path branches into a T. Each maze leads to the next, and it's random which one it spits out to
    # Cycle: Right, Forward, Back

def cornfieldMaze2(pc):
    pc.zone = Zone(29, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Forward, Left, Back

def cornfieldMaze3(pc):
    pc.zone = Zone(30, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Left, Back

def cornfieldMaze4(pc):
    pc.zone = Zone(31, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Left 1, Left 2, Back

def cornfieldMaze5(pc):
    pc.zone = Zone(32, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right 1, Right 2, Back

def cornfieldMaze6(pc):
    pc.zone = Zone(33, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Forward, Left, Back

def cornfieldMaze7(pc):
    pc.zone = Zone(34, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right, Left, Back

def cornfieldMaze8(pc):
    pc.zone = Zone(35, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Right 1, Right 2, Back

def cornfieldMaze9(pc):
    pc.zone = Zone(36, pc)
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: Forward, Left, Back

def cornfieldMazeCenter(pc):
    pc.zone = Zone(37, pc)
    doSomething(pc)
    pass
    # The maze winds up eventually (4 - 15 moves) at the cornfieldMazeCenter, which is an open space. The dirt floor is a perfect circle inside the corn - almost like a crop circle, but in the middle is a spiral staircase leading down. It's important that getting here feels disorienting, and feels like a threshold has been crossed, leading to another world. This change can happen during the above maze instances, gradually. Will need 4 major progression dialogues.
    # Cycle: Back (immediately leads to cornfieldTangle, but coming back here involves going through the maze again). Down the stairs.
    # GS: Staircase examined (look)


def newGame():
    statsTuple = ("str", "dex", "int", "con")
    pointsLeft = 10
    creationRunning = True

    # Welcome
    print("Welcome to to the land of Corindos. Who are you? ")

    # Set name
    name = input()
    print(f"Hello, {name}. You have a pool of ten points to spend to increase your stats.")

    # Set player to Alive
    isAlive = True

    # Set currentZone to 0 for game opening
    startingZoneID = 0

    ### Create and spend points on stats
    # starting base stats
    stats = {
        "str": 8,  # strength and damage
        "dex": 8,  # maneuverability and reflexes
        "int": 8,  # perception and understanding
        "con": 8  # health and resillience
    }

    # Additional point allocation, based on pointsLeft
    for i in statsTuple:
        next = False
        if (pointsLeft > 0):
            while next == False:
                if (pointsLeft > 0):
                    print(f"\nCurrent {i}: {stats[i]}. Add [0 - {pointsLeft}]: ")
                    try:
                        readIn = int(input())
                        if (readIn <= pointsLeft and readIn >= 0):
                            stats[i] += readIn
                            pointsLeft -= readIn
                            print(f"new {i}: {stats[i]}")
                            next = True
                        else:
                            print(f"invalid input, please choose a number between [0 - {pointsLeft}]")
                    except ValueError:
                        print(f"invalid input, please choose a number between [0 - {pointsLeft}]")
                else:
                    next = True

        else:
            print(f"Current {i}: {stats[i]}. No more points to spend.")

    # Calculate derived stats (maxHP, currentHP, and damage)
    maxHP = stats["con"] + 2
    currentHP = int(maxHP)
    damage = math.ceil(stats["str"] / 5)
    weapon = {
        "weaponName": "bare hands",
        "baseDamage": 2
    }

    magic = math.ceil((stats["int"] / 2) - 4)

    # Set initial globalStatus variables to define the original values of a new game. These will get changed as the game is played, and should remain consistent throughout the whole game. ALL new globalStatus variables need to be published here first, and updated anywhere that they ought to be updated.
    globalStatus = {
        "Game Start": True,
        "Fancy Hat taken": False,
        "Farmhouse First Time": True,
        "Kitchen First Time": True,
        "Kitchen examined": False,
        "Closet1 First Time": True,
        "Muddy Boots taken": False,
        "Closet1 Box examined": False,
        "Emerald Medallion taken": False,
        "Sitting Room First Time": True,
        "StairsInside First Time": True,
        "Hallway First Time": True,
        "Master Bedroom First Time": True,
        "Guest Bedroom First Time": True,
        "Storage First Time": True,
        "Study First Time": True,
        "StairsCellar First Time": True
    }

    # Creates new inventory with note object
    inventory = {
        "Note": {
            "quantity": 1,
            "description": "A small note from your friend pleading for you to visit her at her farm. She seemed desparate, which is not like her. But she also seemed excited, as if she was on the verge of a great discovery.",
            "value": 0
        }
    }

    # Define newPlayer dictionary in same format as load, then return it.
    newPlayer = {
        "name": name,
        "isAlive": isAlive,
        "zoneID": startingZoneID,
        "stats": stats,
        "maxHP": maxHP,
        "currentHP": currentHP,
        "damage": damage,
        "globalStatus": globalStatus,
        "inventory": inventory,
        "weapon": weapon,
        "magic": magic
    }
    return newPlayer


def gameStart():
    print("\t1 - NEW GAME\n\t2 - CONTINUE")
    choice = int(input())

    if(choice == 2):
        return "CONTINUE"
    else:
        return "NEW GAME"


if __name__ == "__main__":

    # Slither Engine: Aetrynos
    # version 0.1.2
    printTitle()

    # Start menu for selecting gameStart option (new / continue)
    startOption = gameStart()
    if(startOption == "CONTINUE"):
        with open("saves/gameSave.json", encoding="utf-8") as file:
            continuePlayer = json.load(file)
        pc = Player(continuePlayer)
    else:
        pc = Player(newGame())

    # Begin the gameloop if player is alive
    gameloop(pc)
