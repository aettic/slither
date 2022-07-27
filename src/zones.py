# zones.py

from item import Item

class Zone:

    def __init__(self, zoneID, pc):
        # Zones are essentially rooms. All events in the game take place in a zone. Zomes feature a number of attributes, which define everything about them, from what the zone is called, to what it looks like, to what kind of options are available in that zone, to what items are available, and these attributes can change for the player based on the PC's global status dictionary. If, for instance, it's the first time walking into the dirt road zone, then there is a hat available to pick up, if the hat has been picked up, it will not show up anymore in the description, or the options.
        # Inside a zone, options are dictated by a select list of possible option types, and what they do specifically is defined in the zone, based on its current circumstance.
        self.zoneID = zoneID
        self.items = []




        ### DIRT ROAD ###------------------------------------------------------------------------ -|

        if (self.zoneID == 0):  # starting zone (dirtRoad)
            self.summary = '''You stand just off a dirt road. The road continues North and
South. There is a farm to the West. Past the farmhouse can be
seen a barn, and two small buildings.'''
            self.description = '''You are standing just off a dirt road which stretches onward
for what seems like miles to the North and South. The sun hangs
overhead, slowly dipping toward the horizon behind a steady farm.
Several structures dot the property, including a house, a barn,
and a couple ancilliary buildings. Behind you, across the road,
a wide field of beans stretches far into the distance, abutting
a misty thicket of wood. Tucked into the sparse grass, in the
ditch just off the road, you spot a tiny hat.'''
            self.items.clear()
            self.items = [1]

            if(pc.globalStatus["dirtRoad examined"] == False):
                self.options = [
                    "Walk West toward the house",
                    "Walk North along the road",
                    "Walk South along the road",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You walk toward the house.",
                        "moveTo": 1,
                    },
                    2: {
                        "do": "You walk up the road, but decide to head back.",
                    },
                    3: {
                        "do": "You walk down the road, but decide to head back.",
                    },
                    4: {
                        "do": self.description,
                        "examine": "dirtRoad"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Fancy Hat taken"] == False):
                    self.options = [
                        "Walk West toward the house",
                        "Walk North along the road",
                        "Walk South along the road",
                        "Pickup the hat",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You walk toward the house.",
                            "moveTo": 1,
                        },
                        2: {
                            "do": "You walk up the road, but decide to head back.",
                        },
                        3: {
                            "do": "You walk down the road, but decide to head back.",
                        },
                        4: {
                            "do": "You pick up the small hat.",
                            "takeItem": 1
                        },
                        5: {
                            "do": self.description,
                            "examine": "dirtRoad"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                elif(pc.globalStatus["Fancy Hat taken"] == True):
                    self.description = '''You are standing just off a dirt road which stretches onward
for what seems like miles to the North and South. The sun hangs
overhead, slowly dipping toward the horizon behind a steady farm.
Several structures dot the property, including a house, a barn,
and a couple ancilliary buildings. Behind you, across the road,
a wide field of beans stretches far into the distance, abutting
a misty thicket of wood.'''
                    self.options = [
                        "Walk West toward the house",
                        "Walk North along the road",
                        "Walk South along the road",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You walk toward the house.",
                            "moveTo": 1,
                        },
                        2: {
                            "do": "You walk up the road, but decide to head back.",
                        },
                        3: {
                            "do": "You walk down the road, but decide to head back.",
                        },
                        4: {
                            "do": self.description,
                            "examine": "dirtRoad"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }




        ### FARMHOUSE ###------------------------------------------------------------------------ -|

        elif (self.zoneID == 1):  # farmhouseFront entrance (HUB FRONT)
            self.summary = '''You stand in front of the farmstead home, darkened with abandon.
Behind the farm is a prairie with several structures including
a well, an outhouse, a shed, and a large barn. On the far North
of the property is a large cornfield.'''
            self.description = '''A looming log farmhouse, nearly a two-story cabin, complete
with thatched gable roofing, stands firm in front of you, here
in the center of this farm property. The sun threatens to set
behind it, inching closer every moment. Behind the house, a
smattering of structures dot the property: A stone well close by;
a farm tool shed, a cramped looking outhouse, and a large barn
which dwarfs the house itself, even from so far away. The gently
rolling landscape surrounding the house is comprised of wheats
and grasses, with a couple small plots of beans, cabbages, and
other low crops. In the distance a scarecrow watches plaintively
over the crops. The Northern edge of the property fades into a
dense and tall corn field. The whole property is surrounded on
the outskirts by darkened and misty woods.'''
            self.items.clear()
            self.options = [
                "Enter the house",
                "Walk into the backyard",
                "Check out the cellar doors",
                "Travel to the corn field",
                "Return to the road",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk inside the farmhouse through the porch door.",
                    "moveTo": 2
                },
                2: {
                    "do": "You skirt the side of the house and walk into the prairie behind the house.",
                    "moveTo": 14
                },
                3: {
                    "do": "You walk around the side of the house and to the cellar doors.",
                    "moveTo": 12
                },
                4: {
                    "do": "You depart the house and head North, toward the wall of green corn stalks.",
                    "moveTo": 24
                },
                5: {
                    "do": "You decide to head back toward the dirt road.",
                    "moveTo": 0
                },
                6: {
                    "do": self.description,
                    "examine": "farmhouseFront"
                },
                7: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 2):  # inside farmhouse - kitchen
            self.summary = '''The house is dark. You stand in the kitchen, which also serves as
a dining room. There is a closet to your right, a great room
behind a wall straight ahead, and a staircase at the far back
of this floor leading up.'''
            self.description = '''Only the dim evening light spills in from the windows on the
West side of the wall. It appears that this place was left in
a hurry. The tell-tale signs of a struggle can be seen about the
room. There are unlit candles on the table and around the room.
There is a glass jar with lid sitting upright on the table.'''
            self.items.clear()
            self.items = [17]

            if(pc.globalStatus["farmhouseKitchen examined"] == False):
                self.options = [
                    "Into the sitting room",
                    "Open the closet",
                    "Head back outside",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You traverse the creaking floor and head into the sitting room.",
                        "moveTo": 4
                    },
                    2: {
                        "do": "You walk over to the closet door and pull it open.",
                        "moveTo": 3
                    },
                    3: {
                        "do": "You step back outside the house.",
                        "moveTo": 1
                    },
                    4: {
                        "do": self.description,
                        "examine": "farmhouseKitchen"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Glass Jar taken"] == False):
                    self.description = '''Only the dim evening light spills in from the windows on the West
side of the wall. It appears that this place was left in
a hurry. The tell-tale signs of a struggle can be seen about the
room. There are unlit candles on the table and around the room.
There is a glass jar with lid sitting upright on the table.'''
                    self.options = [
                        "Into the sitting room",
                        "Open the closet",
                        "Head back outside",
                        "Examine the signs of struggle",
                        "Take the glass jar",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You traverse the creaking floor and head into the sitting room.",
                            "moveTo": 4
                        },
                        2: {
                            "do": "You walk over to the closet door and pull it open.",
                            "moveTo": 3
                        },
                        3: {
                            "do": "You step back outside the house.",
                            "moveTo": 1
                        },
                        4: {
                            "do": '''You look around the room, examining the chaos and bedlam. Silver-
ware and dishes lie scattered haphazardly. A tea kettle is over-
turned on the floor, a small puddle of brown tea gathered around
it. It is no longer warm. A fight happened here. Is Alys okay?
You can see the footprints came from the sitting room.'''
                        },
                        5: {
                            "do": '''You grab the glass jar, and slip it into your backpack.''',
                            "takeItem": 17
                        },
                        6: {
                            "do": self.description,
                            "examine": "farmhouseKitchen"
                        },
                        7: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''Only the dim evening light spills in from the windows on the
        West side of the wall. It appears that this place was left in
        a hurry. The tell-tale signs of a struggle can be seen about the
        room. There are unlit candles on the table and around the room.'''
                    self.options = [
                        "Into the sitting room",
                        "Open the closet",
                        "Head back outside",
                        "Examine the signs of struggle",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You traverse the creaking floor and head into the sitting room.",
                            "moveTo": 4
                        },
                        2: {
                            "do": "You walk over to the closet door and pull it open.",
                            "moveTo": 3
                        },
                        3: {
                            "do": "You step back outside the house.",
                            "moveTo": 1
                        },
                        4: {
                            "do": '''You look around the room, examining the chaos and bedlam. Silver-
ware and dishes lie scattered haphazardly. A tea kettle is over-
turned on the floor, a small puddle of brown tea gathered around
it. It is no longer warm. A fight happened here. Is Alys okay?
You can see the footprints came from the sitting room.'''
                        },
                        5: {
                            "do": self.description,
                            "examine": "farmhouseKitchen"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }


        elif (self.zoneID == 3):  # farmhouseCloset1
            self.summary = '''A dusty front closet, muddy boots on the ground, a couple thick
coats, and some overalls.'''
            self.description = '''A wooden dowel supports a handful of coats, a pair of hide
overalls, and a nice shawl tucked behind the rest of the clothes.
There is a shelf, upon which rests a small box. On the floor are
two pairs of muddy boots. One pair looks like it could fit you.'''
            self.items.clear()
            self.items = [2, 3]

            if(pc.globalStatus["farmhouseCloset1 examined"] == False):
                if(pc.globalStatus["Muddy Boots taken"] == False):
                    self.options = [
                        "Head back to the kitchen",
                        "Go to the sitting room",
                        "Take the boots",
                        "Look around the area",
                        "Player Menu"
                    ]
                    self.selection = {
                        1: {
                            "do": "You close the closet door, and walk back to the kitchen.",
                            "moveTo": 2
                        },
                        2: {
                            "do": "You close the closet door and head into the sitting room.",
                            "moveTo": 4
                        },
                        3: {
                            "do": '''You grab the boots, dried mud is crusted on the
sides, but they look comfortable.''',
                            "takeItem": 2
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseCloset1"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''A wooden dowel supports a handful of coats, a pair of hide
overalls, and a nice shawl tucked behind the rest of the clothes.
There is a shelf, upon which rests a small box. On the floor is a
pair of boots, which probably won't fit you.'''
                    self.options = [
                        "Head back to the kitchen",
                        "Go to the sitting room",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the closet door, and walk back to the kitchen",
                            "moveTo": 2
                        },
                        2: {
                            "do": "You close the closet door and head into the sitting room",
                            "moveTo": 4
                        },
                        3: {
                            "do": self.description,
                            "examine": "farmhouseCloset1"
                        },
                        4: {
                            "menu": "menu"
                        }
                    }

            else:

                if(pc.globalStatus["Muddy Boots taken"] == False):
                    if(pc.globalStatus["farmhouseCloset1 Box examined"] == False):
                        self.options = [
                            "Head back to the kitchen",
                            "Go to the sitting room",
                            "Take the boots",
                            "Look in the box",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You close the closet door, and walk back to the kitchen.",
                                "moveTo": 2
                            },
                            2: {
                                "do": "You close the closet door and head into the sitting room.",
                                "moveTo": 4
                            },
                            3: {
                                "do": '''You grab the boots, dried mud is crusted on the
sides, but they look comfortable.''',
                                "takeItem": 2
                            },
                            4: {
                                "do": '''You pull the box down and open it up, inside is a small emerald
trinket in the shape of a pyramid.''',
                                "examine": "farmhouseCloset1 Box"
                            },
                            5: {
                                "do": self.description,
                                "examine": "farmhouseCloset1"
                            },
                            6: {
                                "menu": "menu"
                            }
                        }
                    elif(pc.globalStatus["farmhouseCloset1 Box examined"] == True):
                        if(pc.globalStatus["Emerald Pyramid Medallion taken"] == False):
                            self.options = [
                                "Head back to the kitchen",
                                "Go to the sitting room",
                                "Take the boots",
                                "Take the Medallion",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the closet door, and walk back to the kitchen.",
                                    "moveTo": 2
                                },
                                2: {
                                    "do": "You close the closet door and head into the sitting room.",
                                    "moveTo": 4
                                },
                                3: {
                                    "do": '''You grab the boots, dried mud is crusted on the
sides, but they look comfortable.''',
                                    "takeItem": 2
                                },
                                4: {
                                    "do": '''You gently lift the delicate charm out of the box, it is on a
silver chain. You put it in your pack.''',
                                    "takeItem": 3
                                },
                                5: {
                                    "do": self.description,
                                    "examine": "farmhouseCloset1"
                                },
                                6: {
                                    "menu": "menu"
                                }
                            }

                        elif(pc.globalStatus["Emerald Pyramid Medallion taken"] == True):
                            self.options = [
                                "Head back to the kitchen",
                                "Go to the sitting room",
                                "Take the boots",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the closet door, and walk back to the kitchen.",
                                    "moveTo": 2
                                },
                                2: {
                                    "do": "You close the closet door and head into the sitting room.",
                                    "moveTo": 4
                                },
                                3: {
                                    "do": '''You grab the boots, dried mud is crusted on the
sides, but they look comfortable.''',
                                    "takeItem": 2
                                },
                                4: {
                                    "do": self.description,
                                    "examine": "farmhouseCloset1"
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }


                elif(pc.globalStatus["Muddy Boots taken"] == True):
                    self.description = '''A wooden dowel supports a handful of coats, a pair of hide
overalls, and a nice shawl tucked behind the rest of the clothes.
There is a shelf, upon which rests a small box. On the floor is a
pair of boots, which probably won't fit you.'''
                    if(pc.globalStatus["farmhouseCloset1 Box examined"] == False):
                        self.options = [
                            "Head back to the kitchen",
                            "Go to the sitting room",
                            "Look in the box",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You close the closet door, and walk back to the kitchen",
                                "moveTo": 2
                            },
                            2: {
                                "do": "You close the closet door and head into the sitting room",
                                "moveTo": 4
                            },
                            3: {
                                "do": '''You pull the box down and open it up, inside is a small emerald
trinket in the shape of a pyramid.''',
                                "examine": "farmhouseCloset1 Box"
                            },
                            4: {
                                "do": self.description,
                                "examine": "farmhouseCloset1"
                            },
                            5: {
                                "menu": "menu"
                            }
                        }
                    elif(pc.globalStatus["farmhouseCloset1 Box examined"] == True):
                        if(pc.globalStatus["Emerald Pyramid Medallion taken"] == False):
                            self.options = [
                                "Head back to the kitchen",
                                "Go to the sitting room",
                                "Take the Medallion",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the closet door, and walk back to the kitchen",
                                    "moveTo": 2
                                },
                                2: {
                                    "do": "You close the closet door and head into the sitting room",
                                    "moveTo": 4
                                },
                                3: {
                                    "do": '''You gently lift the delicate charm out of the box, it is on a
silver chain. You put it in your pack.''',
                                    "takeItem": 3
                                },
                                4: {
                                    "do": self.description,
                                    "examine": "farmhouseCloset1"
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }
                        elif(pc.globalStatus["Emerald Pyramid Medallion taken"] == True):
                            self.options = [
                                "Head back to the kitchen",
                                "Go to the sitting room",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the closet door, and walk back to the kitchen.",
                                    "moveTo": 2
                                },
                                2: {
                                    "do": "You close the closet door and head into the sitting room.",
                                    "moveTo": 4
                                },
                                3: {
                                    "do": self.description,
                                    "examine": "farmhouseCloset1"
                                },
                                4: {
                                    "menu": "menu"
                                }
                            }


        elif (self.zoneID == 4):  # farmhouseSittingRoom
            self.summary = '''This sitting room features two chairs positioned before a stout
fireplace, blackened with use. Behind the chairs, a staircase
climbs to the second floor. The kitchen and closet aren't far away.'''
            self.description = '''A pair of comfortable looking chairs face a fireplace, taking up
the body of the room. On one side is a basket filled with some
books. The fireplace seems to have exploded outward, as ash is
scattered in a burst toward the chairs. Upon closer inspection,
in the ash are tiny footprints...'''
            self.items.clear()

            if(pc.globalStatus["farmhouseSittingRoom examined"] == False):
                self.options = [
                    "Climb the stairs",
                    "Head back to the kitchen",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head toward the spiral staircase, taking its steps up.",
                        "moveTo": 5
                    },
                    2: {
                        "do": "You venture back to the kitchen",
                        "moveTo": 2
                    },
                    3: {
                        "do": self.description,
                        "examine": "farmhouseSittingRoom"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                self.options = [
                    "Climb the stairs",
                    "Head back to the kitchen",
                    "Examine the fireplace",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head toward the spiral staircase, taking its steps up.",
                        "moveTo": 5
                    },
                    2: {
                        "do": "You venture back to the kitchen.",
                        "moveTo": 2
                    },
                    3: {
                        "do": '''Ash seems to have spewn from the fireplace outward, and has coated
the floor and even the bottoms of the chairs. Little clawed
footprints can be made out in the ash, coming from the fireplace,
and leading out of the sitting room. Following the tracks, you
can make out multiple sets, heading toward the kitchen at the
front of the house.''',
                        "examine": "farmhouseSittingRoom Fireplace"
                    },
                    4: {
                        "do": self.description,
                        "examine": "farmhouseSittingRoom"
                    },
                    5: {
                        "menu": "menu"
                    }
                }

        elif (self.zoneID == 5):  # farmhouseStairsInside
            self.summary = '''These simple stairs spiral up counter-clockwise, leading between the
ground floor and upper floor.'''
            self.description = '''Solid wooden boards fan out from a sturdy central support pillar
which runs the height of the house, from ground to roof. The
stairs creak gently. The back wall is decorated with a handful
of portraits: A beautiful woman you know to be Alys, a young
man who must be her son, and another man who you remember as
her husband. A crest of the Astraniela family featuring thirteen
stars around a circular labyrinth design with a heart at the
center.'''
            self.items.clear()
            self.options = [
                "Down to the ground floor sitting room",
                "Up the stairs into the hallway",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You climb down the stairs and end up back in the sitting room.",
                    "moveTo": 4
                },
                2: {
                    "do": "You ascend, spilling out into an upstairs hallway.",
                    "moveTo": 6
                },
                3: {
                    "do": self.description
                },
                4: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 6):  # farmhouseHallway
            self.summary = "A hallway with two doors on either side."
            self.description = '''This hallway is quite plain, with two doors on either side and a
large chest at the far end, resting beneath a stained glass window
depicting a scene of meteors gliding downward at an angle, fiery
tails trailing behind.'''
            self.items.clear()
            self.items = [4]

            if(pc.globalStatus["farmhouseHallway examined"] == False):
                self.options = [
                    "Back to the stairs",
                    "First door on the left",
                    "Second door on the left",
                    "First door on the right",
                    "Second door on the right",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You climb down the stairs and end up back in the sitting room.",
                        "moveTo": 5
                    },
                    2: {
                        "do": "You enter the first door on the left, a Master Bedroom.",
                        "moveTo": 8
                    },
                    3: {
                        "do": "You enter the second door on the left, a Study.",
                        "moveTo": 10
                    },
                    4: {
                        "do": "You enter the first door on the right, a Storage room.",
                        "moveTo": 11
                    },
                    5: {
                        "do": "You enter the second door on the right, a Bedroom.",
                        "moveTo": 9
                    },
                    6: {
                        "do": self.description,
                        "examine": "farmhouseHallway"
                    },
                    7: {
                        "menu": "menu"
                    }
                }
            elif(pc.globalStatus["farmhouseHallway examined"] == True):
                if(pc.globalStatus["farmhouseHallway Chest examined"] == False):
                    self.options = [
                        "Back to the stairs",
                        "First door on the left",
                        "Second door on the left",
                        "First door on the right",
                        "Second door on the right",
                        "Open the chest and look inside",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You climb down the stairs and end up back in the sitting room.",
                            "moveTo": 5
                        },
                        2: {
                            "do": "You enter the first door on the left, a Master Bedroom.",
                            "moveTo": 8
                        },
                        3: {
                            "do": "You enter the second door on the left, a Study.",
                            "moveTo": 10
                        },
                        4: {
                            "do": "You enter the first door on the right, a Storage room.",
                            "moveTo": 11
                        },
                        5: {
                            "do": "You enter the second door on the right, a Bedroom.",
                            "moveTo": 9
                        },
                        6: {
                            "do": '''You open up the large chest and peek inside. There is an ornate
looking book with a gem set in the cover.''',
                            "examine": "farmhouseHallway Chest"
                        },
                        7: {
                            "do": self.description,
                            "examine": "farmhouseHallway"
                        },
                        8: {
                            "menu": "menu"
                        }
                    }
                elif(pc.globalStatus["farmhouseHallway Chest examined"] == True):
                    self.description = '''This hallway is quite plain, with two doors on either side and a
large open chest at the far end, resting beneath a stained glass
window depicting a scene of meteors gliding downward at an angle,
fiery tails trailing behind.'''
                    if(pc.globalStatus["Spellbook taken"] == False):
                        self.options = [
                            "Back to the stairs",
                            "First door on the left",
                            "Second door on the left",
                            "First door on the right",
                            "Second door on the right",
                            "Take the book",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You climb down the stairs and end up back in the sitting room.",
                                "moveTo": 5
                            },
                            2: {
                                "do": "You enter the first door on the left, a Master Bedroom.",
                                "moveTo": 8
                            },
                            3: {
                                "do": "You enter the second door on the left, a Study.",
                                "moveTo": 10
                            },
                            4: {
                                "do": "You enter the first door on the right, a Storage room.",
                                "moveTo": 11
                            },
                            5: {
                                "do": "You enter the second door on the right, a Bedroom.",
                                "moveTo": 9
                            },
                            6: {
                                "do": '''You take the arcane looking tome, and place it gently with your
things.''',
                                "takeItem": 4
                            },
                            7: {
                                "do": self.description,
                                "examine": "farmhouseHallway"
                            },
                            8: {
                                "menu": "menu"
                            }
                        }
                    elif(pc.globalStatus["Spellbook taken"] == True):
                        self.description = '''This hallway is quite plain, with two doors on either side and a
large empty chest at the far end, resting beneath a stained glass
window depicting a scene of meteors gliding downward at an angle,
fiery tails trailing behind.'''
                        self.options = [
                            "Back to the stairs",
                            "First door on the left",
                            "Second door on the left",
                            "First door on the right",
                            "Second door on the right",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You climb down the stairs and end up back in the sitting room.",
                                "moveTo": 5
                            },
                            2: {
                                "do": "You enter the first door on the left, a Master Bedroom.",
                                "moveTo": 8
                            },
                            3: {
                                "do": "You enter the second door on the left, a Study.",
                                "moveTo": 10
                            },
                            4: {
                                "do": "You enter the first door on the right, a Storage room.",
                                "moveTo": 11
                            },
                            5: {
                                "do": "You enter the second door on the right, a Bedroom.",
                                "moveTo": 9
                            },
                            6: {
                                "do": self.description,
                                "examine": "farmhouseHallway"
                            },
                            7: {
                                "menu": "menu"
                            }
                        }

        elif (self.zoneID == 7):  # farmhouseCloset2
            self.summary = "A simple closet full of clothes, sheets, and other odds and ends."
            self.description = '''This closet is full of linens, shirts and trousers, and some
extra blankets Nothing terrible interesting. On a small shelf
near the top, is a box of matches.'''
            self.items.clear()
            self.items = [15]

            if(pc.globalStatus["farmhouseCloset2 examined"] == False):
                self.options = [
                    "Close the closet door",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You close the closet door.",
                        "moveTo": 9
                    },
                    2: {
                        "do": self.description,
                        "examine": "farmhouseCloset2"
                    },
                    3: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Matches taken"] == False):
                    self.options = [
                        "Close the closet door",
                        "Take the matches",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the closet door.",
                            "moveTo": 9
                        },
                        2: {
                            "do": "You take the box of matches.",
                            "takeItem": 15,
                        },
                        3: {
                            "do": self.description,
                            "examine": "farmhouseCloset2"
                        },
                        4: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''This closet is full of linens, shirts and trousers, and some
