#!/usr/bin/python
# Slither v0.1 (Work in Progress)
# This file runs the core of the Slither engine, and accesses other adjacent classes.


from creature import Creature
from item import Item
from player import Player
from zones import Zone
import json
import math
import os
import random
import sys


def printTitle():
    print(f'\033[{random.choice([31, 32, 33, 34, 35, 36, 37, 38, 39])}m' + '''
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▄ █ ███▄██▄ ▄█ ████ ▄▄█ ▄▄▀████ ▄▄▄█ ▄▄▀█ ▄▄▄██▄██ ▄▄▀█ ▄▄██
██▄▄▄▀▀█ ███ ▄██ ██ ▄▄ █ ▄▄█ ▀▀▄████ ▄▄▄█ ██ █ █▄▀██ ▄█ ██ █ ▄▄██
██ ▀▀▀ █▄▄█▄▄▄██▄██▄██▄█▄▄▄█▄█▄▄████ ▀▀▀█▄██▄█▄▄▄▄█▄▄▄█▄██▄█▄▄▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ v0.1.9 ▀▀▀▀

   db     888888  888888  88""Yb  Yb  dY  88b 88   dP"Yb   .dP"Y8
  dPYb    88__      88    88__dP   YbdY   88Yb88  dY   Yb  `Ybo.
 dP__Yb   88""      88    88"Yb     88    88 Y88  Yb   dY    `Y8b
dP""""Yb  888888    88    88  Yb    88    88  Y8   YbodP   '8bodP'''
+ '\n \033[0m')


def doSomething(pc):
    currentZoneID = pc.zone.zoneID
    # print(pc.zone.summary)

    while(currentZoneID == pc.zoneID):

        pc.zone = Zone(currentZoneID, pc)

        if (pc.isAlive == False):
            running = False
            break

        print("")
        for i in pc.zone.options:
            print(f"{pc.zone.options.index(i) + 1}: {i}")

        try:
            choice = int(input("\nWhat do you do?\n> "))

            whatHappens = pc.zone.selection[choice]
            for key in whatHappens:
                if(key == "do"):
                    print(whatHappens[key])
                elif(key == "examine"):
                    pc.globalStatus[f"{whatHappens[key]} examined"] = True
                elif(key == "menu"):
                    pc.menu()
                elif(key == "moveTo"):
                    pc.zoneID = whatHappens[key]
                elif(key == "read"):
                    print(whatHappens[key])
                elif(key == "takeItem"):
                    pc.inventory.append(pc.zone.items.pop(pc.zone.items.index(whatHappens[key])))
                    pc.globalStatus[f"{Item(whatHappens[key]).name} taken"] = True
                    break
                elif(key == "toggle"):
                    pc.globalStatus[f"{whatHappens[key]} toggle"] = not pc.globalStatus[f"{whatHappens[key]} toggle"]
                else:
                    print("\n\t:: INVALID SELECTION ::")
                    break
        except ValueError:
            print("\n\t:: PLEASE ENTER A VALID SELECTION ::")
        except KeyError:
            print("\n\t:: PLEASE ENTER A VALID SELECTION ::")
        except KeyboardInterrupt:
            exitScreen()

        # timers (matches and grue spawn)
        if(pc.globalStatus["Match Lit"] == True):
            pc.matchTimer += 1
        else:
            pc.matchTimer = 0

        if(pc.matchTimer == 5):
            pc.globalStatus["Match Lit"] = False
            print("The match burns up, and its light and warmth are gone.")
            pc.matchTimer = 0

        if(pc.globalStatus["Dark"] == True and pc.globalStatus["Dark Place"] == True):
            pc.darknessTimer += 1
        else:
            pc.darknessTimer = 0

        if(pc.darknessTimer == 3):
            grue = Creature("Grue")
            combat(pc, grue)

        pc.globalStatus["Dark"] = False

def combat(pc, enemy):
    combatRunning = True

    # introduce enemy
    print("\n\t# ENCOUNTER #")
    print(f"A {enemy.type} has appeared, {enemy.description}.")

    while(combatRunning):

        # combat selections
        print(f"1: Strike at the {enemy.type}")
        print("2: Stay on your guard")
        print("3: Use an item")
        print("4: Try to scare it off")
        print("5: Run and hide")

        # take user selection
        try:
            choice = int(input("\nWhat do you do?\n> "))

            if (choice == 1):
                enemy.attack(pc)
                pc.attack(enemy)
            elif(choice == 2):
                print("You stand firm.")
                pc.defense += 3
                enemy.attack(pc)
                pc.defense -= 3
            elif(choice == 3):
                pc.viewInventory()
                enemy.attack(pc)
            elif(choice == 4):
                print("You attempt to scare off the creature.")
                combatRunning = pc.intimidate(enemy)
            elif(choice == 5):
                print("You flee the combat.")
                combatRunning = False

            else:
                print("WIP")

            print(f"\n{pc.name}: [{pc.currentHP} / {pc.maxHP}], {enemy.type}: [{enemy.currentHP} / {enemy.maxHP}]")

            if(not pc.isAlive or not enemy.isAlive):
                combatRunning = False

        except ValueError:
            print("Enter a valid input")
        except KeyboardInterrupt:
            exitScreen()

def gameloop(pc):
    running = pc.isAlive

    # GAME START - should only play when game is launched
    while(running):
        if (pc.isAlive == False):
            running = False
            break

        pc.zone = Zone(pc.zoneID, pc)
        # each loop statement will play every time one enters that room. The descriptions should be split in two: first time, and post-acquaintance.




