# creature.py

import random
from item import Item


class Creature:

    def __init__(self, type):
        self.type = type
        self.isAlive = True

        if (self.type == "Goblin"):

            # Possible descriptions
            descriptions = ["A nasty green creature, half-feral, half-cunning, with a malicious and tricksome spark about its eye", "A tiny brownie, mangy and ferocious, with a wild smile wider than its own face", "A thin and nimble spirte, its warty skin matte as dry bark"]

            # Setting stats
            self.maxHP = 8
            self.currentHP = self.maxHP - 1
            self.damage = 3
            self.description = random.choice(descriptions)
            self.weapons = ["claw", "bite", "knife"]
            self.itemDrops = [5]  # gold coin
            self.xp = 2

        elif (self.type == "Beast"):

            # Possible descriptions
            descriptions = ["A sleek and slender fox, quiet on its feet", "A plodding beaver, angry and territorial", "A grey wolf, its coat thick and light"]

            # Setting stats
            self.maxHP = 4
            self.currentHP = self.maxHP - 1
            self.damage = 2
            self.description = random.choice(descriptions)
            self.weapons = ["claw", "bite", "tail whip"]
            self.itemDrops = [5]  # gold coin
            self.xp = 1

        elif (self.type == "Grue"):

            # Possible descriptions
            descriptions = ["It is dark, but you hear the sloshing of some slimy thing", "The glint of teeth shines against what little light surrounds you", "You smell a foul odor of decay, and hear soft laughter nearby"]

            # Setting stats
            self.maxHP = 10
            self.currentHP = self.maxHP - 0
            self.damage = 10
            self.description = random.choice(descriptions)
            self.weapons = ["bite", "chomp", "eaten"]
            self.itemDrops = [11]  # liquid darkness
            self.xp = 5

    def attack(self, pc):
        damage = random.randrange(self.damage) + 2
        hit = damage - pc.defense
        print(f"The {self.type} attacks with a {random.choice(self.weapons)}.")
        if (hit > 0):
            pc.takeDamage(hit)
            print(f"The {self.type} deals {hit} damage.")
        else:
            if (damage == 0):
                print("You evade the attack.")
            elif (damage > 0):
                print("Your armor protects you from the attack.")

    def takeDamage(self, damage, pc):
        self.currentHP -= damage
        if(self.currentHP <= 0):
            self.isAlive = False
            self.currentHP = 0
            drop = Item(random.choice(self.itemDrops))
            if (drop.itemID not in pc.inventory):
                print(f"The {self.type} falls, and drops a {drop.name}.")
                pc.inventory.append(drop.itemID)
            pc.experience += self.xp