extra blankets Nothing terrible interesting.'''
                    self.options = [
                        "Close the closet door",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the closet door.",
                            "moveTo": 9
                        },
                        2: {
                            "do": self.description,
                            "examine": "farmhouseCloset2"
                        },
                        3: {
                            "menu": "menu"
                        }
                    }

        elif (self.zoneID == 8):  # farmhouseMasterBedroom
            self.summary = "A large bedroom, with a wide bed on an ornately carved frame."
            self.description = '''The room is cozy and modest, but not small. The bed is clearly
well taken care of, and of fine craftsmanship. About the room are
a handful of odds and ends, including some books upon a shelf,
and a brass telescope pointed out the window, toward the sky.'''
            self.items.clear()

            if(pc.globalStatus["farmhouseMasterBedroom examined"] == False):
                self.options = [
                    "Exit the room",
                    "Go to the study",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You leave the room and return to the hall.",
                        "moveTo": 6
                    },
                    2: {
                        "do": "You open the door on the far end, and enter the study.",
                        "moveTo": 10
                    },
                    3: {
                        "do": self.description,
                        "examine": "farmhouseMasterBedroom"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Telescope examined"] == False):
                    self.options = [
                        "Exit the room",
                        "Go to the study",
                        "Peer through the telescope",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You leave the room and return to the hall.",
                            "moveTo": 6
                        },
                        2: {
                            "do": "You open the door on the far end, and enter the study.",
                            "moveTo": 10
                        },
                        3: {
                            "do": '''You scoot over to the telescope and look through it. It is