# |- ------ ROOM LOOPS -------------------------------------------------------------------------- -|

        ### STARTING ZONE ###-------------------------------------------------------------------- -|

        if(pc.zone.zoneID == 0):  # dirt road
            if (pc.globalStatus["Game Start"] == True):
                input("\n\t# ENTER TO START GAME #")

                print('''\nYears ago, when you lived in the town of Almyth, there was a
Strong sense of community. In many ways, it felt like you
mattered to the people you called friends and neighbors. They
were family. After you moved out toward bigger and better
things in the city of Cormandyr, there was a sense of betrayal.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nYes, certainly a sense that your trust had been abused by
those who you called family, who no longer kept in touch. But
also a sense that you were guilty of the same abuse. Did you
ever write? Of course not. The only person you kept in touch
with was Alys Astraniela. So named because of her family's
ties to staring up at the stars, and wondering.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nAlys and her son worked their family's farm, her
parents had both gone years ago, and her husband had left for
the war, but has not returned and the two of them were
all that remained of their nightsky-infatuated family. She
made a point to always return your letters, and in some
ways you felt it was because she was growing lonely. Her
son, Dareth, was a good lad, but surely you'd get sick of
anyone you were stuck with.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nAbout a week ago, you received the most recent letter from
Alys, one that you'd almost hope hadn't been written. In it,
she seemed nearly desparate, and implored you to travel back
out to the countryside and visit her. She had so much to show
you! She was on the verge of unlocking some kind of great
discovery, and she wanted to share this with you, her friend.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nWith some hesitation, but a sense of wonder about you, you
organized to take a carriage out of the city to her farm in
the countryside. The carriage ride was bumpy after a while as
the even cobbled roads unfurled into haphazard dirt trails
beaten by wagon tracks and horseshoes.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nAfter a while, your driver yells back to you that you've
arrived, and nestled on the side of the road you cannot miss
the quaint farmstead that lies before you.\n''')
                input("\t# ENTER TO CONTINUE #")

                print('''\nThe carriage drops you off, and the dust drifts thoughtlessly
into the air leaving a stream of beige behind the team of
horses and their dark wagon as the driver leaves you here
alone. It is quiet.\n''')
                input("\t# ENTER TO CONTINUE #")

            else:
                print("\nThe road still lies barren and empty. The dust has settled.")
            dirtRoad(pc)
            pc.globalStatus["Game Start"] = False


        ### FARMHOUSE ZONES ###------------------------------------------------------------------ -|

        elif(pc.zone.zoneID == 1):
            print("\n\t# FARMHOUSE #")
            if (pc.globalStatus["farmhouseFront first time"] == True):
                print('''Before you stands a looming farmhouse, drab in its aged appearance.
The darkened logs and fogged windows belie the tales of magic
and adventure you have heard from your friend Alys, who is
supposed to live here. You visited once, long ago, but that
is now a mere memory, and what lies ahead are the echoes of
a recent past, one which you do not remember. Something happened
here. Where did she go? You recall Alys' note, which you have
tucked away in your backpack.''')
            else:
                print(pc.zone.summary)
            farmhouseFront(pc)
            pc.globalStatus["farmhouseFront first time"] = False

        elif(pc.zone.zoneID == 2):
            print("\n\t# KITCHEN #")
            if (pc.globalStatus["farmhouseKitchen first time"] == True):
                print('''The door creaks open as you enter the kitchen of this home. The
dry light of evening gently illuminating a dinner table that is
still set, plates with only scraps of food left, silverware
scattered around, and even on the ground. Past the dining room
table is a sitting room, and to the right is a closet door. The
far back of this floor is home to a staircase heading upstairs.''')
            else:
                print(pc.zone.summary)
            farmhouseKitchen(pc)
            pc.globalStatus["farmhouseKitchen first time"] = False

        elif(pc.zone.zoneID == 3):
            print("\n\t# FRONT CLOSET #")
            if (pc.globalStatus["farmhouseCloset1 first time"] == True):
                print('''The door squeaks with rusty hinges. Immediately, you spot two
pairs of boots on the ground, mud now dried onto the wooden
boards underneath.''')
            else:
                print(pc.zone.summary)
            farmhouseCloset1(pc)
            pc.globalStatus["farmhouseCloset1 first time"] = False

        elif(pc.zone.zoneID == 4):
            print("\n\t# SITTING ROOM #")
            if (pc.globalStatus["farmhouseSittingRoom first time"] == True):
                print('''This sitting room would come off as still, and almost peaceful,
were it not for the tumbled pile of books in the corner, or the
scattered dust, dashed from the fireplace. A pair of comfy
looking chairs sit cozily huddled in the center, facing that
fireplace. The stairs spiral up behind them. The kitchen isn't
too far away.''')
            else:
                print(pc.zone.summary)
            farmhouseSittingRoom(pc)
            pc.globalStatus["farmhouseSittingRoom first time"] = False

        elif(pc.zone.zoneID == 5):
            print("\n\t# FARMHOUSE STAIRS #")
            if (pc.globalStatus["farmhouseStairsInside first time"] == True):
                print('''This spiral staircase with a tight railing feels solid under
your feet, yet its boards creak nonetheless. It leads up to
the second floor.''')
            else:
                print(pc.zone.summary)
            farmhouseStairsInside(pc)
            pc.globalStatus["farmhouseStairsInside first time"] = False

        elif(pc.zone.zoneID == 6):
            print("\n\t# UPSTAIRS HALLWAY #")
            if (pc.globalStatus["farmhouseHallway first time"] == True):
                print('''Light filters in from stained glass windows at either end of the
hall, colored by the glass, motes of dust floating through
the hall. Two doors on either side of the hallway. The first
door on the left is open, and it seems to be a bedroom.''')
            else:
                print(pc.zone.summary)
            farmhouseHallway(pc)
            pc.globalStatus["farmhouseHallway first time"] = False

        elif(pc.zone.zoneID == 7):
            print("\n\t# BEDROOM CLOSET #")
            if (pc.globalStatus["farmhouseCloset2 first time"] == True):
                print('''This closet is narrow, packed with a variety of clothes and sheets.
A small spider scurries up the wall and disappears from sight.''')
            else:
                print(pc.zone.summary)
            farmhouseCloset2(pc)
            pc.globalStatus["farmhouseCloset2 first time"] = False

        elif(pc.zone.zoneID == 8):
            print("\n\t# ALYS' BEDROOM #")
            if (pc.globalStatus["farmhouseMasterBedroom first time"] == True):
                print('''This room seems untouched, unlike much of the rest of the
house. The bed is neatly made; a wide matress resting on an
ornately carved wooden frame, and there is a footlocker, shut.
There are shelves with books and knick-knacks, and a mounted
brass telescope pointing out the window, and up at the sky. To
the right is another door leading to an adjacent room.''')
            else:
                print(pc.zone.summary)
            farmhouseMasterBedroom(pc)
            pc.globalStatus["farmhouseMasterBedroom first time"] = False

        elif(pc.zone.zoneID == 9):
            print("\n\t# DARETH'S BEDROOM #")
            if (pc.globalStatus["farmhouseGuestBedroom first time"] == True):
                print('''Another bedroom, This one decorated with more reckless
abandon, clothes thrown into a corner, indicative of laziness,
not of a struggle. There is a door on one side, likely a closet.
There is also a sword mounted over the bed.''')
            else:
                print(pc.zone.summary)
            farmhouseGuestBedroom(pc)
            pc.globalStatus["farmhouseGuestBedroom first time"] = False

        elif(pc.zone.zoneID == 10):
            print("\n\t# STUDY #")
            if (pc.globalStatus["farmhouseStudy first time"] == True):
                print('''This room is darker than the bedroom itself, and contains one
large desk pressed up against the solid wooden wall. A narrow
window lets light in from the North. On the desk is a lantern,
and several handwritten notes.''')
            else:
                print(pc.zone.summary)
            farmhouseStudy(pc)
            pc.globalStatus["farmhouseStudy first time"] = False

        elif(pc.zone.zoneID == 11):
            print("\n\t# STORAGE CLOSET #")
            if (pc.globalStatus["farmhouseStorage first time"] == True):
                print('''Not much in here but blankets, pillows, sheets, and bags of hay
and feathers - probably used for stuffing.''')
            else:
                print(pc.zone.summary)
            farmhouseStorage(pc)
            pc.globalStatus["farmhouseStorage first time"] = False

        elif(pc.zone.zoneID == 12):
            print("\n\t# STAIRS TO THE CELLAR #")
            if (pc.globalStatus["farmhouseStairsCellar first time"] == True):
                print('''A wooden doubledoor rests over the cellar stairs, at a slight
angle, foretelling the imminent descent.''')
            else:
                if(pc.globalStatus["prairieWell first time"] == False):
                    combatChance = random.randint(1, 100)
                    if(combatChance >= 65 and combatChance < 80):
                        beast = Creature("Beast")
                        combat(pc, beast)
                    elif(combatChance >= 80):
                        goblin = Creature("Goblin")
                        combat(pc, goblin)
                print(pc.zone.summary)
            farmhouseStairsCellar(pc)
            pc.globalStatus["farmhouseStairsCellar first time"] = False

        elif(pc.zone.zoneID == 13):
            print("\n\t# FARMHOUSE CELLAR #")
            if (pc.globalStatus["farmhouseCellar first time"] == True):
                print('''Cold and somewhat damp, this stone cellar seems like a well-
deserved escape from the moderate heat of the summer day.''')
                if(pc.globalStatus["Dark"] == True):
                    print("It is dark...")
                else:
                    print("A faint glow illuminates this cellar. It is bright enough to get around safely.")
            else:
                print(pc.zone.summary)
                if(pc.globalStatus["Dark"] == True):
                    print("It is dark...")
                else:
                    print("A faint glow illuminates this cellar. It is bright enough to get around safely.")
            farmhouseCellar(pc)
            pc.globalStatus["farmhouseCellar first time"] = False




        ### PRAIRIE ZONES ###-------------------------------------------------------------------- -|

        elif(pc.zone.zoneID == 14):
            print("\n\t# BACKYARD PRAIRIE #")
            if (pc.globalStatus["prairieBackyard first time"] == True):
                print('''The backyard of the farmstead is a serene prairie which stretches
out for an acre or more. It's huge, and spacious. On the far West
side there is a small field which looks like it contains something
low: beans, or cabbage perhaps. In the midst of the field you spot
a figure... Upon closer inspection, that is a scarecrow. You can
better see the buildings you saw earlier: A shed, an outhouse, a
well not too far away, and a great big barn. There is a garden
nearby as well.''')
            else:
                if(pc.globalStatus["prairieWell first time"] == False):
                    combatChance = random.randint(1, 100)
                    if(combatChance >= 65 and combatChance < 80):
                        beast = Creature("Beast")
                        combat(pc, beast)
                    elif(combatChance >= 80):
                        goblin = Creature("Goblin")
                        combat(pc, goblin)
                print(pc.zone.summary)
            prairieBackyard(pc)
            pc.globalStatus["prairieBackyard first time"] = False

        elif(pc.zone.zoneID == 15):
            print("\n\t# WELL #")
            if (pc.globalStatus["prairieWell first time"] == True):
                print('''You approach a handmade well, beautiful in its simplistic crafts-
manship, and quaint. The tented wooden roof bows with age, and
the rope seems to hang taut, perhaps suspending a bucket. In
the distance, you can see the shed, the outhouse, the garden,
and the back of the barn.''')
                print('''Suddenly, you spot something moving at the rim of the well. It
becomes clear that something is climbing out of the well! Green
clawed hands, large eyes and mouth, pointy ears... This can only
be a Goblin. You've heard a lot about these, but never seen one.''')
                pc.globalStatus["Goblin seen"] = True
                goblin = Creature("Goblin")
                combat(pc, goblin)
            else:
                print(pc.zone.summary)
            prairieWell(pc)
            pc.globalStatus["prairieWell first time"] = False

        elif(pc.zone.zoneID == 16):
            print("\n\t# SHED #")
            if (pc.globalStatus["prairieShedExterior first time"] == True):
                print('''This sagging shack feels as if it might collapse at any moment,
yet it stands firm against the soft wind. You imagine you can
hear its creaking bones. The door is held fast with a large lock.''')
            else:
                combatChance = random.randint(1, 100)
                if(combatChance >= 65 and combatChance < 80):
                    beast = Creature("Beast")
                    combat(pc, beast)
                elif(combatChance >= 80):
                    goblin = Creature("Goblin")
                    combat(pc, goblin)
                print(pc.zone.summary)
            prairieShedExterior(pc)
            pc.globalStatus["prairieShedExterior first time"] = False

        elif(pc.zone.zoneID == 17):
            print("\n\t# INSIDE THE SHED #")
            if (pc.globalStatus["prairieShedInterior first time"] == True):
                print('''The inside of the shed is dim, and it's difficult to see in
much detail, but you can make out seveal tools propped up and hung
on walls. You can also see a stack of boxes on the ground, maybe
used for hauling vegetables to and fro.''')
            else:
                print(pc.zone.summary)
            prairieShedInterior(pc)
            pc.globalStatus["prairieShedInterior first time"] = False

        elif(pc.zone.zoneID == 18):
            print("\n\t# OUTHOUSE #")
            if (pc.globalStatus["prairieOuthouse first time"] == True):
                print('''Ah, the outhouse. It doesn't smell great, but it's not
overwhelming. This thin wooden building has a crescent moon cut
out of the door to let light in when it's closed.''')
            else:
                if(pc.globalStatus["prairieWell first time"] == False):
                    combatChance = random.randint(1, 100)
                    if(combatChance >= 65 and combatChance < 80):
                        beast = Creature("Beast")
                        combat(pc, beast)
                    elif(combatChance >= 80):
                        goblin = Creature("Goblin")
                        combat(pc, goblin)
                print(pc.zone.summary)
            prairieOuthouse(pc)
            pc.globalStatus["prairieOuthouse first time"] = False




        ### BARN ZONES ###----------------------------------------------------------------------- -|

        elif(pc.zone.zoneID == 19):
            print("\n\t# FRONT OF THE BARN #")
            if (pc.globalStatus["barnFront first time"] == True):
                print('''This barn is the same brown color as the house, no doubt made of
the same wood source; perhaps the trees of the nearby forest. The
large double doors are painted tan, like the front foor of the
farmstead. There are simple windows on either side of the door.
One of the doors is open, and it is quiet inside.''')
            else:
                if(pc.globalStatus["prairieWell first time"] == False):
                    combatChance = random.randint(1, 100)
                    if(combatChance >= 65 and combatChance < 80):
                        beast = Creature("Beast")
                        combat(pc, beast)
                    elif(combatChance >= 80):
                        goblin = Creature("Goblin")
                        combat(pc, goblin)
                print(pc.zone.summary)
            barnFront(pc)
            pc.globalStatus["barnFront first time"] = False

        elif(pc.zone.zoneID == 20):
            print("\n\t# INSIDE THE BARN #")
            if (pc.globalStatus["barnInterior first time"] == True):
                print('''The interior of the barn is strangely quiet. There are no animals
which strikes you as strange, because there are pens and stables
while they're not grazing. There is a distinctive animal smell,
a combination of sweat, and waste, and slop. Deeper inside, you
can see a ladder leading up to a darkened loft. At the back of
the barn are four stables where horses might once have slept.''')
            else:
                print(pc.zone.summary)
            barnInterior(pc)
            pc.globalStatus["barnInterior first time"] = False

        elif(pc.zone.zoneID == 21):
            print("\n\t# BARN LOFT #")
            if (pc.globalStatus["barnLoft first time"] == True):
                if(pc.globalStatus["Dark"] == True):
                    print('''The loft is dark, hay peeks out of the darkness and drifts back
toward the deepest recesses, where you cannot see. The space
large enough to move around, but it's too dark to make your way.''')
                else:
                    print('''Stacks of hay lie pressed up against the wall in this loft, and a
small desk can be seen huddled in the far corner. As you walk
around, the floor boards creak, and suddenly a black shape darts
out from the hay! You've startled a stray cat, and it flees down
the wall's support beams, and out of the barn.''')
            else:
                print(pc.zone.summary)
            barnLoft(pc)
            pc.globalStatus["barnLoft first time"] = False

        elif(pc.zone.zoneID == 22):
            print("\n\t# BACK OF THE BARN #")
            if (pc.globalStatus["barnBack first time"] == True):
                print('''Behind the barn is quiet, there's nothing back here except a
small path leading back to the Well, and eventually the garden.
You can see the tall line of trees not too far away, marking
the property boundary perhaps, and serving as a border into the
wild.''')
            else:
                print(pc.zone.summary)
            barnBack(pc)
            pc.globalStatus["barnBack first time"] = False

        elif(pc.zone.zoneID == 23):
            print("\n\t# STABLE #")
            if (pc.globalStatus["barnStable first time"] == True):
                print('''This small stable can hold 4 horses, but seems to hold none.
It's quite strange, the absence of animals. Where did they go?
There are hooks for leads, and there are saddles hung on the
wall. Clearly nobody rode the horses out of here, unless they
rode bareback.''')
            else:
                if(pc.globalStatus["barnStable first time"] == False):
                    combatChance = random.randint(1, 100)
                    if(combatChance >= 65 and combatChance < 90):
                        beast = Creature("Beast")
                        combat(pc, beast)
                    elif(combatChance >= 90):
                        goblin = Creature("Goblin")
                        combat(pc, goblin)
                print(pc.zone.summary)
            barnStable(pc)
            pc.globalStatus["barnStable first time"] = False




        ### CORNFIELD ZONES ###------------------------------------------------------------------ -|

        elif(pc.zone.zoneID == 24):
            print("\n\t# THE EDGE OF THE CORNFIELD #")
            if (pc.globalStatus["cornfieldEdge first time"] == True):
                print('''A long wall of corn stretches from East to West with the
setting sun. Each stalk nearly 7 feet tall, prime for harvest.
There is an order about the way they seem to be planted, though
this pattern seems wild and orchestrated by nature herself.''')
            else:
                print(pc.zone.summary)
            cornfieldEdge(pc)
            pc.globalStatus["cornfieldEdge first time"] = False

        elif(pc.zone.zoneID == 25):
            print("\n\t# INSIDE THE CORN #")
            if (pc.globalStatus["cornfieldThick first time"] == True):
                print('''The corn gets thicker here, and it's harder to move through.''')
            else:
                print(pc.zone.summary)
            cornfieldThick(pc)
            pc.globalStatus["cornfieldThick first time"] = False

        elif(pc.zone.zoneID == 26):
            print("\n\t# DEEPER INTO THE CORN #")
            if (pc.globalStatus["cornfieldTangle first time"] == True):
                print('''As you keep pushing, deeper, the corn becomes tangled and
you snare your foot on some kind of root. You free yourself, and
when you look up, you catch the backside of a small creature,
disappearing deeper into the corn. Its green skin and pointed
ears evoke the image of a goblin in your mind. Could this be
a goblin?''')
            else:
                print(pc.zone.summary)
            cornfieldTangle(pc)
            pc.globalStatus["cornfieldTangle first time"] = False

        elif(pc.zone.zoneID == 27):
            print("\n\t# CORN MAZE START #")
            if (pc.globalStatus["cornfieldMazeStart first time"] == True):
                print('''Looking around at the sheer walls and perfect aisle before you,
you are absolutely sure that you've stumbled upon a corn maze...
In the middle of the cornfield... A bit unorthodox, at any rate.
Before you, the path continues straight for several more feet.''')
            else:
                print(pc.zone.summary)
            cornfieldMazeStart(pc)
            pc.globalStatus["cornfieldMazeStart first time"] = False

        elif(pc.zone.zoneID == 28):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze1 first time"] == True):
                print('''It's quiet as you step into the aisle of corn walls, rows on both sides extending forward to a hard T in the distance.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze1(pc)
            pc.globalStatus["cornfieldMaze1 first time"] = False

        elif(pc.zone.zoneID == 29):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze2 first time"] == True):
                print('''Another intersection in ''')
            else:
                print(pc.zone.summary)
            cornfieldMaze2(pc)
            pc.globalStatus["cornfieldMaze2 first time"] = False

        elif(pc.zone.zoneID == 30):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze3 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze3(pc)
            pc.globalStatus["cornfieldMaze3 first time"] = False

        elif(pc.zone.zoneID == 31):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze4 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze4(pc)
            pc.globalStatus["cornfieldMaze4 first time"] = False

        elif(pc.zone.zoneID == 32):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze5 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze5(pc)
            pc.globalStatus["cornfieldMaze5 first time"] = False

        elif(pc.zone.zoneID == 33):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze6 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze6(pc)
            pc.globalStatus["cornfieldMaze6 first time"] = False

        elif(pc.zone.zoneID == 34):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze7 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze7(pc)
            pc.globalStatus["cornfieldMaze7 first time"] = False

        elif(pc.zone.zoneID == 35):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze8 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze8(pc)
            pc.globalStatus["cornfieldMaze8 first time"] = False

        elif(pc.zone.zoneID == 36):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze9 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze9(pc)
            pc.globalStatus["cornfieldMaze9 first time"] = False

        elif(pc.zone.zoneID == 37):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze10 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze10(pc)
            pc.globalStatus["cornfieldMaze10 first time"] = False

        elif(pc.zone.zoneID == 38):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze11 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze11(pc)
            pc.globalStatus["cornfieldMaze11 first time"] = False

        elif(pc.zone.zoneID == 39):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze12 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze12(pc)
            pc.globalStatus["cornfieldMaze12 first time"] = False

        elif(pc.zone.zoneID == 40):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze13 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze13(pc)
            pc.globalStatus["cornfieldMaze13 first time"] = False

        elif(pc.zone.zoneID == 41):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze14 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze14(pc)
            pc.globalStatus["cornfieldMaze14 first time"] = False

        elif(pc.zone.zoneID == 42):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze15 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze15(pc)
            pc.globalStatus["cornfieldMaze15 first time"] = False

        elif(pc.zone.zoneID == 43):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze16 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze16(pc)
            pc.globalStatus["cornfieldMaze16 first time"] = False

        elif(pc.zone.zoneID == 44):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze17 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze17(pc)
            pc.globalStatus["cornfieldMaze17 first time"] = False

        elif(pc.zone.zoneID == 45):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze18 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze18(pc)
            pc.globalStatus["cornfieldMaze18 first time"] = False

        elif(pc.zone.zoneID == 46):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze19 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze19(pc)
            pc.globalStatus["cornfieldMaze19 first time"] = False

        elif(pc.zone.zoneID == 47):
            print("\n\t# CORN MAZE #")
            if (pc.globalStatus["cornfieldMaze20 first time"] == True):
                print('''As you continue through the corn, you find another intersection.''')
            else:
                print(pc.zone.summary)
            cornfieldMaze20(pc)
            pc.globalStatus["cornfieldMaze20 first time"] = False

        elif(pc.zone.zoneID == 48):
            print("\n\t# CROP CIRCLE #")
            if (pc.globalStatus["cornfieldMazeCenter first time"] == True):
                print('''You spill out into a clearing, circular, and large in the middle of the this corn maze. The crops here have been pressed down in a spiral, creating a peculiar vortex of flattened corn in a perfect cirle. In the center of this crop circle, you see what appears to be the very top of a stone staircase, spiraling down into the ground.''')
            else:
                print(pc.zone.summary)
            cornfieldMazeCenter(pc)
            pc.globalStatus["cornfieldMazeCenter first time"] = False

        elif(pc.zone.zoneID == 49):
            endOfGame(pc)





        # kill game
        else:
            running = False

        print("----------------------------------------------------------------------")





# |- ------ ROOM FUNCTIONS ---------------------------------------------------------------------- -|

### DIRT ROAD

def dirtRoad(pc):
    pc.zone = Zone(0, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    pass
    # Upon returning to this area later to remove introduction flavor.
    # Cycle: Walk toward house, walk north or south (null), pick up hat
    # Item: Fancy Hat
    # GS: Fancy Hat taken


### FARMHOUSE ROOMS

def farmhouseFront(pc):
    pc.zone = Zone(1, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Looming farmhouse
    # Cycle: Walk into house, walk to backyard, walk to cornfield, walk back to road

def farmhouseKitchen(pc):
    pc.zone = Zone(2, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Dark kitchen, remnants of food recently abandoned.
    # Cycle: Closet, Sitting Room, Stairs up, examine signs of struggle
    # GS: Struggle examined

def farmhouseCloset1(pc):
    pc.zone = Zone(3, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Small front closet with work clothes and warm clothes (women's)
    # Cycle: Back to kitchen
    # Items: Boots (armor) & gloves (Puzzle item: armor + safely handle dangerous things)
    # GS: Boots taken, Emerald Pyramid Medallion in box

def farmhouseSittingRoom(pc):
    pc.zone = Zone(4, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Smoldering embers of a fire. A couple books. More signs of struggle. Weapon missing from wall.
    # Cycle: Walk to kitchen, upstairs
    # Item: Books (non removable)
    # GS: Books read

def farmhouseStairsInside(pc):
    pc.zone = Zone(5, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Leads between first and second floors
    # Cycle: walk up or down the Stairs

def farmhouseHallway(pc):
    pc.zone = Zone(6, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Open hallway split in two, chest at far End
    # Cycle: Master, Guest, Closet, Storage, examine chest
    # Items in chest: Spellbook (need Int 12)
    # GS: Hallway Chest examined, Spellbook taken

def farmhouseCloset2(pc):
    pc.zone = Zone(7, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Small closet with more clothes
    # Cycle: Back to Hallway

def farmhouseMasterBedroom(pc):
    pc.zone = Zone(8, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Comfortable bed, fireplace directly above lower floor's fireplace. Chest of belongings (expensive stuff has been taken), more signs of Struggle
    # Cycle: Back to Hallway, to Study
    # Item: Alcohol
    # GS: Master Chest examined

def farmhouseGuestBedroom(pc):
    pc.zone = Zone(9, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Smaller bed, towels, sheets, pillows
    # Cycle: Back to Hallway, To Storage

def farmhouseStudy(pc):
    pc.zone = Zone(10, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Desk with books, chair, and small lantern. Bookshelf. Surprisingly in tact.
    # Cycle: Back to Master Bedroom
    # Items: Lantern, note
    # GS: Lantern taken, note taken

def farmhouseStorage(pc):
    pc.zone = Zone(11, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Extra sheets, bedspread stuff
    # Cycle: back to Guest bedroom
    # Item: Sheets (puzzle item)
    # GS: Sheets taken

def farmhouseStairsCellar(pc):
    pc.zone = Zone(12, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Stairs outside protected by a door
    # Cycle: Into Cellar, out to prairieBackyard, open / close the door
    # GS: Door opened (can be closed)

def farmhouseCellar(pc):
    pc.zone = Zone(13, pc)
    pc.globalStatus["Dark Place"] = True
    doSomething(pc)

    # Dark, cold, and grey stone. Underground. No light at all. Jarred foods, gunpowder, alchmical ingredients and utensils
    # Cycle: Back to Stairs
    # Items: Gunpowder (puzzel item)
    # GS: Gunpowder taken


### PRAIRIE

def prairieBackyard(pc):
    pc.zone = Zone(14, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Open, view of scarecrow, leads to all other places (HUB)
    # Cycle: Well, Shed, Outhouse, barnFront, House Front, Cellar stairs, Cornfield
    # GS: Bloodtrail examined (look)

def prairieWell(pc):
    pc.zone = Zone(15, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Large handbuilt stone well. Tented roof. Rope pulley system for bucket. Water inside.
    # Cycle: Backyard, barnBack, outhouse, shed
    # Item: Bucket of water (puzzle item)
    # GS: Bucket taken

def prairieShedExterior(pc):
    pc.zone = Zone(16, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Dingy shack with sloped roof
    # Cycle: Enter shed, back to Backyard, Well, Outhouse, BarnFront

def prairieShedInterior(pc):
    pc.zone = Zone(17, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Filled with tools
    # Cycle: Shed exterior
    # Item: Acrid Solution
    # GS: Acrid Solution taken

def prairieOuthouse(pc):
    pc.zone = Zone(18, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # It's an outhouse.
    # Cycle: Backyard, Well, Shed


### BARN

def barnFront(pc):
    pc.zone = Zone(19, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Same materials and style as house, Open windows high up, Large barn doors
    # Cycle: barnInterior, barnBack, Backyard, Well, Shed

def barnInterior(pc):
    pc.zone = Zone(20, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Floor made of hard packed dirt with scattered hay. A trail of blood leads out of one of the stables. Pitchfork on a support beam. No animals.
    # Cycle: barnFront, barnBack, barnStable, barnLoft
    # Item: Pitchfork (weapon)
    # GS: Pitchfork taken

def barnLoft(pc):
    pc.zone = Zone(21, pc)
    pc.globalStatus["Dark Place"] = True
    doSomething(pc)

    # Upper area, accessible by ladder from barnInterior. Stray cat startled and reflexes
    # Cycle: barnInterior
    # GS: Cat fled

def barnBack(pc):
    pc.zone = Zone(22, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # Outside the barn's back door, blood trail passs around the edges of the fields all the way to the cornfieldEdge
    # Cycle: barnInterior, barnStable, prairieWell
    # GS: Bloodtrail examined (automatically True)

def barnStable(pc):
    pc.zone = Zone(23, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # The rear of the interior, no animals present, but one stable shows clear signs of a struggle. Bloodtrail leads from the stable out into barnBack, and then prairieBackyard, as well as to cornfieldEdge
    # Cycle: barnBack, barnInterior
    # Item: Brass Key
    # GS: Brass Key taken, Bloodtrail examined (automatically True)


### CORNFIELD

def cornfieldEdge(pc):
    pc.zone = Zone(24, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)
    # The south end of the Cornfield, a wall of tall corn. On the far West side, a trail of blood can be seen once Bloodtrail examined is True.
    # Cycle: back to prairieBackyard, or prairieOuthouse, forward to cornfieldThick
    # GS: Bloodtrail examined (look)

def cornfieldThick(pc):
    pc.zone = Zone(25, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # First step into the corn. The corn is thicker and harder to move through
    # Cycle: Back to cornfieldEdge, forward to cornfieldTangle

def cornfieldTangle(pc):
    pc.zone = Zone(26, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # The corn is dense, and tangled, but there is a flash of movement
    # Cycle: Back to cornfieldThick. following the movement leads to cornfieldMazeStart.
    # GS: Flash of movement

def cornfieldMazeStart(pc):
    pc.zone = Zone(27, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # The corn thins out and opens into a clear path, two and a half feet wide. Plenty of space to walk comfortably.
    # Cycle: back to cornfieldTangle, forward to cornfieldMaze1

def cornfieldMaze1(pc):
    pc.zone = Zone(28, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # It becomes apparent that this is a corn maze, because the path branches into an intersection. Each maze leads to the next. There are three different possibilities, determined at game start
    # Cycle: West, North, East

def cornfieldMaze2(pc):
    pc.zone = Zone(29, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)
    pass
    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East

def cornfieldMaze3(pc):
    pc.zone = Zone(30, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East, South

def cornfieldMaze4(pc):
    pc.zone = Zone(31, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East

def cornfieldMaze5(pc):
    pc.zone = Zone(32, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, East, South

def cornfieldMaze6(pc):
    pc.zone = Zone(33, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East, South

def cornfieldMaze7(pc):
    pc.zone = Zone(34, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, South

def cornfieldMaze8(pc):
    pc.zone = Zone(35, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: North, East, South

def cornfieldMaze9(pc):
    pc.zone = Zone(36, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East, South

def cornfieldMaze10(pc):
    pc.zone = Zone(37, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, East

def cornfieldMaze11(pc):
    pc.zone = Zone(38, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # It becomes apparent that this is a corn maze, because the path branches into a T. Each maze leads to the next, and it's random which one it spits out to
    # Cycle: West, North, East, South

def cornfieldMaze12(pc):
    pc.zone = Zone(39, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, East, South

def cornfieldMaze13(pc):
    pc.zone = Zone(40, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, East, South

def cornfieldMaze14(pc):
    pc.zone = Zone(41, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, East, South

def cornfieldMaze15(pc):
    pc.zone = Zone(42, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: North, East, South

def cornfieldMaze16(pc):
    pc.zone = Zone(43, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, South

def cornfieldMaze17(pc):
    pc.zone = Zone(44, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: North, East, South

def cornfieldMaze18(pc):
    pc.zone = Zone(45, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, South

def cornfieldMaze19(pc):
    pc.zone = Zone(46, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: North, East, South

def cornfieldMaze20(pc):
    pc.zone = Zone(47, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # More maze. Each maze leads to the next, and it's random which one it spits out to.
    # Cycle: West, North, South

def cornfieldMazeCenter(pc):
    pc.zone = Zone(48, pc)
    pc.globalStatus["Dark Place"] = False
    doSomething(pc)

    # The maze winds up eventually (4 - 15 moves) at the cornfieldMazeCenter, which is an open space. The dirt floor is a perfect circle inside the corn - almost like a crop circle, but in the middle is a spiral staircase leading down. It's important that getting here feels disorienting, and feels like a threshold has been crossed, leading to another world. This change can happen during the above maze instances, gradually. Will need 4 major progression dialogues.
    # Cycle: Back (immediately leads to cornfieldTangle, but coming back here involves going through the maze again). Down the stairs.
    # GS: Staircase examined (look)

def endOfGame(pc):
    # ten points for winning the game
    points = 10

    print(f'''Congratulations {pc.name}! You have successfully completed the
game as it stands, so far. Alys lies deep below, in a world
largely untouched by Human hands. It is perilous to continue, but
you have made the choice to descend into that realm, despite the
dangers that might lurk beyond. It is quite dark down there.\n''')

    print(f'''But that is a tale for another time. For now, it's time to
celebrate how far you have come. Winning a game, even one that
is only partially completed is still a great achievement, is it
not? You have achieved that, at least. What else have you done?\n''')

    print(f"You gained {pc.experience} Experience Points.")
    points += pc.experience

    valueTotal = 0
    for itemID in pc.inventory:
        valueTotal += Item(itemID).value

    print("You found items totalling (WIP) gold pieces in value")
    points += int(valueTotal)

    if(pc.globalStatus["Sword taken"] == True):
        print("You discovered Dareth's cherished blade.")
        points += 2

    if(pc.globalStatus["Liquid Darkness taken"] == True):
        print("You slew a Grue, and took its heart.")
        points += 10

    if(pc.globalStatus["Fancy Hat taken"] == True):
        print("You picked up an otherworldly headpiece.")
        points += 2

    if(pc.globalStatus["Emerald Merkaba taken"] == True):
        print("You found a mysterious star deep in a well.")
        points += 10

    if(pc.globalStatus["Telescope examined"] == True):
        print("You witnessed a miracle.")
        points += 3

    if(pc.globalStatus["Spellbook taken"] == True):
        print("You stumbled upon an esoteric tome.")
        points += 4

    if(pc.globalStatus["Hidden Note 1 taken"] == True):
        print("You found the first of Alys' hidden notes.")
        points += 1

    if(pc.globalStatus["Hidden Note 2 taken"] == True):
        print("You found the second of Alys' hidden notes.")
        points += 1

    if(pc.globalStatus["Hidden Note 3 taken"] == True):
        print("You found the third of Alys' hidden notes.")
        points += 1

    if(pc.globalStatus["Gold Coin taken"] == True):
        print("You found a shiny penny.")
        points += 3

    print(f"TOTAL: {points} POINTS")

    print("Congratulations, and thank you for playing!")
    pc.globalStatus["Game Won"] = True
    pc.globalStatus["Game Over"] = True
    pc.saveState()
    exitScreen()





def newGame():

    # Welcome
    print("Welcome to to the land of Aetrynos. Who are you?")

    # Set name
    try:
        name = input("> ")
    except KeyboardInterrupt:
        exitScreen()

    print(f'''Hello, {name}. Next, you will declare your starting stats.
There are four, each pertaining to a different aspect of life in
the world of Aetrynos. STRENGTH governs your ability to do damage
to enemies you encounter. DEXTERITY is a measure of your ability
to maneuver, and evade attacks. INTELLIGENCE describes your
intellect, and capacity for understanding the Arcane. And finally,
CONSTITUTION demonstrates your heartiness, and resilience.

You have a pool of ten points to spend to increase your stats,
but each starts at 9. You do not need to spend all the points in
your pool, but you only have this one chance, so spend them wisely.
Any remaining points might be useful... later on...''')

    statsTuple = ("STR", "DEX", "INT", "CON")
    pointsLeft = 10

    ### Create and spend points on stats
    # starting base stats
    stats = {
        "STR": 9,  # strength and damage
        "DEX": 9,  # maneuverability and reflexes
        "INT": 9,  # perception and understanding
        "CON": 9  # health and resillience
    }

    # Additional point allocation, based on pointsLeft
    for i in statsTuple:
        next = False
        if (pointsLeft > 0):
            while next == False:
                if (pointsLeft > 0):
                    print(f"\nCurrent {i}: {stats[i]}. Add [0 - {pointsLeft}]: ")
                    try:
                        readIn = int(input("> "))
                        if (readIn <= pointsLeft and readIn >= 0):
                            stats[i] += readIn
                            pointsLeft -= readIn
                            print(f"new {i}: {stats[i]}")
                            next = True
                        else:
                            print(f"invalid input, please choose a number between [0 - {pointsLeft}]")
                    except ValueError:
                        print(f"invalid input, please choose a number between [0 - {pointsLeft}]")
                    except KeyboardInterrupt:
                        exitScreen()
                else:
                    next = True

        else:
            print(f"Current {i}: {stats[i]}. No more points to spend.")

    # Calculate derived stats (maxHP, currentHP, and damage)
    maxHP = stats["CON"] + 2
    currentHP = int(maxHP)
    damage = math.ceil(stats["STR"] / 5)
    magic = math.ceil((stats["INT"] / 2) - 4)
    defense = math.ceil((stats["DEX"] / 5) - 1)
    experience = pointsLeft * 10

    # Creates new inventory
    inventory = [0]  # only Note from Alys
    # inventory = [0, 21]  # note and key
    # inventory = [0, 7, 9, 1, 12, 14, 15]  # testing all item types
    # inventory = [0, 7, 12, 16, 17, 18] # testing bomb

    # equippable slots
    weapon = [99] # start with knife equipped
    armor = []

    # Set currentZone to 0 for game opening
    startingZoneID = 0

    # Timers
    darknessTimer = 0  # timer for rounds spent in darkness
    matchTimer = 0  # timer for rounds with match lit

    # Select the maze path for later (All zone IDs are maze numbers + 27)
    mazeOptions = [
        [27, 28, 29, 31, 46, 44, 42, 36, 39, 40, 37, 38, 43, 45, 35, 48],
        [27, 28, 32, 33, 35, 38, 37, 36, 39, 42, 44, 34, 31, 32, 48],
        [27, 28, 29, 47, 33, 35, 45, 43, 41, 40, 37, 36, 34, 48]
    ]
    maze = random.choice([1, 2, 3])
    mazeKey = mazeOptions[maze - 1]

    # Set initial globalStatus variables to define the original values of a new game. These will get changed as the game is played, and should remain consistent throughout the whole game. ALL new globalStatus variables need to be published here first, and updated anywhere that they ought to be updated. All "first time" start at True, and as a general rule all "examine" and "talen" start at False. The appropriate user actions will change them as necessary.
    globalStatus = {
        # organize by category, and then label, alphabetically

        ### GAME CORE
        "Game Start": True,

        ### first time
        # barn
        "barnFront first time": True,
        "barnInterior first time": True,
        "barnLoft first time": True,
        "barnBack first time": True,
        "barnStable first time": True,

        # cornfield
        "cornfieldEdge first time": True,
        "cornfieldMaze1 first time": True,
        "cornfieldMaze2 first time": True,
        "cornfieldMaze3 first time": True,
        "cornfieldMaze4 first time": True,
        "cornfieldMaze5 first time": True,
        "cornfieldMaze6 first time": True,
        "cornfieldMaze7 first time": True,
        "cornfieldMaze8 first time": True,
        "cornfieldMaze9 first time": True,
        "cornfieldMaze10 first time": True,
        "cornfieldMaze11 first time": True,
        "cornfieldMaze12 first time": True,
        "cornfieldMaze13 first time": True,
        "cornfieldMaze14 first time": True,
        "cornfieldMaze15 first time": True,
        "cornfieldMaze16 first time": True,
        "cornfieldMaze17 first time": True,
        "cornfieldMaze18 first time": True,
        "cornfieldMaze19 first time": True,
        "cornfieldMaze20 first time": True,
        "cornfieldMazeCenter first time": True,
        "cornfieldMazeStart first time": True,
        "cornfieldThick first time": True,
        "cornfieldTangle first time": True,

        # farmhouse
        "farmhouseCellar first time": True,
        "farmhouseCloset1 first time": True,
        "farmhouseCloset2 first time": True,
        "farmhouseFront first time": True,
        "farmhouseGuestBedroom first time": True,
        "farmhouseHallway first time": True,
        "farmhouseKitchen first time": True,
        "farmhouseMasterBedroom first time": True,
        "farmhouseSittingRoom first time": True,
        "farmhouseStairsCellar first time": True,
        "farmhouseStairsInside first time": True,
        "farmhouseStorage first time": True,
        "farmhouseStudy first time": True,

        # prairie
        "prairieBackyard first time": True,
        "prairieShedExterior first time": True,
        "prairieShedInterior first time": True,
        "prairieWell first time": True,
        "prairieOuthouse first time": True,

        ### ITEMS TAKEN
        # f"{Item(itemID).name} taken" as format
        "Acrid Solution taken": False,
        "Alchemical Powder taken": False,
        "Alcohol taken": False,
        "Bottle of Ink taken": False,
        "Brass Key taken": False,
        "Emerald Pyramid taken": False,
        "Emerald Pyramid Medallion taken": False,
        "Emerald Merkaba taken": False,
        "Fancy Hat taken": False,
        "Glass Jar taken": False,
        "Gold Coin taken": False,
        "Hidden Note 1 taken": False,
        "Hidden Note 2 taken": False,
        "Hidden Note 3 taken": False,
        "Lantern taken": False,
        "Letter from Alys taken": False,
        "Liquid Darkness taken": False,
        "Matches taken": False,
        "Muddy Boots taken": False,
        "Pitchfork taken": False,
        "Spellbook taken": False,
        "Sword taken": False,

        ### EXAMINED
        # f"{location or item} examined" as format
        "barnFront examined": False,
        "barnInterior examined": False,
        "barnLoft examined": False,
        "barnBack examined": False,
        "barnStable examined": False,
        "barnStable stall3 examined": False,
        "cornfieldEdge examined": False,
        "cornfieldMaze1 examined": False,
        "cornfieldMaze2 examined": False,
        "cornfieldMaze3 examined": False,
        "cornfieldMaze4 examined": False,
        "cornfieldMaze5 examined": False,
        "cornfieldMaze6 examined": False,
        "cornfieldMaze7 examined": False,
        "cornfieldMaze8 examined": False,
        "cornfieldMaze9 examined": False,
        "cornfieldMaze10 examined": False,
        "cornfieldMaze11 examined": False,
        "cornfieldMaze12 examined": False,
        "cornfieldMaze13 examined": False,
        "cornfieldMaze14 examined": False,
        "cornfieldMaze15 examined": False,
        "cornfieldMaze16 examined": False,
        "cornfieldMaze17 examined": False,
        "cornfieldMaze18 examined": False,
        "cornfieldMaze19 examined": False,
        "cornfieldMaze20 examined": False,
        "cornfieldMazeCenter examined": False,
        "cornfieldMazeStart examined": False,
        "cornfieldThick examined": False,
        "cornfieldTangle examined": False,
        "dirtRoad examined": False,
        "farmhouseCellar examined": False,
        "farmhouseCloset1 Box examined": False,
        "farmhouseCloset2 examined": False,
        "farmhouseGuestBedroom examined": False,
        "farmhouseHallway examined": False,
        "farmhouseHallway Chest examined": False,
        "farmhouseKitchen examined": False,
        "farmhouseMasterBedroom examined": False,
        "farmhouseSittingRoom examined": False,
        "farmhouseSittingRoom Fireplace examined": False,
        "farmhouseStairsCellar examined": False,
        "farmhouseStudy examined": False,
        "farmhouseStorage examined": False,
        "prairieBackyard examined": False,
        "prairieOuthouse examined": False,
        "prairieShedExterior examined": False,
        "prairieShedExterior Lock examined": False,
        "prairieShedInterior Boxes examined": False,
        "prairieShedInterior examined": False,
        "prairieWell examined": False,
        "prairieWell Inside": False,
        "Study Notes examined": False,
        "Telescope examined": False,

        ### STATUS EFFECTS
        # toggle effects
        "Damage Enchanted": False,
        "Darkvision": False,
        "Lantern Lit": False,
        "Match Lit": False,
        "Stelthy": False,

        # environment effects
        "Dark": False,
        "Dark Place": False,
        "Goblin seen": False,
        "prairieShedExterior Unlocked toggle": False,
        "prairieWell obstruction destroyed": False,
        "Staircase Visible": False,

        ### GAME END
        "Game Won": False,
        "Game Over": False

    }

    # Set player to Alive
    isAlive = True

    # Define newPlayer dictionary in same format as load, then return it.
    newPlayer = {
        "armor": armor,  # player's armor (release: 0 - Clothes)
        "currentHP": currentHP,  # current HP, starts the same as Max
        "damage": damage,  # the player's base damage range, determined by STR
        "darknessTimer": darknessTimer,  # used for measuring time spent in the dark
        "defense": defense,  # the player's defenses, based on DEX
        "experience": experience,  # running experience points for advancement and leveling up
        "globalStatus": globalStatus,  # a huge dictionary of all GS booleans
        "inventory": inventory,  # the starting inventory (release: 0)
        "isAlive": isAlive,  # the player starts alive, if this becomes false, Game Over
        "magic": magic,  # the player's magical attunement, based on INT
        "matchTimer": matchTimer,  # used to track how long a match is burning
        "maxHP": maxHP,  # the player's maximum HP, based on CON
        "maze": maze,  # the number of the maze version
        "mazeKey": mazeKey,  # the specific path for the generated maze
        "name": name,  # the player's name
        "stats": stats,  # the player's stats / attributes (STR, DEX, INT, CON)
        "weapon": weapon,  # the player's weapon (release: 99 - knife)
        "zoneID": startingZoneID  # Choose where play starts (release: 0)
    }

    return newPlayer


def gameStart():
    print("\t\t\t  1 - NEW GAME\n\t\t\t  2 - CONTINUE\n")

    try:
        choice = input("> ")

        if(int(choice) == 2):
            return "CONTINUE"
        elif(int(choice) == 1):
            return "NEW GAME"

    except KeyboardInterrupt:
        exitScreen()


def exitScreen():
    print(f'\033[{random.choice([31, 32, 33, 34, 35, 36, 37, 38, 39])}m' + """\n\n
   ..|'''.|                      '|| '||
  .|'     '    ...     ...     .. ||  || ...  .... ...  ....
  ||    .... .|  '|. .|  '|. .'  '||  ||'  ||  '|.  | .|...||
  '|.    ||  ||   || ||   || |.   ||  ||    |   '|.|  ||
   ''|...'|   '|.|'   '|.|'  '|..'||. '|...'     '|    '|...'
                                              .. |
                                               ''              """ + '\n \033[0m')
    quit()


if __name__ == "__main__":

    # Slither Engine: Aetrynos
    # version 0.1.3
    printTitle()

    # Start menu for selecting gameStart option (new / continue)
    startOption = gameStart()
    if(startOption == "CONTINUE"):
        with open("src/saves/gameSave.json", encoding="utf-8") as file:
            continuePlayer = json.load(file)
        pc = Player(continuePlayer)
    else:
        pc = Player(newGame())

    pc.viewStats()


    #goblin = Creature("Goblin")
    #combat(pc, goblin)

    # Begin the gameloop if player is alive
    gameloop(pc)
