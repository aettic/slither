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
        self.armor = playerDict["armor"]
        self.currentHP = playerDict["currentHP"]
        self.damage = playerDict["damage"]
        self.darknessTimer = playerDict["darknessTimer"]
        self.defense = playerDict["defense"]
        self.experience = playerDict["experience"]
        self.globalStatus = playerDict["globalStatus"]
        self.inventory = playerDict["inventory"]
        self.isAlive = playerDict["isAlive"]
        self.magic = playerDict["magic"]
        self.matchTimer = playerDict["matchTimer"]
        self.maxHP = playerDict["maxHP"]
        self.maze = playerDict["maze"]
        self.mazeKey = playerDict["mazeKey"]
        self.name = playerDict["name"]
        self.stats = playerDict["stats"]
        self.weapon = playerDict["weapon"]
        self.zoneID = playerDict["zoneID"]

        # Create Zone object using given zoneID
        self.zone = Zone(self.zoneID, self)




    ### |- ------ COMBAT ------------------------------------------------------------------------ -|

    def attack(self, creature):
        weaponName = Item(self.weapon[0]).name
        bonus = Item(self.weapon[0]).damageBonus
        damage = random.randrange(self.damage) + random.randrange(bonus)

        print(f"You attack with your {weaponName}.")
        if(damage > 0):
            print(f"You deal {damage} damage.")
            creature.takeDamage(damage, self)
        else:
            print(f"The {creature.type} evades your attack.")


    def takeDamage(self, damage):
        self.currentHP -= (damage - self.defense)
        if(self.currentHP <= 0):
            self.isAlive = False
            print("You have perished.\n\n\t # GAME OVER #")


    def intimidate(self, enemy):
        intimidation = (self.stats["STR"] + self.stats["CON"]) - 15 #min 1, max 11
        intimidateFactor = math.ceil(random.randrange(intimidation))
        if(intimidateFactor > (math.ceil(enemy.maxHP / 2))):
            print(f"The {enemy.type} is scared by your terrifying visage, and scurries away!")
            return False
        else:
            print(f"The {enemy.type} is not bothered by your attempts at being frightening...")
            enemy.attack(self)
            return True




    ### |- ------ ITEM INTERACTIONS ------------------------------------------------------------- -|

    def useItem(self, itemID):
        item = Item(itemID)
        if(item.use != False):
            if(item.use == "equip"):
                self.equipItem(item)
            elif(item.use == "spell"):
                if(self.stats["INT"] >= item.statRequired["INT"]):
                    self.castSpell(item)
                else:
                    print("You do not have a high enough Intelligence score.")
            elif(item.use == "toggle"):
                self.toggle(item)
            elif(item.use == "combine"):
                self.combine(item)
            elif(item.use == "read"):
                print(item.read)


    def equipItem(self, item):
        if(item.armor == True):
            self.armor.append(item.itemID)
            self.defense += item.armorBonus
            print(f"You don the {item.name}")
        elif(item.weapon == True):
            # unequip current weapon
            self.damage -= Item(self.weapon[0]).damageBonus
            self.inventory.append(self.weapon.pop(0))

            self.weapon = [item.itemID]
            self.damage += item.damageBonus
            print(f"You wield the {item.name}")
        else:
            print("Not yet made")
        self.inventory.pop(self.inventory.index(item.itemID))


    def castSpell(self, item):
        if(item.itemID == 4):  # Spellbook
            self.magic += item.magicBonus
            self.globalStatus["Damage Enchanted"] = True
            print("\n\t# CHOOSE A SPELL #")
            print("1: Astral Crown")
            print("2: Miraculous Recovery")
            print("3: Subtle Steps")
            choice = input("> ")
            if(choice == 1):
                if(self.magic >= item.spell["Astral Crown"]["magic"]):
                    print(item.spell["Astral Crown"]["description"])
                    self.damage += item.spell["Astral Crown"]["effect"]
                    self.defense += item.spell["Astral Crown"]["effect"]
                    self.magic -= 1
                else:
                    print("You attempt to cast the spell, but nothing happens.")
            elif(choice == 2):
                if(self.magic >= item.spell["Miraculous Recovery"]["magic"]):
                    print(item.spell["Miraculous Recovery"]["description"])
                    self.currentHP += item.spell["Miraculous Recovery"]["effect"]
                    self.magic -= 1
                else:
                    print("You attempt to cast the spell, but nothing happens.")
            elif(choice == 3):
                if(self.magic >= item.spell["Subtle Steps"]["magic"]):
                    print(item.spell["Subtle Steps"]["description"])
                    self.globalStatus["Stealthy"] = item.spell["Subtle Steps"]["effect"]
                    self.magic -= 1
                else:
                    print("You attempt to cast the spell, but nothing happens.")
        elif(item.itemID == 6):  # Ink?
            print(item.spell)
            self.inventory.pop(self.inventory.index(item.itemID))
        elif(item.itemID == 11):  # Liquid Darkness
            self.magic += item.magicBonus
            print(item.spell)
            self.globalStatus["Darkvision"] = True
        elif(item.itemID == 19):  # Jar Bomb
            if (self.zoneID == 15):
                print("How do you use the jar bomb?")
                print("1: Throw")
                print("2: Roll")
                print("3: Shake and Drop")
                choice = input("> ")
                if(int(choice) == 1):
                    print("you throw the bomb and it shatters, the ingredients burn up.")
                elif(int(choice) == 2):
                    print('''You gently roll the jar toward your target, which mixes it together,
    and it explodes!''')
                elif(int(choice) == 3):
                    print('''You gently shake up the mixture, and can feel the pressure as the
concoction expands. You quickly let it down, to drop down the well
shaft. It explodes! The smell of sulfur and stardust fills your
nostrils...''')
                    self.globalStatus["prairieWell obstruction destroyed"] = True
            else:
                print("How do you use the jar bomb?")
                print("1: Throw")
                print("2: Roll")
                print("3: Shake and Hold")
                choice = input("> ")
                if(int(choice) == 1):
                    print("you throw the bomb and it shatters, the ingredients burn up.")
                elif(int(choice) == 2):
                    print('''You gently roll the jar toward your target, which mixes it together,
    and it explodes!''')
                elif(int(choice) == 3):
                    print('''You shake the jar and hold onto it, it explodes in your hand,
    shattered splinters of glass and alchemical fire engulf you.\n\n\t# GAME OVER #\n''')
                    self.isAlive = False
            self.inventory.pop(self.inventory.index(item.itemID))
        elif(item.itemID == 22):  # Emerald Merkaba Pendant
            self.magic += item.magicBonus
            self.globalStatus["Staircase Visible"] = True
            print(item.spell)


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
                self.matchTimer = 0
            else:
                print("You put out the match")
                if(self.globalStatus["Dark Place"] == True):
                    self.globalStatus["Dark"] = True
                self.globalStatus["Match Lit"] = False
        else:
            print("Not yet made")


    def combine(self, item):
        combineCount = 0
        for i in item.combine:
            if i in self.inventory:
                combineCount += 1
        if(item.itemID == 16 or item.itemID == 17 or item.itemID == 18):
            if (combineCount == 2):
                print('''You add the powder to the glass jar, and then pour in the caustic
liquid solution, and shut the lid tight. If you shake this, it
will explode soon after.''')
                self.inventory.pop(self.inventory.index(16))
                self.inventory.pop(self.inventory.index(17))
                self.inventory.pop(self.inventory.index(18))
                self.inventory.append(19)
            elif (combineCount < 2):
                print("You do not have enough to make this item useful. Keep looking.")

        elif(item.itemID == 3 or item.itemID == 20):
            if (combineCount == 1):
                print('''You gently slide the emerald pyramids together, and they fit
perfectly. You twist them clockwise, and they click together, and
seem to become a single, solid crystal.''')
                self.inventory.pop(self.inventory.index(3))
                self.inventory.pop(self.inventory.index(20))
                self.inventory.append(22)
            else:
                print("You do not have enough to make this item useful. Keep looking.")
        else:
            print("WIP")




    ### |- ------ VIEW FUNCTIONS ---------------------------------------------------------------- -|

    def viewInventory(self):
        print("\n\t# INVENTORY #")
        for itemID in self.inventory:
            print(f"\n{self.inventory.index(itemID) + 1}: {Item(itemID).name}")
            print(Item(itemID).description)
        print(f"\n# SELECT AN ITEM TO USE [1 - {len(self.inventory)}] (ENTER to exit menu) #")
        choice = input("> ")
        if (choice == ""):
            print("")
        else:
            self.useItem(self.inventory[int(choice) - 1])


    def viewEquipment(self):
        print("\n\t# EQUIPMENT #")
        if(len(self.weapon) < 1):
            print(f"Wielding: Bare Fists (damage: {self.damage})")
        else:
            print(f"Wielding: {Item(self.weapon[0]).name} (damage: {self.damage})")
        if(len(self.armor) < 1):
            print("Wearing: Clothes")
        else:
            print(f"Wearing: {Item(self.armor[0]).name}")


    def viewStats(self):
        print(f"\n\t# STATS #\nHP: {self.currentHP} / {self.maxHP}")
        for stat in self.stats:
            print(f"{stat}: {self.stats[stat]}")
        print(f"Damage: {self.damage}")
        print(f"Defense: {self.defense}")
        print(f"Magic: {self.magic}")




    ### |- ------ PLAYER MENU ------------------------------------------------------------------- -|

    # Open a menu to interact with player character
    def menu(self):
        print("\n\t# MENU #")
        print("1: Inventory")
        print("2: Stats")
        print("3: Equipment")
        print("4: Save Game")
        print("5: Quit")
        print("ENTER - Return to Game")
        choice = input("> ")

        if (int(choice) == 1):
            self.viewInventory()
        elif (int(choice) == 2):
            self.viewStats()
        elif (int(choice) == 3):
            self.viewEquipment()
        elif (int(choice) == 4):
            print("\n\t# GAME SAVED #")
            self.saveState()
        elif (int(choice) == 5):
            print(f'\033[{random.choice([31, 32, 33, 34, 35, 36, 37, 38, 39])}m' + """\n\n
           ..|'''.|                      '|| '||
          .|'     '    ...     ...     .. ||  || ...  .... ...  ....
          ||    .... .|  '|. .|  '|. .'  '||  ||'  ||  '|.  | .|...||
          '|.    ||  ||   || ||   || |.   ||  ||    |   '|.|  ||
           ''|...'|   '|.|'   '|.|'  '|..'||. '|...'     '|    '|...'
                                                      .. |
                                                       ''""" + '\n \033[0m')
            quit()
        else:
            print("")


    # Save the current game state as a JSON file. Unencrypted and editable.
    def saveState(self):
        saveDict = {
            "armor": self.armor,
            "currentHP": self.currentHP,
            "damage": self.damage,
            "darknessTimer": self.darknessTimer,
            "defense": self.defense,
            "experience": self.experience,
            "globalStatus": self.globalStatus,
            "inventory": self.inventory,
            "isAlive": self.isAlive,
            "magic": self.magic,
            "matchTimer": self.matchTimer,
            "maxHP": self.maxHP,
            "maze": self.maze,
            "mazeKey": self.mazeKey,
            "name": self.name,
            "stats": self.stats,
            "weapon": self.weapon,
            "zoneID": self.zoneID
        }

        saveJson = json.dumps(saveDict, indent = 2)

        with open("src/saves/gameSave.json", 'w') as file:
            file.write(saveJson)