pointed at the blue sky. Gentle clouds roll by. As you gaze
through the glass, you see what appears to be a ball of green
fire cruise smoothly across the scene, piercing a cloud and
leaving a hole in the shape of a perfect circle!''',
                            "examine": "Telescope"
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseMasterBedroom"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.options = [
                        "Exit the room",
                        "Go to the study",
                        "Peer through the telescope",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You leave the room and return to the hall.",
                            "moveTo": 6
                        },
                        2: {
                            "do": "You open the door on the far end, and enter the study.",
                            "moveTo": 10
                        },
                        3: {
                            "do": '''You look through the brass tube again, hoping to see something
amazing, but all you see are the clouds in the sky, drifting
out of view.'''
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseMasterBedroom"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }

        elif (self.zoneID == 9):  # farmhouseGuestBedroom
            self.summary = "A small bedroom, decorated with a variety of hand drawn sketches."
            self.description = '''This bedroom is smaller than the one across the hall, and seems
like it might belong to Alys' son, Dareth. The walls are covered
in pages of parchment, each with different unique drawings made
in what appear to be charcoal in some cases, and ink in others.
The back wall is one large mural, drawn across a grid of pages
that covers the entire wall, including behind the bed. Above the
bed is a sword, mounted to a plaque on the wall. It looks like
it could be removed.'''
            self.items.clear()
            self.items = [12]

            if(pc.globalStatus["farmhouseGuestBedroom examined"] == False):
                self.options = [
                    "Exit the room",
                    "Open the closet door",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You leave the bedroom and return to the hallway.",
                        "moveTo": 6
                    },
                    2: {
                        "do": "You open the closet door.",
                        "moveTo": 7
                    },
                    3: {
                        "do": self.description,
                        "examine": "farmhouseGuestBedroom"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Sword taken"] == False):
                    self.options = [
                        "Exit the bedroom",
                        "Open the closet door",
                        "Take the sword",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You leave the bedroom and return to the hallway.",
                            "moveTo": 6
                        },
                        2: {
                            "do": "You open the closet door.",
                            "moveTo": 7
                        },
                        3: {
                            "do": "You take down the sword from its mount.",
                            "takeItem": 12
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseGuestBedroom"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''This bedroom is smaller than the one across the hall, and seems
like it might belong to Alys' son, Dareth. The walls are covered
in pages of parchment, each with different unique drawings made
in what appear to be charcoal in some cases, and ink in others.
The back wall is one large mural, drawn across a grid of pages
that covers the entire wall, including behind the bed. Above the
bed is a plaque mounted to the wall, which once held a sword.'''
                    self.options = [
                        "Exit the bedroom",
                        "Open the closet door",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You leave the bedroom and return to the hallway.",
                            "moveTo": 6
                        },
                        2: {
                            "do": "You open the closet door.",
                            "moveTo": 7
                        },
                        3: {
                            "do": self.description,
                            "examine": "farmhouseGuestBedroom"
                        },
                        4: {
                            "menu": "menu"
                        }
                    }

        elif (self.zoneID == 10):  # farmhouseStudy
            self.summary = '''The centerpiece of this study is its wide desk. The area is poorly
lit by a thin window above the desk. Papers are littered all over
the desk, and some on the floor.'''
            self.description = '''This cramped space seems well-used. A wide, but shallow desk
abuts the wooden wall, and the room is dimly lit by the evening
sky through a thin window above the desk. Two unlit candles in
sconces flank the door on either side. A small bottle of black
ink sits on the desk, next to a quill. You can also see that
notes are scattered about. Each contains formulae, sketches, and
hastily written theories and worries.'''
            self.items.clear()
            self.items = [6]
            if(pc.globalStatus["Match Lit"] == False and pc.globalStatus["Lantern Lit"] == False):
                pc.globalStatus["Dark"] = True

            if(pc.globalStatus["farmhouseStudy examined"] == False):
                self.options = [
                    "Return to the Bedroom",
                    "Exit to the hallway",
                    "Read the letter",
                    "Look around the area",
                    "Player Menu"
                ]

                if(pc.globalStatus["Dark"] == True):
                    self.selection = {
                        1: {
                            "do": "You leave the study, closing the door behind you.",
                            "moveTo": 8
                        },
                        2: {
                            "do": "You leave the study, closing the door behind you.",
                            "moveTo": 6
                        },
                        3: {
                            "do": "It is too dark to make out what the letter says clearly."
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseStudy"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.selection = {
                        1: {
                            "do": "You leave the study, closing the door behind you.",
                            "moveTo": 8
                        },
                        2: {
                            "do": "You leave the study, closing the door behind you.",
                            "moveTo": 6
                        },
                        3: {
                            "do": "You read the letter.",
                            "read": Item(11).read
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseStudy"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
            elif(pc.globalStatus["farmhouseStudy examined"] == True):
                if(pc.globalStatus["Dark"] == True):
                    if(pc.globalStatus["Bottle of Ink taken"] == False):
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Pick up the Bottle of Ink",
                            "Read the letter",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 8
                            },
                            2: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 6
                            },
                            3: {
                                "do": '''You pick up the ink bottle, and carefully place it in your pack,
making sure it's closed..''',
                                "takeItem": 6
                            },
                            4: {
                                "do": "It is too dark to make out what the letter says clearly."
                            },
                            5: {
                                "do": self.description,
                                "examine": "farmhouseStudy"
                            },
                            6: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.description = '''This cramped space seems well-used. A wide, but shallow desk
abuts the wooden wall, and the room is dimly lit by the evening
sky through a thin window above the desk. Two unlit candles in
sconces flank the door on either side. Writing materials sit on
the desk. You can also see that notes are scattered about. Each
contains formulae, sketches, and hastily written theories and
worries.'''
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Read the letter",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 8
                            },
                            2: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 6
                            },
                            3: {
                                "do": "It is too dark to make out what the letter says clearly."
                            },
                            4: {
                                "do": self.description,
                                "examine": "farmhouseStudy"
                            },
                            5: {
                                "menu": "menu"
                            }
                        }
                else:
                    if(pc.globalStatus["Bottle of Ink taken"] == False):
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Pick up the Bottle of Ink",
                            "Read the letter",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 8
                            },
                            2: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 6
                            },
                            3: {
                                "do": '''You pick up the ink bottle, and carefully place it in your pack,
making sure it's closed..''',
                                "takeItem": 6
                            },
                            4: {
                                "do": "You read the letter.",
                                "read": Item(11).read
                            },
                            5: {
                                "do": self.description,
                                "examine": "farmhouseStudy"
                            },
                            6: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Read the letter",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 8
                            },
                            2: {
                                "do": "You leave the study, closing the door behind you.",
                                "moveTo": 6
                            },
                            3: {
                                "do": "You read the letter.",
                                "read": Item(11).read
                            },
                            4: {
                                "do": self.description,
                                "examine": "farmhouseStudy"
                            },
                            5: {
                                "menu": "menu"
                            }
                        }


        elif (self.zoneID == 11):  # farmhouseStorage
            self.summary = '''This small storage room seems to contain a variety of items useful
around the house.'''
            self.description = '''Inside this storage room are bags of hay and feathers, likely
used for stuffing; extra pillows; sheets; a small wooden box
containing some personal belongings. There is a folded note in
the box, amidst other odds and ends.'''
            self.items.clear()
            self.items = [9]

            if(pc.globalStatus["farmhouseStorage examined"] == False):
                self.options = [
                    "Close the door",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You close the door and return to the hallway.",
                        "moveTo": 6
                    },
                    2: {
                        "do": self.description,
                        "examine": "farmhouseStorage"
                    },
                    3: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Hidden Note 2 taken"] == False):
                    self.options = [
                        "Close the door",
                        "Take the Note",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the door and return to the hallway.",
                            "moveTo": 6
                        },
                        2: {
                            "do": "You take the note.",
                            "takeItem": 9
                        },
                        3: {
                            "do": self.description,
                            "examine": "farmhouseStorage"
                        },
                        4: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''Inside this storage room are bags of hay and feathers, likely
