# creature.py

import random


class Creature:

    def __init__(self, type):
        self.type = type
        self.isAlive = True

        if (self.type == "Goblin"):

            # Possible descriptions
            descriptions = ["A nasty green creature, half-feral, half-cunning, with a malicious and tricksome spark about its eye", "A tiny brownie, mangie and ferocious, with a wild smile wider than its own face", "A thin and nimble spirte, its warty skin matte as dry bark"]

            # Setting stats
            self.maxHP = 6
            self.currentHP = self.maxHP - 1
            self.damage = 3
            self.description = random.choice(descriptions)
            self.weapons = ["claws", "bite", "knife"]

        elif (self.type == "Beast"):

            # Possible descriptions
            descriptions = ["A sleek and slender fox, quiet on its feet", "A plodding beaver, angry and territorial", "A grey wolf, its coat thick and light"]

            # Setting stats
            self.maxHP = 4
            self.currentHP = self.maxHP - 1
            self.damage = 2
            self.description = random.choice(descriptions)
            self.weapons = ["claw", "bite", "tail whip"]
            self.itemDrops = [
                {
                    "itemName": "gold coin"
                }
            ]

    def attack(pc):
        print(f"The {self.type} attacks with a {random.choice(self.weapons)}")
        pc.takeDamage(random.randrange(self.damage))

    def takeDamage(damage):
        self.currentHP -= damage
        if(self.currentHP <= 0):
            self.isAlive = False
            print(f"The {self.type} falls, and drops a {random.choice(self.itemDrops)["itemName"]}.")
