import math
import zones

class Player:
    def __init__(self):

        # base stats
        self.stats = {
            "str": 8,  # strength and damage
            "dex": 8,  # maneuverability and reflexes
            "int": 8,  # perception and understanding
            "con": 8  # health and resillience
        }

        # initialize character creator to select stats
        self.characterCreation()

        # set starting room to 0 for opening scene
        self.zoneID = 0

        self.inventory = {
            "Note": {
                "quantity": 1,
                "description": "A small note from your friend pleading for you to visit her at her farm. She seemed desparate, which is not like her. But she also seemed excited, as if she was on the verge of a great discovery.",
                "value": 0
            }
        }

    def characterCreation(self):

        statsTuple = ("str", "dex", "int", "con")
        pointsLeft = 10

        print("Welcome to character creation. Please enter a name:")
        self.name = input()
        print(f"Hello, {self.name}. You have a pool of ten points to spend to increase your stats.")

        for i in statsTuple:
            next = False
            if (pointsLeft > 0):
                while next == False:
                    if (pointsLeft > 0):
                        print(f"\nCurrent {i}: {self.stats[i]}. Add [0 - {pointsLeft}]: ")
                        readIn = int(input())
                        if (readIn <= pointsLeft and readIn >= 0):
                            self.stats[i] += readIn
                            pointsLeft -= readIn
                            print(f"new {i}: {self.stats[i]}")
                            next = True
                        else:
                            print(f"invalid input, please choose a number between [0 - {pointsLeft}]")
                    else:
                        next = True
            else:
                print(f"Current {i}: {self.stats[i]}. No more points to spend.")

        self.hp = self.stats["con"] + 2
        self.damage = math.ceil(self.stats["str"] / 5)
        self.globalStatus = {
            "Fancy Hat taken": False
        }

        self.isAlive = True

        print("\n # FINAL STATS #")

        for i in statsTuple:
            print(f"{i}: {self.stats[i]}")

        print(f"Base Damage: {self.damage}")
        print(f"HP: {self.hp}")



    pass