used for stuffing; extra pillows; sheets; a small wooden box
containing some personal belongings. The box contains old pic-
tures, trinkets, and other odds and ends.'''
                    self.options = [
                        "Close the door",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the door and return to the hallway.",
                            "moveTo": 6
                        },
                        2: {
                            "do": self.description,
                            "examine": "farmhouseStorage"
                        },
                        3: {
                            "menu": "menu"
                        }
                    }

        elif (self.zoneID == 12):  # farmhouseStairsCellar
            self.summary = "Double doors lay closed over the entrance to the cellar."
            self.description = '''Heavy looking wooden doors stand resolute, shut tight
over the entrance to the cellar. The wooden doors are carved with
a large symbol, circular, with interconnected knots, and thirteen
stars sround the edge. In the center is an ornate labyrinth. You
spot a small folded piece of paper tucked between some of the
stones.'''
            self.items.clear()
            self.items = [8]

            if(pc.globalStatus["farmhouseStairsCellar examined"] == False):
                self.options = [
                    "Open the doors and descend",
                    "Head back to the prairie",
                    "Walk toward the front of the house",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": '''You pull open the heavy wooden doors, and climb down the stairs
into the darkened cellar.''',
                        "moveTo": 13
                    },
                    2: {
                        "do": '''You leave the cellar doors and head toward the backyard.''',
                        "moveTo": 14
                    },
                    3: {
                        "do": '''You leave the cellar doors and return to the front of the house.''',
                        "moveTo": 1
                    },
                    4: {
                        "do": self.description,
                        "examine": "farmhouseStairsCellar"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Hidden Note 1 taken"] == False):
                    self.options = [
                        "Open the doors and descend",
                        "Head back to the prairie",
                        "Walk toward the front of the house",
                        "Pick up the note",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": '''You pull open the heavy wooden doors, and climb down the stairs
    into the darkened cellar.''',
                            "moveTo": 13
                        },
                        2: {
                            "do": '''You leave the cellar doors and head toward the backyard.''',
                            "moveTo": 14
                        },
                        3: {
                            "do": '''You leave the cellar doors and return to the front of the house.''',
                            "moveTo": 1
                        },
                        4: {
                            "do": '''You reach down and pick up the folded note.''',
                            "takeItem": 8
                        },
                        5: {
                            "do": self.description,
                            "examine": "farmhouseStairsCellar"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''Heavy looking wooden doors stand resolute, shut tight
over the entrance to the cellar. The wooden doors are carved with
a large symbol, circular, with interconnected knots, and thirteen
stars sround the edge. In the center is an ornate labyrinth.'''
                    self.options = [
                        "Open the doors and descend",
                        "Head back to the prairie",
                        "Walk toward the front of the house",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": '''You pull open the heavy wooden doors, and climb down the stairs
    into the darkened cellar.''',
                            "moveTo": 13
                        },
                        2: {
                            "do": '''You leave the cellar doors and head toward the backyard.''',
                            "moveTo": 14
                        },
                        3: {
                            "do": '''You leave the cellar doors and return to the front of the house.''',
                            "moveTo": 1
                        },
                        4: {
                            "do": self.description,
                            "examine": "farmhouseStairsCellar"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }

        elif (self.zoneID == 13):  # farmhouseCellar

            self.summary = "This is a dank and darkened cellar."
            self.description = '''The cellar contains a variety of preserved meats, canned fruits
and pickled vegetables. In one corner, there are a number of
alchemical instruments and tools, likely used by Alys in her
experiments. A packet of black powder lies on a workbench in this
area.'''
            self.items.clear()
            self.items = [9, 16]

            if(pc.globalStatus["Match Lit"] == False and pc.globalStatus["Lantern Lit"] == False):
                pc.globalStatus["Dark"] = True


            if(pc.globalStatus["farmhouseCellar examined"] == False):
                self.options = [
                    "Climb back out of the cellar",
                    "Look around the area",
                    "Player Menu"
                ]
                if(pc.globalStatus["Dark"] == True):
                    self.selection = {
                        1: {
                            "do": "You climb back out of the cellar, surfacing above ground.",
                            "moveTo": 12
                        },
                        2: {
                            "do": "It is too dark to look around. You hear faint noises in the dark."
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.selection = {
                        1: {
                            "do": "You climb back out of the cellar, surfacing above ground.",
                            "moveTo": 12
                        },
                        2: {
                            "do": self.description,
                            "examine": "farmhouseCellar"
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
            else:
                if(pc.globalStatus["Dark"] == True):
                    self.options = [
                        "Climb back out of the cellar",
                        "Look around the area",
                        "Player Menu"
                    ]
                    self.selection = {
                        1: {
                            "do": "You climb back out of the cellar, surfacing above ground.",
                            "moveTo": 12
                        },
                        2: {
                            "do": "It is too dark to look around. You hear faint noises in the dark."
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
                else:
                    if(pc.globalStatus["Alchemical Powder taken"] == False):
                        self.options = [
                            "Climb back out of the cellar",
                            "Take the alchemical powder",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You climb back out of the cellar, surfacing above ground.",
                                "moveTo": 12
                            },
                            2: {
                                "do": "You grab the packet of Alchemical Powder.",
                                "takeItem": 16
                            },
                            3: {
                                "do": self.description,
                                "examine": "farmhouseCellar"
                            },
                            4: {
                                "menu": "menu"
                            }
                        }
                    elif(pc.globalStatus["Alchemical Powder taken"] == True):
                        self.description = '''The cellar contains a variety of preserved meats, canned fruits
and pickled vegetables. In one corner, there are a number of
alchemical instruments and tools, likely used by Alys in her
experiments.'''
                        self.options = [
                            "Climb back out of the cellar",
                            "Look around the area",
                            "Player Menu"
                        ]
                        self.selection = {
                            1: {
                                "do": "You climb back out of the cellar, surfacing above ground.",
                                "moveTo": 12
                            },
                            2: {
                                "do": self.description,
                                "examine": "farmhouseCellar"
                            },
                            3: {
                                "menu": "menu"
                            }
                        }








        ### PRAIRIE ###------------------------------------------------------------------------ -|

        elif (self.zoneID == 14):  # prairieBackyard / Garden (HUB)
            self.summary = '''An open prairie with a small garden. To the south is a barn, and
nearby are an outhouse, a shed, and a well. To the north is the
dense cornfield.'''
            self.description = '''The garden contains a variety of produce, as well as autumn
flowers and a handful of decorative gourds growing, ready for
harvest soon. Standing resolute in the center of the crops is
a looming scarecrow - nearly 8 feet tall on its wooden cross,
arms outstretched, and hands hanging like claws. Its face is a
burlap sack taught over some small ovoid shape, giving an uncanny
likeness to a human head; its face stares blankly at the barn.
You spot a shiny gold coin on the ground.'''
            self.items.clear()
            self.items = [5]

            if(pc.globalStatus["prairieBackyard examined"] == False):
                self.options = [
                    "Walk to the Barn",
                    "Head to the Outhouse",
                    "Go to the Shed",
                    "Head North to the Cornfield",
                    "Walk back to the front of the house",
                    "Head to the cellar doors",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": '''You stroll over to the Barn.''',
                        "moveTo": 19
                    },
                    2: {
                        "do": '''You take a few steps and end up at the Outhouse.''',
                        "moveTo": 18
                    },
                    3: {
                        "do": '''You walk over to the Shed.''',
                        "moveTo": 16
                    },
                    4: {
                        "do": '''You start walking North, toward the cornfield.''',
                        "moveTo": 24
                    },
                    5: {
                        "do": '''You return to the front of the house.''',
                        "moveTo": 1
                    },
                    6: {
                        "do": '''You walk around the side of the house to the cellar doors.''',
                        "moveTo": 12
                    },
                    7: {
                        "do": self.description,
                        "examine": "prairieBackyard"
                    },
                    8: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Gold Coin taken"] == False):
                    self.options = [
                        "Walk to the Barn",
                        "Head to the Outhouse",
                        "Go to the Shed",
                        "Head North to the Cornfield",
                        "Walk back to the front of the house",
                        "Head to the cellar doors",
                        "Pick up the coin",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": '''You stroll over to the Barn.''',
                            "moveTo": 19
                        },
                        2: {
                            "do": '''You take a few steps and end up at the Outhouse.''',
                            "moveTo": 18
                        },
                        3: {
                            "do": '''You walk over to the Shed.''',
                            "moveTo": 16
                        },
                        4: {
                            "do": '''You start walking North, toward the cornfield.''',
                            "moveTo": 24
                        },
                        5: {
                            "do": '''You return to the front of the house.''',
                            "moveTo": 1
                        },
                        6: {
                            "do": '''You walk around the side of the house to the cellar doors.''',
                            "moveTo": 12
                        },
                        7: {
                            "do": "You bend down and pick up the coin, it's unlike normal coins you have seen.",
                            "takeItem": 5
                        },
                        8: {
                            "do": self.description,
                            "examine": "prairieBackyard"
                        },
                        9: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''The garden contains a variety of produce, as well as autumn
flowers and a handful of decorative gourds growing, ready for
harvest soon. Standing resolute in the center of the crops is
a looming scarecrow - nearly 8 feet tall on its wooden cross,
arms outstretched, and hands hanging like claws. Its face is a
burlap sack taught over some small ovoid shape, giving an uncanny
likeness to a human head; its face stares blankly at the barn.'''
                    self.options = [
                        "Walk to the Barn",
                        "Head to the Outhouse",
                        "Go to the Shed",
                        "Head North to the Cornfield",
                        "Walk back to the front of the house",
                        "Head to the cellar doors",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": '''You stroll over to the Barn.''',
                            "moveTo": 19
                        },
                        2: {
                            "do": '''You take a few steps and end up at the Outhouse.''',
                            "moveTo": 18
                        },
                        3: {
                            "do": '''You walk over to the Shed.''',
                            "moveTo": 16
                        },
                        4: {
                            "do": '''You start walking North, toward the cornfield.''',
                            "moveTo": 24
                        },
                        5: {
                            "do": '''You return to the front of the house.''',
                            "moveTo": 1
                        },
                        6: {
                            "do": '''You walk around the side of the house to the cellar doors.''',
                            "moveTo": 12
                        },
                        7: {
                            "do": self.description,
                            "examine": "prairieBackyard"
                        },
                        8: {
                            "menu": "menu"
                        }
                    }


        elif (self.zoneID == 15):  # prairieWell
            self.summary = '''In the midst of the open field is a medium sized well made of
stone, with a tented roof and strong wooden frame.'''
            self.description = '''This well sits not too far from the house, in the open field of
the praririe. From here, you can see the back of the Barn, the
Shed, the Outhouse, and the garden, including its stalwart scare-
crow. The well itself looks handmade. There is a rope pulley
system attached to the roofing, clearly for hoisting and lowering
a bucket for water.'''
            self.items.clear()
            self.items = [20]

            if(pc.globalStatus["prairieWell examined"] == False):
                self.options = [
                    "Head to the Outhouse",
                    "Go to the Shed",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": '''You walk back toward the Outhouse.''',
                        "moveTo": 18
                    },
                    2: {
                        "do": '''You walk over to the Shed.''',
                        "moveTo": 16
                    },
                    3: {
                        "do": self.description,
                        "examine": "prairieWell"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["prairieWell obstruction destroyed"] == False):
                    self.options = [
                        "Head to the Outhouse",
                        "Go to the Shed",
                        "Pull the rope",
                        "Peer into the Well",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": '''You walk back toward the Outhouse.''',
                            "moveTo": 18
                        },
                        2: {
                            "do": '''You walk over to the Shed.''',
                            "moveTo": 16
                        },
                        3: {
                            "do": '''You pull the rope to hoist the bucket up, but something blocks
its path, and it is stuck.'''
                        },
                        4: {
                            "do": '''You take a look down into the well. Some sort of stony obstruction
seems to be lodged halfway down.'''
                        },
                        5: {
                            "do": self.description,
                            "examine": "prairieWell"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                else:
                    if(pc.globalStatus["Emerald Merkaba taken"] == False):
                        self.options = [
                            "Head to the Outhouse",
                            "Go to the Shed",
                            "Pull the rope",
                            "Peer into the Well",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": '''You walk back toward the Outhouse.''',
                                "moveTo": 18
                            },
                            2: {
                                "do": '''You walk over to the Shed.''',
                                "moveTo": 16
                            },
                            3: {
                                "do": '''You pull the rope to hoist the bucket, which comes up with ease.
The bucket is filled with some water, and sitting at the bottom is a glimmering green stone object.''',
                                "takeItem": 20
                            },
                            4: {
                                "do": '''You take a look down into the well. It is now clear of any
obstructions, and you can see a bucket below. Inside the bucket
you can make out some water, and a shining green stone.''',
                                "examine": "prairieWell Inside"
                            },
                            5: {
                                "do": self.description,
                                "examine": "prairieWell"
                            },
                            6: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.options = [
                            "Head to the Outhouse",
                            "Go to the Shed",
                            "Peer into the Well",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": '''You walk back toward the Outhouse.''',
                                "moveTo": 18
                            },
                            2: {
                                "do": '''You walk over to the Shed.''',
                                "moveTo": 16
                            },
                            3: {
                                "do": '''You take a look down into the well. It is now clear of any
obstructions, and you can see a bucket below. Inside the bucket
you can make out some water, and a shining green stone.''',
                                "examine": "prairieWell Inside"
                            },
                            4: {
                                "do": self.description,
                                "examine": "prairieWell"
                            },
                            5: {
                                "menu": "menu"
                            }
                        }



        elif (self.zoneID == 16):  # prairieShedExterior
            self.summary = '''A small, drab shed, still standing. It has a slanted roof, and a
single door.'''
            self.items.clear()
            self.items = []

            # IF THE SHED IS LOCKED
            if(pc.globalStatus["prairieShedExterior Unlocked toggle"] == False):
                self.description = '''The Shed is built of different wood than the house and barn, and
almost seems older. Perhaps it was already here. As if to
emphasize its difference from the other buildings on this land,
the shed is locked with a large metal padlock, which takes a key.'''
                self.options = [
                    "Return to the Garden",
                    "Head to the Well",
                    "Walk over to the barn",
                    "Head to the outhouse",
                    "Unlock the shed door",
                    "Look around the area",
                    "Player Menu"
                ]

                if(21 in pc.inventory):

                    self.selection = {
                        1: {
                            "do": "You head back toward the Garden, and its scarecrow.",
                            "moveTo": 14
                        },
                        2: {
                            "do": "You walk over to the stone water well.",
                            "moveTo": 15
                        },
                        3: {
                            "do": "You walk over to the large barn.",
                            "moveTo": 22
                        },
                        4: {
                            "do": "You walk behind the shed, toward the outhouse.",
                            "moveTo": 18
                        },
                        5: {
                            "do": '''You use the brass key that you found in the stable, and the door
unlocks.''',
                            "toggle": "prairieShedExterior Unlocked"

                        },
                        6: {
                            "do": self.description,
                            "examine": "prairieShedExterior"
                        },
                        7: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.selection = {
                        1: {
                            "do": "You head back toward the Garden, and its scarecrow.",
                            "moveTo": 14
                        },
                        2: {
                            "do": "You walk over to the stone water well.",
                            "moveTo": 15
                        },
                        3: {
                            "do": "You walk over to the large barn.",
                            "moveTo": 22
                        },
                        4: {
                            "do": "You walk behind the shed, toward the outhouse.",
                            "moveTo": 18
                        },
                        5: {
                            "do": '''You require a key to unlock this door. Try looking around.'''

                        },
                        6: {
                            "do": self.description,
                            "examine": "prairieShedExterior",
                        },
                        7: {
                            "menu": "menu"
                        }
                    }
            else:
                self.description = '''The Shed is built of different wood than the house and barn, and
almost seems older. Perhaps it was already here. This shed used
to be locked, but the swings on the handle, not open.'''
                self.options = [
                    "Return to the Garden",
                    "Head to the Well",
                    "Walk over to the barn",
                    "Head to the outhouse",
                    "Open the shed door",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head back toward the Garden, and its scarecrow.",
                        "moveTo": 14
                    },
                    2: {
                        "do": "You walk over to the stone water well.",
                        "moveTo": 15
                    },
                    3: {
                        "do": "You walk over to the large barn.",
                        "moveTo": 22
                    },
                    4: {
                        "do": "You walk behind the shed, toward the outhouse.",
                        "moveTo": 18
                    },
                    5: {
                        "do": '''You pull the door open and step inside.''',
                        "moveTo": 17

                    },
                    6: {
                        "do": self.description,
                        "examine": "prairieShedExterior",
                    },
                    7: {
                        "menu": "menu"
                    }
                }


        elif (self.zoneID == 17):  # prairieShedInterior
            self.summary = '''Inside the shed, there are a handful of tools, and boxes.'''
            self.description = '''The dimly lit interior of this shed is crowded with items: Some
yard tools including hoes, rakes, saws, poles, and other strange
implements you've never seen. On the floor is a stack of wide,
flat wooden boxes, which seem sturdy, probably used to haul
produce from the garden into the house.'''
            self.items.clear()
            self.items = [7, 18]

            if(pc.globalStatus["prairieShedInterior examined"] == False):
                if(pc.globalStatus["Lantern taken"] == False):
                    self.options = [
                        "Close the shed door",
                        "Take the Lantern",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the door to the shed.",
                            "moveTo": 16
                        },
                        2: {
                            "do": "You unhook the Lantern and fasten it to your bag.",
                            "takeItem": 7
                        },
                        3: {
                            "do": self.description,
                            "examine": "prairieShedInterior"
                        },
                        4: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.options = [
                        "Close the shed door",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You close the door to the shed.",
                            "moveTo": 16
                        },
                        2: {
                            "do": self.description,
                            "examine": "prairieShedInterior"
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
            else:
                if(pc.globalStatus["prairieShedInterior Boxes examined"] == False):
                    if(pc.globalStatus["Lantern taken"] == False):
                        self.options = [
                            "Close the shed door",
                            "Take the Lantern",
                            "Examine some of the boxes",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You close the door to the shed.",
                                "moveTo": 16
                            },
                            2: {
                                "do": "You unhook the Lantern and fasten it to your bag.",
                                "takeItem": 7
                            },
                            3: {
                                "do": '''You take a closer look at the boxes, moving some aside, and
you discover a small vial of some kind of blue liquid.''',
                                "examine": "prairieShedInterior Boxes"
                            },
                            4: {
                                "do": self.description,
                                "examine": "prairieShedInterior"
                            },
                            5: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.options = [
                            "Close the shed door",
                            "Examine some of the boxes",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You close the door to the shed.",
                                "moveTo": 16
                            },
                            2: {
                                "do": '''You take a closer look at the boxes, moving some aside, and
you discover a small vial of some kind of blue liquid.''',
                                "examine": "prairieShedInterior Boxes"
                            },
                            3: {
                                "do": self.description,
                                "examine": "prairieShedInterior"
                            },
                            4: {
                                "menu": "menu"
                            }
                        }
                else:
                    if(pc.globalStatus["Lantern taken"] == False):
                        if(pc.globalStatus["Acrid Solution taken"] == False):
                            self.options = [
                                "Close the shed door",
                                "Take the Lantern",
                                "Take the vial of blue liquid",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the door to the shed.",
                                    "moveTo": 16
                                },
                                2: {
                                    "do": "You unhook the Lantern and fasten it to your bag.",
                                    "takeItem": 7
                                },
                                3: {
                                    "do": '''You slip the vial into your backpack.''',
                                    "takeItem": 18
                                },
                                4: {
                                    "do": self.description,
                                    "examine": "prairieShedInterior"
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }
                        else:
                            self.options = [
                                "Close the shed door",
                                "Take the Lantern",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the door to the shed.",
                                    "moveTo": 16
                                },
                                2: {
                                    "do": "You unhook the Lantern and fasten it to your bag.",
                                    "takeItem": 7
                                },
                                3: {
                                    "do": self.description,
                                    "examine": "prairieShedInterior"
                                },
                                4: {
                                    "menu": "menu"
                                }
                            }
                    else:
                        if(pc.globalStatus["Acrid Solution taken"] == False):
                            self.options = [
                                "Close the shed door",
                                "Take the vial of blue liquid",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the door to the shed.",
                                    "moveTo": 16
                                },
                                2: {
                                    "do": '''You slip the vial into your backpack.''',
                                    "takeItem": 18
                                },
                                3: {
                                    "do": self.description,
                                    "examine": "prairieShedInterior"
                                },
                                4: {
                                    "menu": "menu"
                                }
                            }
                        else:
                            self.options = [
                                "Close the shed door",
                                "Look around the area",
                                "Player Menu"
                            ]

                            self.selection = {
                                1: {
                                    "do": "You close the door to the shed.",
                                    "moveTo": 16
                                },
                                2: {
                                    "do": self.description,
                                    "examine": "prairieShedInterior"
                                },
                                3: {
                                    "menu": "menu"
                                }
                            }

        elif (self.zoneID == 18):  # prairieOuthouse
            self.summary = '''A little outhouse, complete with moon cutout. From here you can
reach the shed, the well, and the garden.'''
            self.description = '''The outhouse is quaint and charming, a sure sign of country life,
and a nice reprieve from the odd circumstances surrounding Alys'
disappearance. Opening the door, you can see everything you'd
expect to find inside an outhouse. Nothing terrible exciting.'''
            self.items.clear()
            self.items = []

            self.options = [
                "Head to the shed",
                "Go to the well",
                "Return to the garden",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You head back to the shed.",
                    "moveTo": 16
                },
                2: {
                    "do": "You walk over to the well.",
                    "moveTo": 15
                },
                3: {
                    "do": "You return back to the prairie garden.",
                    "moveTo": 14
                },
                4: {
                    "do": self.description,
                    "examine": "prairieOuthouse"
                },
                5: {
                    "menu": "menu"
                }
            }





        # |- --- ### BARN ----------------------------------------------------------------------- -|

        elif (self.zoneID == 19):  # barnFront
            self.summary = '''The plain front of this barn. The doors stand open, just a crack,
and in the distance you can see the backyard garden, the shed, and the well.'''
            self.description = '''The paint has started to peel in places, but still seems fairly
fresh over the door. The walls themselves are untreated, and raw,
remeniscent of the trees at the edges of the property. Tucked
into a nook in the wall you find a small folded note.'''
            self.items.clear()
            self.items = [10]

            if(pc.globalStatus["barnFront examined"] == False):
                self.options = [
                    "Head back to the Gardens",
                    "Walk into the open barn",
                    "Head to the back of the barn",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You turn back and return to the Garden.",
                        "moveTo": 14
                    },
                    2: {
                        "do": "You move through the open doors, into the barn.",
                        "moveTo": 20
                    },
                    3: {
                        "do": "Walk around the barn to the rear",
                        "moveTo": 22
                    },
                    4: {
                        "do": self.description,
                        "examine": "barnFront"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Hidden Note 3 taken"] == False):
                    self.options = [
                        "Head back to the Gardens",
                        "Walk into the open barn",
                        "Head to the back of the barn",
                        "Pick up the note",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You turn back and return to the Garden.",
                            "moveTo": 14
                        },
                        2: {
                            "do": "You move through the open doors, into the barn.",
                            "moveTo": 20
                        },
                        3: {
                            "do": "Walk around the barn to the rear",
                            "moveTo": 22
                        },
                        4: {
                            "do": "You pull the note out of the nook it's stuck in.",
                            "takeItem": 10
                        },
                        5: {
                            "do": self.description,
                            "examine": "barnFront"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''The paint has started to peel in places, but still seems fairly
fresh over the door. The walls themselves are untreated, and raw,
remeniscent of the trees at the edges of the property.'''
                    self.options = [
                        "Head back to the Gardens",
                        "Walk into the open barn",
                        "Head to the back of the barn",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You turn back and return to the Garden.",
                            "moveTo": 14
                        },
                        2: {
                            "do": "You move through the open doors, into the barn.",
                            "moveTo": 20
                        },
                        3: {
                            "do": "Walk around the barn to the rear",
                            "moveTo": 22
                        },
                        4: {
                            "do": self.description,
                            "examine": "barnFront"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }


        elif (self.zoneID == 20):  # barnInterior
            self.summary = '''The interior of the barn. There is a ladder to the loft, there
are some stables in the back, and exits in the front and rear.'''
            self.description = '''The dense smell of animal fur and waste hangs tightly to
the air, though no animals are to be found. A pitchfork rests on
a hook on one of the middle support pillars, its wrought iron the
product of a local forge. Hay clings to its forks, and litters
the ground on all sides of the barn. The pens and styes are
empty. Even the hen house is silent.'''
            self.items.clear()
            self.items = [13]

            if(pc.globalStatus["barnInterior examined"] == False):
                self.options = [
                    "Exit the barn doors",
                    "Explore the stable",
                    "Climb the ladder",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head back outside through the front doors.",
                        "moveTo": 19
                    },
                    2: {
                        "do": "You walk to the rear of the barn and check out the empty stables.",
                        "moveTo": 23
                    },
                    3: {
                        "do": "You climb the metal ladder and enter the hay loft.",
                        "moveTo": 21
                    },
                    4: {
                        "do": self.description,
                        "examine": "barnInterior"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Pitchfork taken"] == False):
                    self.options = [
                        "Exit the barn doors",
                        "Explore the stable",
                        "Climb the ladder",
                        "Take the Pitchfork",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You head back outside through the front doors.",
                            "moveTo": 19
                        },
                        2: {
                            "do": "You walk to the rear of the barn and check out the empty stables.",
                            "moveTo": 23
                        },
                        3: {
                            "do": "You climb the metal ladder and enter the hay loft.",
                            "moveTo": 21
                        },
                        4: {
                            "do": "You lift the pitchfork off its hook, and strap it to your back.",
                            "takeItem": 13
                        },
                        5: {
                            "do": self.description,
                            "examine": "barnInterior"
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.description = '''The dense smell of animal fur and waste hangs tightly to
the air, though no animals are to be found. An empty hook used to
hold a pitchfork. Hay litters the ground on all sides of the
barn. The pens and styes are empty. Even the hen house is silent.'''
                    self.options = [
                        "Exit the barn doors",
                        "Explore the stable",
                        "Climb the ladder",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You head back outside through the front doors.",
                            "moveTo": 19
                        },
                        2: {
                            "do": "You walk to the rear of the barn and check out the empty stables.",
                            "moveTo": 23
                        },
                        3: {
                            "do": "You climb the metal ladder and enter the hay loft.",
                            "moveTo": 21
                        },
                        4: {
                            "do": self.description,
                            "examine": "barnInterior"
                        },
                        5: {
                            "menu": "menu"
                        }
                    }


        elif (self.zoneID == 21):  # barnLoft
            self.summary = '''This loft is small, and somewhat cramped with a low angled
ceiling. There is a workbench on one side, and the floor is
littered with hay, which also lies in stacks near the wall.'''
            self.description = '''The cozy loft is full up with hay, stacked in piles, but it is
also home to a small workshop bench, and some minor crafts tools.
It appears that someone used this spot to build things, and work
on honing their craft skills. Leather and bits of metal cover
the floor, mixed in with some of the hay, closer to the bench.'''
            self.items.clear()
            self.items = [23]

            if(pc.globalStatus["Match Lit"] == False and pc.globalStatus["Lantern Lit"] == False):
                pc.globalStatus["Dark"] = True
                self.summary = "This loft is quite dark without a light, and there are no windows..."
                self.description = '''It is too dark to make much out, but hay is scattered about the
floor, and stacked up along the wall.'''

            if(pc.globalStatus["barnLoft examined"] == False):
                self.options = [
                    "Climb back down the ladder",
                    "Look around the area",
                    "Player Menu"
                ]

                if(pc.globalStatus["Dark"] == True):
                    self.selection = {
                        1: {
                            "do": "You climb back down the ladder.",
                            "moveTo": 20
                        },
                        2: {
                            "do": "It is too dark to see."
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.selection = {
                        1: {
                            "do": "You climb back down the ladder.",
                            "moveTo": 20
                        },
                        2: {
                            "do": self.description,
                            "examine": "barnLoft"
                        },
                        3: {
                            "menu": "menu"
                        }
                    }
            else:
                if(pc.globalStatus["barnLoft Workbench examined"] == False):
                    self.options = [
                        "Climb back down the ladder",
                        "Examine the workbench",
                        "Look around the area",
                        "Player Menu"
                    ]

                    if(pc.globalStatus["Dark"] == True):
                        self.selection = {
                            1: {
                                "do": "You climb back down the ladder.",
                                "moveTo": 20
                            },
                            2: {
                                "do": '''It's too dark to make out what's on the bench.'''
                            },
                            3: {
                                "do": "It is too dark to see."
                            },
                            4: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.selection = {
                            1: {
                                "do": "You climb back down the ladder.",
                                "moveTo": 20
                            },
                            2: {
                                "do": '''The workbench has a variety of drawings, like schematics, and
several odds and ends on top and sticking out from underneath it.
These objects are confounding, but appear to be the makings of
some kind of machines. There is a small journal on the desk.''',
                                "examine": "barnLoft Workbench"
                            },
                            3: {
                                "do": self.description,
                                "examine": "barnLoft"
                            },
                            4: {
                                "menu": "menu"
                            }
                        }

                else:
                    if(pc.globalStatus["barnLoft Workbench Journal examined"] == False):
                        self.options = [
                            "Climb back down the ladder",
                            "Examine the workbench",
                            "Skim the journal",
                            "Look around the area",
                            "Player Menu"
                        ]

                        if(pc.globalStatus["Dark"] == True):
                            self.selection = {
                                1: {
                                    "do": "You climb back down the ladder.",
                                    "moveTo": 20
                                },
                                2: {
                                    "do": '''It's too dark to make out what's on the bench.'''
                                },
                                3: {
                                    "do": "It's too dark to read the journal."
                                },
                                4: {
                                    "do": "It is too dark to see."
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }
                        else:
                            self.selection = {
                                1: {
                                    "do": "You climb back down the ladder.",
                                    "moveTo": 20
                                },
                                2: {
                                    "do": '''The workbench has a variety of drawings, like schematics, and
several odds and ends on top and sticking out from underneath it.
These objects are confounding, but appear to be the makings of
some kind of machines. There is a small journal on the desk.''',
                                    "examine": "barnLoft Workbench"
                                },
                                3: {
                                    "do": '''You pick up the journal and skim its pages. Most of it appears to
be schematics and notes about creations. It appears to be in
handwriting different to Alys' own handwriting. More angular, and
jagged, but with a simple elegance about it. As you flip through,
a loose page falls out and onto the workbench.''',
                                    "examine": "barnLoft Workbench Journal"
                                },
                                4: {
                                    "do": self.description,
                                    "examine": "barnLoft"
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }
                    else:
                        if(pc.globalStatus["Journal Page taken"] == False):
                            self.options = [
                                "Climb back down the ladder",
                                "Examine the workbench",
                                "Take the loose page",
                                "Look around the area",
                                "Player Menu"
                            ]

                            if(pc.globalStatus["Dark"] == True):
                                self.selection = {
                                    1: {
                                        "do": "You climb back down the ladder.",
                                        "moveTo": 20
                                    },
                                    2: {
                                        "do": '''It's too dark to make out what's on the bench.'''
                                    },
                                    3: {
                                        "do": "You pick up the page and slip it in with your things.",
                                        "takeItem": 23
                                    },
                                    4: {
                                        "do": "It is too dark to see."
                                    },
                                    5: {
                                        "menu": "menu"
                                    }
                                }
                            else:
                                self.selection = {
                                    1: {
                                        "do": "You climb back down the ladder.",
                                        "moveTo": 20
                                    },
                                    2: {
                                        "do": '''The workbench has a variety of drawings, like schematics, and
several odds and ends on top and sticking out from underneath it.
These objects are confounding, but appear to be the makings of
some kind of machines. There is a small journal on the desk.''',
                                        "examine": "barnLoft Workbench"
                                    },
                                    3: {
                                        "do": "You pick up the page and slip it in with your things.",
                                        "takeItem": 23
                                    },
                                    4: {
                                        "do": self.description,
                                        "examine": "barnLoft"
                                    },
                                    5: {
                                        "menu": "menu"
                                    }
                                }
                        else:
                            self.options = [
                                "Climb back down the ladder",
                                "Examine the workbench",
                                "Look around the area",
                                "Player Menu"
                            ]

                            if(pc.globalStatus["Dark"] == True):
                                self.selection = {
                                    1: {
                                        "do": "You climb back down the ladder.",
                                        "moveTo": 20
                                    },
                                    2: {
                                        "do": '''It's too dark to make out what's on the bench.'''
                                    },
                                    3: {
                                        "do": "It is too dark to see.",
                                        "examine": "barnLoft"
                                    },
                                    4: {
                                        "menu": "menu"
                                    }
                                }
                            else:
                                self.selection = {
                                    1: {
                                        "do": "You climb back down the ladder.",
                                        "moveTo": 20
                                    },
                                    2: {
                                        "do": '''The workbench has a variety of drawings, like schematics, and
several odds and ends on top and sticking out from underneath it.
These objects are confounding, but appear to be the makings of
some kind of machines. There is a small journal on the desk.''',
                                        "examine": "barnLoft Workbench"
                                    },
                                    3: {
                                        "do": self.description,
                                        "examine": "barnLoft"
                                    },
                                    4: {
                                        "menu": "menu"
                                    }
                                }




        elif (self.zoneID == 22):  # barnBack
            self.summary = '''The rear side of the barn. From here you can see the Well and Outhouse'''
            self.description = '''Behind the barn, you are standing near the edge of the woods on
the South end of the property. North of the barn you can see the
rest of the property. On the ground, you see a trail of blood
from the stable.'''
            self.items.clear()
            self.items = []

            if(pc.globalStatus["barnBack examined"] == False):

                self.options = [
                    "Go inside the barn",
                    "Head around to the front of the barn",
                    "Walk over to the Shed",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head inside the barn.",
                        "moveTo": 23
                    },
                    2: {
                        "do": "You walk around the barn to the front.",
                        "moveTo": 19
                    },
                    3: {
                        "do": "You take the path over to the Shed.",
                        "moveTo": 16
                    },
                    4: {
                        "do": self.description,
                        "examine": "barnBack"
                    },
                    5: {
                        "menu": "menu"
                    }
                }

            else:
                self.options = [
                    "Go inside the barn",
                    "Head around to the front of the barn",
                    "Walk over to the Shed",
                    "Examine the bloodtrail",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head inside the barn.",
                        "moveTo": 23
                    },
                    2: {
                        "do": "You walk around the barn to the front.",
                        "moveTo": 19
                    },
                    3: {
                        "do": "You take the path over to the Shed.",
                        "moveTo": 16
                    },
                    4: {
                        "do": '''You bend down and take a closer look at the bloodtrail. It's
dried, but it doesn't seem more than a day old, it's still red.
You can tell that something - or someone - was dragged from the
barn stable to the north. You also spot tiny footprints in some
of the blood streaks. Looking in the distance, you see the wall
of corn at the other end of the property.'''
                    },
                    5: {
                        "do": self.description,
                        "examine": "barnBack"
                    },
                    6: {
                        "menu": "menu"
                    }
                }


        elif (self.zoneID == 23):  # barnStable
            self.summary = '''The back end of the barn, a set of four stables with closed doors.'''
            self.description = '''There are four stables, two on either side, with doors that look
handmade, and painted a dull white. Each door is latched, but not
locked. Behind the stables you see signs of horses having lived
here, but there are no horses to be found.'''
            self.items.clear()
            self.items = [21]

            if(pc.globalStatus["barnBack examined"] == False):

                self.options = [
                    "Head back to the pens",
                    "Walk out the back door",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You walk to the front side of the barn's interior.",
                        "moveTo": 20
                    },
                    2: {
                        "do": "You walk through the small door and outside the back of the barn.",
                        "moveTo": 22
                    },
                    3: {
                        "do": self.description,
                        "examine": "barnBack"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["barnStable stall3 examined"] == False):

                    self.options = [
                        "Head back to the pens",
                        "Walk out the back door",
                        "Examine the first stall",
                        "Examine the second stall",
                        "Examine the third stall",
                        "Examine the fourth stall",
                        "Look around the area",
                        "Player Menu"
                    ]

                    self.selection = {
                        1: {
                            "do": "You walk to the front side of the barn's interior.",
                            "moveTo": 20
                        },
                        2: {
                            "do": "You walk through the small door and outside the back of the barn.",
                            "moveTo": 22
                        },
                        3: {
                            "do": '''You open the door of the first stall and look inside. The ground
is barren, except some hay, and you can see horse prints. A
saddle rests on a hook at the back of the stall.'''
                        },
                        4: {
                            "do": '''The door of the second stall was already open a crack. You push
it the rest of the way, and see that the ground is empty, except
for horse prints, and horseshoe marks. Some dark brown fur can
also be seen on the ground, and caught into the wooden joints of
the stall walls. A saddle rests on a hook at the back of the
stall.'''
                        },
                        5: {
                            "do": '''The third stall's door creaks as you push it open, and
immediately you see blood on the ground. A faint trail leads out
of the stables, out the back of the barn. It's sparse, but
consistent. You also spot a key nearby the pool of drying blood.''',
                            "examine": "barnStable stall3"
                        },
                        6: {
                            "do": '''The fourth stall's door seems to be broken, and it's stuck shut.
However, you can see the inside of the stall from above the
doors, and it is empty.'''
                        },
                        7: {
                            "do": self.description,
                            "examine": "barnBack"
                        },
                        8: {
                            "menu": "menu"
                        }
                    }
                else:
                    if(pc.globalStatus["Brass Key taken"] == False):
                        self.options = [
                            "Head back to the pens",
                            "Walk out the back door",
                            "Examine the first stall",
                            "Examine the second stall",
                            "Examine the third stall",
                            "Examine the fourth stall",
                            "Take the key",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You walk to the front side of the barn's interior.",
                                "moveTo": 20
                            },
                            2: {
                                "do": "You walk through the small door and outside the back of the barn.",
                                "moveTo": 22
                            },
                            3: {
                                "do": '''You open the door of the first stall and look inside. The ground
is barren, except some hay, and you can see horse prints. A
saddle rests on a hook at the back of the stall.'''
                            },
                            4: {
                                "do": '''The door of the second stall was already open a crack. You push
it the rest of the way, and see that the ground is empty, except
for horse prints, and horseshoe marks. Some dark brown fur can
also be seen on the ground, and caught into the wooden joints of
the stall walls. A saddle rests on a hook at the back of the
stall.'''
                            },
                            5: {
                                "do": '''The third stall's door creaks as you push it open, and
immediately you see blood on the ground. A faint trail leads out
of the stables, out the back of the barn. It's sparse, but
consistent. You also spot a key nearby the pool of drying blood.''',
                                "examine": "barnStable stall3"
                            },
                            6: {
                                "do": '''The fourth stall's door seems to be broken, and it's stuck shut.
However, you can see the inside of the stall from above the
doors, and it is empty.'''
                            },
                            7: {
                                "do": "You pick up the bloody key.",
                                "takeItem": 21
                            },
                            8: {
                                "do": self.description,
                                "examine": "barnBack"
                            },
                            9: {
                                "menu": "menu"
                            }
                        }
                    else:
                        self.options = [
                            "Head back to the pens",
                            "Walk out the back door",
                            "Examine the first stall",
                            "Examine the second stall",
                            "Examine the third stall",
                            "Examine the fourth stall",
                            "Look around the area",
                            "Player Menu"
                        ]

                        self.selection = {
                            1: {
                                "do": "You walk to the front side of the barn's interior.",
                                "moveTo": 20
                            },
                            2: {
                                "do": "You walk through the small door and outside the back of the barn.",
                                "moveTo": 22
                            },
                            3: {
                                "do": '''You open the door of the first stall and look inside. The ground
is barren, except some hay, and you can see horse prints. A
saddle rests on a hook at the back of the stall.'''
                            },
                            4: {
                                "do": '''The door of the second stall was already open a crack. You push
it the rest of the way, and see that the ground is empty, except
for horse prints, and horseshoe marks. Some dark brown fur can
also be seen on the ground, and caught into the wooden joints of
the stall walls. A saddle rests on a hook at the back of the
stall.'''
                            },
                            5: {
                                "do": '''The third stall's door creaks as you push it open, and
immediately you see blood on the ground. A faint trail leads out
of the stables, out the back of the barn. It's sparse, but
consistent. You also spot a key nearby the pool of drying blood.''',
                                "examine": "barnStable stall3"
                            },
                            6: {
                                "do": '''The fourth stall's door seems to be broken, and it's stuck shut.
However, you can see the inside of the stall from above the
doors, and it is empty.'''
                            },
                            7: {
                                "do": self.description,
                                "examine": "barnBack"
                            },
                            8: {
                                "menu": "menu"
                            }
                        }




        # |- --- ### CORNFIELD ------------------------------------------------------------------ -|

        elif (self.zoneID == 24):  # cornfieldEdge
            self.summary = '''The northern boundary of the yard, a solid wall of very tall corn.'''
            self.description = '''The perfectly groomed wall of corn stalks stretches far from East
to West, and seems to act as a fortress wall, protecting
something beyond. Upon closer inspection of the corn wall, you
discover somewhere you could slip into, and what looks like a
path beyond. Looking around, you spot a blood trail which
leads from the Southern part of the yard to this wall of corn.'''
            self.items.clear()

            if(pc.globalStatus["cornfieldEdge examined"] == False):

                self.options = [
                    "Walk back to the Farmstead",
                    "Head back to the Garden",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You walk to the front of the farm house.",
                        "moveTo": 1
                    },
                    2: {
                        "do": "You walk toward the praririe Garden.",
                        "moveTo": 14
                    },
                    3: {
                        "do": self.description,
                        "examine": "cornfieldEdge"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                self.options = [
                    "Walk back to the Farmstead",
                    "Head back to the Garden",
                    "Slip into the corn, past the edge",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You walk to the front of the farm house.",
                        "moveTo": 1
                    },
                    2: {
                        "do": "You walk toward the praririe Garden.",
                        "moveTo": 14
                    },
                    3: {
                        "do": '''You bend back some of the corn, and manage to wriggle into the cornfield itself. Between the rows of stalks, you see what appears to be a small path leading deeper in.''',
                        "moveTo": 25
                    },
                    4: {
                        "do": self.description,
                        "examine": "cornfieldEdge"
                    },
                    5: {
                        "menu": "menu"
                    }
                }


        elif (self.zoneID == 25):  # cornfieldThick
            self.summary = '''Inside the cornfield, here, the corn begins to get thicker.'''
            self.description = '''All around, you are surrounded by corn. It is getting thicker,
and harder to move, but you can still see a path forward.'''
            self.items.clear()

            self.options = [
                "Exit the corn",
                "Continue deeper into the cornfield",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You make your way back out of the corn.",
                    "moveTo": 24
                },
                2: {
                    "do": '''You keep going, pushing through the tall stalks, making consider-
able noise.''',
                    "moveTo": 26
                },
                3: {
                    "do": self.description,
                    "examine": "cornfieldThick"
                },
                4: {
                    "menu": "menu"
                }
            }


        elif (self.zoneID == 26):  # cornfieldTangle
            self.summary = '''Inside the cornfield, here, it's getting quite difficult to move.'''
            self.description = '''The corn continues to grow denser, and seems to be growing more
wild. It's almost as if you are caught in a natural tangle of
corn, which is so thick you can't even see the soil beneath. Yet,
you can still see a path forward.'''
            self.items.clear()

            self.options = [
                "Exit the corn",
                "Continue deeper into the cornfield",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You make your way back out of the corn.",
                    "moveTo": 24
                },
                2: {
                    "do": '''.''',
                    "moveTo": 27
                },
                3: {
                    "do": self.description,
                    "examine": "cornfieldThick"
                },
                4: {
                    "menu": "menu"
                }
            }


        elif (self.zoneID == 27):  # cornfieldMazeStart
            self.summary = '''The beginning of what is obviously a corn maze.'''
            self.description = '''The walls of corn on either side are straight as a blade, and the
corn stretches high above your head, higher than before, you
think. The path continues forward, and it looks like there might
be a T up ahead. The path is about 3 feet wide, comfortable
enough to move through unhindered.'''
            self.items.clear()

            self.options = [
                "South",
                "Enter the maze proper",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You turn around and head back through the thick corn.",
                    "moveTo": 25
                },
                2: {
                    "do": '''You march forward, into the maze.''',
                    "moveTo": 28
                },
                3: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                4: {
                    "menu": "menu"
                }
            }



        # |- -------------- ### ORANGE MAZE ### ------------------------------------------------- -|


        elif (self.zoneID == 28):  # cornfieldMaze1
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 32
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 29
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 30
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 27
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }


        elif (self.zoneID == 29):  # cornfieldMaze2
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 31
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 46
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 28
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }


        elif (self.zoneID == 30):  # cornfieldMaze3
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 33
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 28
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 47
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 31):  # cornfieldMaze4
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 34
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 46
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 32
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 29
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 32):  # cornfieldMaze5
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 31
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 33
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 28
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 33):  # cornfieldMaze6
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 35
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 32
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 47
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 30
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 34):  # cornfieldMaze7
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 36
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 44
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 31
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 35):  # cornfieldMaze8
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 38
                },
                2: {  # CENTER
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 48
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 45
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 33
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 36):  # cornfieldMaze9
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 39
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 42
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 37
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 34
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 37):  # cornfieldMaze10
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 40
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 36
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 38
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 38):  # cornfieldMaze11
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 41
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 37
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 43
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 35
                },
                5: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                6: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 39):  # cornfieldMaze12
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 42
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 40
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 36
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 40):  # cornfieldMaze13
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 39
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 41
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 37
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 41):  # cornfieldMaze14
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "West",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 40
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 43
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 38
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 42):  # cornfieldMaze15
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 39
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 36
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 44
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 43):  # cornfieldMaze16
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 41
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 38
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 45
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 44):  # cornfieldMaze17
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 42
                },
                2: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 34
                },
                3: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 46
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 45):  # cornfieldMaze18
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 43
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 35
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 47
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 46):  # cornfieldMaze19
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "East",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 44
                },
                3: {
                    "do": '''You walk East.''',  # EAST
                    "moveTo": 31
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 29
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 47):  # cornfieldMaze20
            self.summary = '''An intersection near the beginning of the maze.'''
            self.description = '''This maze is disorienting, as all of the intersections look
similar.'''
            self.items.clear()

            self.options = [
                "North",
                "West",
                "South",
                "Look around the area",
                "Player Menu"
            ]

            self.selection = {
                1: {
                    "do": "You walk North.",  # NORTH
                    "moveTo": 45
                },
                2: {
                    "do": '''You walk West.''',  # WEST
                    "moveTo": 33
                },
                4: {
                    "do": "You walk South.",  # SOUTH
                    "moveTo": 30
                },
                4: {
                    "do": self.description,
                    "examine": "cornfieldMazeStart"
                },
                5: {
                    "menu": "menu"
                }
            }

        elif (self.zoneID == 48):  # cornfieldMazeCenter
            self.summary = '''The center of the maze.'''
            self.items.clear()

            if(pc.globalStatus["Staircase Visible"]):
                self.description = '''An open clearing that appears to be pressed down in a large
circle, flattened to the ground. At the center of this clearing
is a stone staircase descending into the ground.'''
                self.options = [
                    "Return to the Maze",
                    "Descend the Stairs",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You head back to the maze.",  # EAST
                        "moveTo": 35
                    },
                    2: {
                        "do": '''You begin the descent down the stone steps.''',  # DOWN
                        "moveTo": 49
                    },
                    3: {
                        "do": self.description,
                        "examine": "cornfieldMazeStart"
                    },
                    4: {
                        "menu": "menu"
                    }
                }
            else:
                self.description = '''An open clearing that appears to be pressed down in a large
circle, flattened to the ground.'''
                self.options = [
                    "North",
                    "West",
                    "East",
                    "South",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You walk North.",  # NORTH
                        "moveTo": 37
                    },
                    2: {
                        "do": '''You walk West.''',  # WEST
                        "moveTo": 34
                    },
                    3: {
                        "do": '''You walk East.''',  # EAST
                        "moveTo": 35
                    },
                    4: {
                        "do": "You walk South.",  # SOUTH
                        "moveTo": 32
                    },
                    5: {
                        "do": self.description,
                        "examine": "cornfieldMazeStart"
                    },
                    6: {
                        "menu": "menu"
                    }
                }


        elif(self.zoneID == 49):
            self.summary = '''GAME WON.'''
            self.description = '''GAME WON.'''
            self.items.clear()

            self.options = [
                "Menu"
            ]

            self.selection = {
                1: {
                    "menu": "menu"
                }
            }


        elif(self.zoneID == 100):  # template
            self.summary = '''Simple summary.'''
            self.description = '''Complex Description for examination.'''
            self.items.clear()
            self.items = []

            if(pc.globalStatus["template examined"] == False):
                self.options = [
                    "Move ",
                    "Option",
                    "Option",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You move.",
                        "moveTo": 0
                    },
                    2: {

                    },
                    3: {

                    },
                    4: {
                        "do": self.description,
                        "examine": "template"
                    },
                    5: {
                        "menu": "menu"
                    }
                }
            else:
                self.options = [
                    "Move ",
                    "Option",
                    "Option",
                    "Option",
                    "Look around the area",
                    "Player Menu"
                ]

                self.selection = {
                    1: {
                        "do": "You move.",
                        "moveTo": 0
                    },
                    2: {

                    },
                    3: {

                    },
                    4: {

                    },
                    5: {
                        "do": self.description,
                        "examine": "template"
                    },
                    6: {
                        "menu": "menu"
                    }
                }
