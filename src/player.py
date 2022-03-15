import math
import random
from zones import Zone
import json
from item import Item
import os
import sys

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
        self.armor = playerDict["armor"]
        self.defense = playerDict["defense"]
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


    def useItem(self, itemID):

        item = Item(itemID)
        if(item.use != False):
            if(item.use == "equip" and item.equippable == True):
                self.equipItem(item)
            elif(item.use == "spell"):
                self.castSpell(item)
            elif(item.use == "toggle"):
                self.toggle(item)

    def equipItem(self, item):
        if(item.armor == True):
            self.armor.append(item.itemID)
            self.defense += item.armorBonus
        elif(item.weapon == True):
            self.weapon.append(item.itemID)
            self.damage += item.damageBonus
        else:
            print("Not yet made")
        self.inventory.pop(self.inventory.index(item.itemID))

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

        # Lantern
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
                    print("You extinguish the Lantern's flame.")
                    self.globalStatus["Lantern Lit"] = False
                    if(self.globalStatus["Dark"] == False and self.globalStatus["Dark Place"] == True):
                        self.globalStatus["Dark"] = True
                        print("The darkness returns, be careful...")

        # Matches
        elif(item.itemID == 15):
            if(self.globalStatus["Match Lit"] == False):
                print("You light a match.")
                self.globalStatus["Match Lit"] = True
                self.globalStatus["Dark"] = False
                self.globalStatus["Matches timer"] = 3
            else:
                print("You put out the match")
                if(self.globalStatus["Dark Place"] == True):
                    self.globalStatus["Dark"] = True
                self.globalStatus["Match Lit"] = False

        else:
            print("Not yet made")


    def accessInventory(self):
        print("\t# INVENTORY #")
        for itemID in self.inventory:
            print(f"\n{self.inventory.index(itemID) + 1}: {Item(itemID).name}")
            print(Item(itemID).description)

        print(f"\nSelect an item to use [1 - {len(self.inventory)}]")
        choice = input()
        if (choice == ""):
            print("")
        else:
            self.useItem(self.inventory[int(choice) - 1])

    def viewEquipment(self):
        if(len(self.weapon) < 1):
            print(f"Wielding: Bare Fists (damage: {self.damage})")
        else:
            print(f"Wielding: {Item(self.weapon[0]).name} (damage: {self.damage})")

        if(len(self.armor) < 1):
            print("Wearing: Clothes")
        else:
            print(f"Wearing: {Item(self.armor[0]).name}")


    def viewStats(self):
        print(f"HP: {self.currentHP} / {self.maxHP}")
        for stat in self.stats:
            print(f"{stat}: {self.stats[stat]}")
        print(f"Damage: {self.damage}")
        print(f"Magic: {self.magic}")


    # Open a menu to interact with player character
    def menu(self):
        print("\t# MENU #")
        print("1 - Inventory")
        print("2 - Stats")
        print("3 - Equipment")
        print("4 - Save Game")
        print("ENTER - Return to Game")
        choice = input()

        if (int(choice) == 1):
            self.accessInventory()
        elif (int(choice) == 2):
            self.viewStats()
        elif (int(choice) == 3):
            self.viewEquipment()
        elif (int(choice) == 4):
            self.saveState()
        else:
            print("")



    # Save the current game state as a JSON file. Unencrypted and editable.
    def saveState(self):
        saveDict = {
            "name": self.name,
            "isAlive": self.isAlive,
            "zoneID": self.zoneID,
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
