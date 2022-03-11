# item.py

class Item:
    def __init__(self, itemID):
        self.itemID = itemID

        # define item information based on ID
        if(self.itemID == 1):
            self.name = "Fancy Hat"
            self.value = 5
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.description = "A small decorative hat, too small to wear. It is finely crafted of black silk with green embroidery."

        elif(self.itemID == 2):
            self.name = "Muddy Boots"
            self.value = 2
            self.equippable = True
            self.armor = True
            self.armorBonus = 1
            self.weapon = False
            self.magic = False
            self.description = "A pair of slightly muddy work boots."

        elif(self.itemID == 3):
            self.name = "Emerald Medallion"
            self.value = 7
            self.equippable = True
            self.armor = False
            self.weapon = False
            self.magic = True
            self.magicBonus = 2
            self.statRequired = {"int": 8}
            self.description = "A brilliantly faceted forest-green gem set in sterling silver and strung on a silver chain Meant to be warn around the neck."

        elif(self.itemID == 4):
            self.name = "Spellbook"
            self.value = 10
            self.equippable = True
            self.armor = False
            self.weapon = False
            self.magic = True
            self.magicBonus = 2
            self.statRequired = {"int": 12}
            self.description = "A brilliantly faceted forest-green gem set in sterling silver and strung on a silver chain Meant to be warn around the neck."
