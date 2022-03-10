import math
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

        # Create Zone object using given zoneID
        self.zone = Zone(self.zoneID, self)


    def printStats(self):
        print("\n # FINAL STATS #")

        for i in statsTuple:
            print(f"{i}: {self.stats[i]}")

        print(f"Base Damage: {self.damage}")
        print(f"HP: {self.maxHP}")


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
            "inventory": self.inventory
        }

        saveJson = json.dumps(saveDict, indent = 2)

        with open("saves/gameSave.json", 'w') as file:
            file.write(saveJson)
