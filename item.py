# item.py

class Item:
    def __init__(self, itemID):
        self.itemID = itemID

        # define item information based on ID
        if(self.itemID == 0):
            self.name = "Note from Alys"
            self.value = 0
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A small note from your friend pleading for you to visit her at her farm. She seemed desparate, which is not like Alys. But she also seemed excited, as if she was on the verge of a great discovery."

        elif(self.itemID == 1):
            self.name = "Fancy Hat"
            self.value = 5
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A small decorative hat, too small to wear. It is finely crafted of black silk with green embroidery."

        elif(self.itemID == 2):
            self.name = "Muddy Boots"
            self.value = 2
            self.equippable = True
            self.armor = True
            self.armorBonus = 1
            self.weapon = False
            self.magic = False
            self.use = "equip"
            self.description = "A pair of slightly muddy work boots."

        elif(self.itemID == 3):
            self.name = "Emerald Medallion"
            self.value = 7
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = True
            self.magicBonus = 2
            self.statRequired = {"int": 8}
            self.use = "spell"
            self.spell = "Rubbing the emerald medallion causes green magical sparks, and has revealed something hidden. You also feel invigorated."
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
            self.use = "spell"
            self.description = "A handbound leather journal which shines with a magical spark. The cover is emblazoned with a drawing of an eye."

        elif(self.itemID == 5):
            self.name = "Gold Coin"
            self.value = 1
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A strange golden coin with a star on one side, and a tree on the other. Could be worth something."

        elif(self.itemID == 6):
            self.name = "Alcohol"
            self.value = 2
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A very high proof clear alcohol, its ornate crystal decanter belies the fact that it is too strong to drink."

        elif(self.itemID == 7):
            self.name = "Lantern"
            self.value = 3
            self.equippable = True
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = "toggle"
            self.description = "An oil lantern which can easily be lit, the flame is protected by glass windows."

        elif(self.itemID == 8):
            self.name = "Hidden Note 1"
            self.value = 0
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A torn page of a journal, hurriedly documenting magical features of some sort of stairway. It appears to indicate that this stairway exists and does not exist at the same time; or perhaps it exists in a parallel dimension."

        elif(self.itemID == 9):
            self.name = "Hidden Note 2"
            self.value = 0
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "A drawing of a spiral, with evenly spaced segments, terminating in a circle which takes up half the page. Around it are a sunburts of branching lines... They almost seem to be the stocks of plants, spread away from the circle and its captivating spiral. There is a single word written on this note: 'Amaze'."

        elif(self.itemID == 10):
            self.name = "Hidden Note 3"
            self.value = 0
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "This note is a hastily sketched drawing of a wall of corn."

        elif(self.itemID == 11):
            self.name = "Letter from Alys"
            self.value = 0
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = False
            self.use = False
            self.description = "'To whoever finds this, consider this my last will and testement. Things are different. It's hard to know anymore which side I'm on. I thought that I could control things when I first found it, but that quickly proved foolish.'"

        elif(self.itemID == 12):
            self.name = "Sword"
            self.value = 5
            self.equippable = True
            self.armor = False
            self.weapon = True
            self.damageBonus = 4
            self.magic = False
            self.use = "equip"
            self.description = "A simple shortsword, handmade, but not by any expert. The blade is sharp, but crudely assymetrical."

        elif(self.itemID == 13):
            self.name = "Pitchfork"
            self.value = 2
            self.equippable = True
            self.armor = False
            self.weapon = True
            self.damageBonus = 1
            self.magic = False
            self.use = "equip"
            self.description = "A well-used iron pitchfork on a long wooden handle. The wood is warn and grimy with age."

        elif(self.itemID == 14):
            self.name = "Liquid Darkness"
            self.value = 100
            self.equippable = False
            self.armor = False
            self.weapon = False
            self.magic = True
            self.magicBonus = 5
            self.use = "spell"
            self.spell = "You crush the shadow thing, and it surrounds you like the cold embrace of undersea tentacles. For a moment your vision goes dark, and then it begins to fade back in, brighter than before. You can now see in the dark."
            self.description = "A roiling and evanescent mass of pure shadow. It is weightless, and you can feel immense power eminating from its core."
