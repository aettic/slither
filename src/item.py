# item.py

class Item:
    def __init__(self, itemID):
        self.itemID = itemID

        # default values
        self.name = "Item"
        self.value = 0
        self.description = "Item description."
        self.equippable = False
        self.armor = False
        self.weapon = False
        self.magic = False
        self.use = False

        # define item information based on ID
        if(self.itemID == 0):
            self.name = "Note from Alys"
            self.value = 0
            self.use = "read"
            self.description = '''A small note from your friend pleading for you to visit her at
her farm. She seemed desparate, which is not like Alys. But she
also seemed excited, as if she was on the verge of a great discovery.'''
            self.read = '''\nMy Dearest friend,

Things have been rather strange as of late. Peculiar, but also
intriguing. My studies have kept me on my toes, especially with
the evolving circumstances and consequences. I have opened some-
thing... What it is, I'm not sure. But it is open, and I suspect
that I am unable to close it again...

It is so exciting! I know I must probe deeper, past the boundar-
ies, and into this mysterious world I have discovered. Come out
here to the farm, please, you must see this wild magic yourself!

May the stars shine down upon your nights, my friend.

                                            - Alys Astraniela'''
            # location: Given to player at the start of the game

        elif(self.itemID == 1):
            self.name = "Fancy Hat"
            self.value = 3
            self.description = '''A small decorative hat, too small to wear. It is finely crafted
of black silk with green embroidery.'''
            # location: On the dirt road, hidden in a ditch

        elif(self.itemID == 2):
            self.name = "Muddy Boots"
            self.value = 2
            self.armor = True
            self.armorBonus = 1
            self.use = "equip"
            self.description = "A pair of slightly muddy work boots."
            # location: Inside the kitchen closet in the farmhouse

        elif(self.itemID == 3):
            self.name = "Emerald Pyramid Medallion"
            self.value = 7
            self.magic = True
            self.magicBonus = 2
            self.use = "combine"
            self.combine = [20]
            self.description = '''A brilliantly faceted forest-green gem in the shape of a Pyramid
strung on a silver chain and meant to be worn around the neck. It
seems to have a subtle motion about it, as if vibrating, though
you're sure it's not moving. There are a variety of complex
looking slots around the edges, as if it is part of a larger
whole. When worn, the pyramid points down.'''
            # location: Inside the kitchen closet in the farmhouse, hidden in a box

        elif(self.itemID == 4):
            self.name = "Spellbook"
            self.value = 10
            self.magic = True
            self.magicBonus = 2
            self.skillRequired = {"INT": 13}
            self.use = "spell"
            self.spell = {
                "Astral Crown": {
                    "description": '''You evoke a thousand luminaries of the night sky, as green stars
descend all around you and form a crown around your head.
You feel empowered as the crown of stars fades around you.''',
                    "effect": 4,
                    "magic": 3
                },
                "Miraculous Recovery": {
                    "description": '''The page of the book begins to glow in golden light, and you feel
your will and vigor return to you.''',
                    "effect": 5,
                    "magic": 2
                },
                "Subtle Steps": {
                    "description": '''A shroud of darkness envelopes you as your shadow fades and blends
into the world around you. Suddenly, your footsteps are silent.''',
                    "effect": True,
                    "magic": 2
                }
            }
            self.description = '''A handbound leather journal which shines with a magical spark.
The cover is emblazoned with a drawing of an eye, set with a gem.'''
            # location: Inside the upstairs hallway, hidden in a chest

        elif(self.itemID == 5):
            self.name = "Gold Coin"
            self.value = 1
            self.description = '''A strange golden coin with a star on one side, and a tree on
the other. Could be worth something.'''
            # location: In the prairie, hidden on the ground, and dropped by Goblins

        elif(self.itemID == 6):
            self.name = "Bottle of Ink"
            self.value = 1
            self.use = "combine"
            self.combine = [23]
            self.description = '''A small, bulbous bottle of black ink, undoubtedly used for
writing with a quill pen.'''
            # location: The Study, upstairs, on the desk.

        elif(self.itemID == 7):
            self.name = "Lantern"
            self.value = 3
            self.use = "toggle"
            self.lightSource = True
            self.description = '''An oil lantern which can easily be lit, the flame is protected by
glass windows.'''
            # location: Found in the shed, on a hook

        elif(self.itemID == 8):
            self.name = "Hidden Note 1"
            self.value = 0
            self.use = "toggle"
            self.read = '''A torn page of a journal, hurriedly documenting magical features
of some sort of stairway. It appears to indicate that this
stairway exists and does not exist at the same time; or perhaps
it exists in a parallel dimension.'''
            self.description = "A strange note found by the cellar stairs."
            # location: Tucked into the stairs of the cellar

        elif(self.itemID == 9):
            self.name = "Hidden Note 2"
            self.value = 0
            self.use = "toggle"
            self.read = '''A drawing of a spiral, with evenly spaced segments, terminating
in a circle which takes up half the page. Around it are a
sunburts of branching lines... They almost seem to be plants,
spread away from the circle and its captivating spiral.
There is a single word written on this note: 'Amaze'.'''
            self.description = '''A strange drawing found in a storage closet.'''
            # location: Found in the storage closet in the upstairs hallway

        elif(self.itemID == 10):
            self.name = "Hidden Note 3"
            self.value = 0
            self.use = "toggle"
            self.read = "This note is a hastily sketched drawing of a wall of corn."
            self.description = "A strange drawing found in the Barn Loft."
            # location: Found in the barn loft, in a small desk

        elif(self.itemID == 11):
            self.name = "Letter from Alys"
            self.value = 0
            self.use = "read"
            self.read = """'To whoever finds this, consider this my last will and testement.
Things are different. It's hard to know which side I'm on anymore.
I thought that I could control things when I first found it, but
that quickly proved foolish. Whether by starlight or stubbornness,
the door has opened, and I am finding it quite hard to close.
Perhaps it is that I do not want to close it. I have become
enthralled by the mysterious forces that live down there, but
I'm also terrified for my life. Please do not look for me. Seal
the door if you can, and try to forget this place.'"""
            self.description = "A letter written by Alys, found in her Study."
            # location: Found in the study on the desk, must be bright enough to read (not takeable)

        elif(self.itemID == 12):
            self.name = "Sword"
            self.value = 5
            self.weapon = True
            self.damageBonus = 3
            self.use = "equip"
            self.description = '''A simple shortsword, handmade, but not by any expert. The blade
is sharp, but crudely assymetrical.'''
            # location: On a wall-mount in Dareth's room.

        elif(self.itemID == 13):
            self.name = "Pitchfork"
            self.value = 2
            self.weapon = True
            self.damageBonus = 2
            self.use = "equip"
            self.description = '''A well-used iron pitchfork on a long wooden handle. The wood is
warn and grimy with age.'''
            # location: On a hook in the barnInterior

        elif(self.itemID == 14):
            self.name = "Liquid Darkness"
            self.value = 100
            self.magic = True
            self.magicBonus = 5
            self.use = "spell"
            self.spell = '''You crush the shadow thing, and it surrounds you like the cold embrace
of undersea tentacles. For a moment your vision goes dark, and
then it begins to fade back in, brighter than before. You can
now see in the dark.'''
            self.description = '''A roiling and evanescent mass of pure shadow. It is weightless,
and you can feel immense power eminating from its core.'''
            # location: Only dropped by Grue when killed

        elif(self.itemID == 15):
            self.name = "Matches"
            self.value = 1
            self.use = "toggle"
            self.lightSource = True
            self.description = '''A wooden match with a tip dipped in a dark red flamable
concoction. Strike anywhere.'''
            # location: Found in the closet, hidden under some sheets

        elif(self.itemID == 16):
            self.name = "Alchemical Powder"
            self.value = 3
            self.use = "combine"
            self.combine = [17, 18]
            self.description = '''A paper packet filled with a mysterious black powder with a sheen
like onyx or moonstone.'''
            # location: Found in the cellar, in the corner with some other alchemical stuff

        elif(self.itemID == 17):
            self.name = "Glass Jar"
            self.value = 1
            self.use = "combine"
            self.combine = [16, 18]
            self.description = '''A simple glass jar with an airtight lid.'''
            # location: Found in the kitchen, on the table

        elif(self.itemID == 18):
            self.name = "Acrid Solution"
            self.value = 2
            self.use = "combine"
            self.combine = [16, 17]
            self.description = '''A pungent and caustic solution, it may react violently with other
chemicals.'''
            # location: Inside the Shed, in some boxes, in a small metal container

        elif(self.itemID == 19):
            self.name = "Jar Bomb"
            self.value = 2
            self.skillRequired = {"INT": 9}
            self.use = "spell"
            self.spell = "You shake the jar and throw it! After a few seconds, it explodes!"
            self.description = '''A very dangerous homemade bomb. It could be useful, but it is
also quite fragile. Will probably explode if dropped or thrown.'''
            # location: Created from 16, 17, 18.

        elif(self.itemID == 20):
            self.name = "Emerald Pyramid"
            self.value = 5
            self.use = "combine"
            self.combine = [3]
            self.description = '''A mysterious green pyramid shape, complete with intricate slots
around its edges, it has a peculiar symmertry.'''
            # location: Found in the water pale inside the well.

        elif(self.itemID == 21):
            self.name = "Brass Key"
            self.value = 1
            self.description = '''A simple brass key, with an engraving of a tree on the bow.'''
            # location: On the floor in the Barn Stable, having fallen out of Dareth's pocket.

        elif(self.itemID == 22):
            self.name = "Emerald Merkaba Pendant"
            self.magicBonus = 10
            self.value = 50
            self.skillRequired = {"INT": 11}
            self.use = "spell"
            self.spell = '''You twist the double pyramid structure, which seems to interlock
and shift around itself. The inside glows a bright green, and the
whole surface sparkles brilliantly. It becomes hot, and you feel
almost as if it is on fire, you can see sparks eminating from it
like starlight. You feel as though it has revealed something
hidden. You also feel invigorated.'''
            self.description = '''A green Merkaba shaped pendant, about an inch and a half wide.
The shape is a pair of pyramids, intersected, creating one three-
dimensional star shape, with peculiar symmetry.'''
            # location: created by combining 3 and 20. Requires 12 Int to combine, and use.

        elif(self.itemID == 23):
            self.name = "Journal Page"
            self.value = 1
            self.use = "combine"
            self.combine = [6]
            self.description = '''A narrow loose page of parchment from Dareth's journal. It is
covered with peculiar markings in a language you cannot read,
with some kind of unfinished symbols, but underneath is written
in plain words: "Only in darkness do the stars light the way."'''
            # location: The workbench in the barnLoftd

        elif(self.itemID == 24):
            self.name = "Stained Journal Page"
            self.value = 1
            self.use = "spell"
            self.skillRequired = {"INT": 9}
            self.spell = '''You hold the page up, and can feel it almost guiding you.'''
            self.description = '''The page of the journal is now stained with black ink, except for
a star in the center. The page almost seems to be affected by a
different direction of gravity: one that appears to almost pull
you.'''
            # location: combined from journal page and bottle of ink

        elif(self.itemID == 99):
            self.name = "Knife"
            self.damageBonus = 1
            self.description = '''Your grandfather's knife, useful for many things.'''
            self.use = "equip"
            self.value = 0
            self.weapon = True
            # location: starts with it equipped

        elif(self.itemID == 100):
            self.name = "Template"
            self.value = 0
            self.description = '''.'''
            # location:

        else:
            self.name = "Impossible Item"
            self.value = 0
            self.description = "Ceci n'est pas une item."
