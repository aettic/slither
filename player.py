import math
import random
from zones import Zone
import json
from item import Item

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


    def attack(self, creature):
        damage = random.randrange(self.damage)
        creature.takeDamage(damage)
        print(f"You attack with your {self.weapon}.")
        if(damage > 0):
            print(f"You deal {damage} damage. YOU[{self.currentHP}], IT[{creature.currentHP}]")
        else:
            print(f"The {creature.type} evades your attack.")



    def takeDamage(self, damage):
        self.currentHP -= damage
        if(self.currentHP <= 0):
            self.isAlive = False
            print("You have perished.\n\n\t # GAME OVER #")


    def useItem(self, itemChoice):
        itemID = self.inventory[int(itemChoice) - 1]

        item = Item(itemID)
        if item.use != False:
            if(item.use == "equip" and item.equippable == True):
                self.equipItem(item)
            elif(item.use == "spell"):
                self.castSpell(item)
            elif(item.use == "toggle"):
                self.toggle(item)

    def equipItem(self, item):
        if(item.armor == True):
            self.armor.append(item.itemID)
        elif(item.weapon == True):
            self.weapon = item.name
            self.damage += item.damageBonus
        else:
            print("Not yet made")

    def castSpell(self, item):
        if(item.itemID == 3):
            self.magic += item.magicBonus
            print(item.spell)
            self.globalStatus["Staircase Visible"] = True
        elif(item.itemID == 4):
            self.magic += item.magicBonus
            self.damage += item.magicBonus
            print(item.spell)
            self.globalStatus["Damage Enchanted"] = True
        elif(item.itemID == 11):
            self.magic += item.magicBonus
            print(item.spell)
            self.globalStatus["Darkvision"] = True
        else:
            print("Not yet made")


    def toggle(self, item):
        if(item.itemID == 7):

            if (self.globalStatus["Darkvision"] == True):
                print("You can already see in the dark.")
            else:
                if(self.globalStatus["Lantern Lit"] == False):
                    print("You light the lantern.")
                    self.globalStatus["Lantern Lit"] = True
                    if(self.globalStatus["Dark"] == True and self.globalStatus["Dark Place"] == True):
                        self.globalStatus["Dark"] = False
                        print("The darkness shrinks away and your area is now well lit.")
                    elif(self.globalStatus["Dark"] == True and self.globalStatus["Dark Place"] == False and self.globalStatus["Darkvision"] == False):
                        print("Your immediate area is illuminated.")
                        self.globalStatus["Dark"] = False

                else:
                    print("You extinguish the flame.")
                    pc.globalStatus["Lantern Lit"] = False
                    if(pc.globalStatus["Dark"] == False and pc.globalStatus["Dark Place"] == True):
                        pc.globalStatus["Dark"] = True
                        print("The darkness returns, be careful...")

        else:
            print("Not yet made")


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
