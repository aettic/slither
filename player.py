import math
import random
from zones import Zone
import json

class Player:
    def __init__(self, playerDict):

        # initialize player values based on either newPlayer or loaded JSON data
        self.name = playerDict["name"]
        self.isAlive = playerDict["isAlive"]
        self.zoneID = playerDict["zoneID"]
        self.maxHP = playerDict["maxHP"]
        self.currentHP = playerDict["currentHP"]
        self.globalStatus = playerDict["globalStatus"]
        self.damage = playerDict["damage"]
        self.stats = playerDict["stats"]
        self.inventory = playerDict["inventory"]
        self.weapon = playerDict["weapon"]
        self.magic = playerDict["magic"]

        # Create Zone object using given zoneID
        self.zone = Zone(self.zoneID, self)



    def printStats(self):
        print("\n # FINAL STATS #")

        for i in statsTuple:
            print(f"{i}: {self.stats[i]}")

        print(f"Base Damage: {self.damage}")
        print(f"HP: {self.maxHP}")


    def attack(creature):
        print(f"You attack with your {self.weapon}")
        creature.takeDamage(random.randrange(self.damage))


    def takeDamage(damage):
        self.currentHP -= damage
        if(self.currentHP <= 0):
            self.isAlive = False


    def saveState(self):
        saveDict = {
            "name": self.name,
            "isAlive": self.isAlive,
            "zoneID": self.zone.zoneID,
            "maxHP": self.maxHP,
            "currentHP": self.currentHP,
            "globalStatus": self.globalStatus,
            "damage": self.damage,
            "stats": self.stats,
            "inventory": self.inventory,
            "weapon": self.weapon,
            "magic": self.magic
        }

        saveJson = json.dumps(saveDict, indent = 2)

        with open("saves/gameSave.json", 'w') as file:
            file.write(saveJson)
