# zones.py

from item import Item

class Zone:

    def __init__(self, zoneID, pc):

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
room. There are unlit candles on the table and around the room.'''
            self.items.clear()

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
            elif(pc.globalStatus["farmhouseKitchen examined"] == True):
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
                        "do": self.description
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
                            "do": '''You grab the boots and put them on, dried mud is crusted on the
sides, but they're comfortable.''',
                            "takeItem": 2
                        },
                        4: {
                            "do": '''You pull the box down and open it up, inside is a small crystal
trinket in the shape of a hexagon.''',
                            "examine": "farmhouseCloset1 Box"
                        },
                        5: {
                            "do": self.description
                        },
                        6: {
                            "menu": "menu"
                        }
                    }
                elif(pc.globalStatus["farmhouseCloset1 Box examined"] == True):
                    if(pc.globalStatus["Emerald Medallion taken"] == False):
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
                                "do": '''You grab the boots and put them on, dried mud is crusted on the
sides, but they're comfortable.''',
                                "takeItem": 2
                            },
                            4: {
                                "do": '''You gently lift the delicate charm out of the box, it is on a
silver chain. You put it in your pack.''',
                                "takeItem": 3
                            },
                            5: {
                                "do": self.description
                            },
                            6: {
                                "menu": "menu"
                            }
                        }

                    elif(pc.globalStatus["Emerald Medallion taken"] == True):
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
                                "do": '''You grab the boots and put them on, dried mud is crusted on the
sides, but they're comfortable.''',
                                "takeItem": 2
                            },
                            4: {
                                "do": self.description
                            },
                            5: {
                                "menu": "menu"
                            }
                        }


            elif(pc.globalStatus["Muddy Boots taken"] == True):
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
                            "do": '''You pull the box down and open it up, inside is a small crystal
trinket in the shape of a hexagon.''',
                            "examine": "farmhouseCloset1 Box"
                        },
                        4: {
                            "do": self.description
                        },
                        5: {
                            "menu": "menu"
                        }
                    }
                elif(pc.globalStatus["farmhouseCloset1 Box examined"] == True):
                    if(pc.globalStatus["Emerald Medallion taken"] == False):
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
                                "do": self.description
                            },
                            5: {
                                "menu": "menu"
                            }
                        }
                    elif(pc.globalStatus["Emerald Medallion taken"] == True):
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
                                "do": self.description
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
the body of the room. Around the edges are a basket with some
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
can see multiple sets, heading toward the kitchen at the front of
the house.''',
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
her late husband. A crest of the Astranos family featuring
thirteen stars around a circular labyrinth design with a heart
at the center.'''
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
            self.summary = "A simple closet, full of clothes, sheets, and other odds and ends."
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
sconces flank the door on either side. On top of the desk is a
black iron lantern with glass cage. You can also see that notes
are scattered about. Each contains formulae, sketches, and hastily
written theories and worries.'''
            self.items.clear()
            self.items = [7]
            if(pc.globalStatus["Match Lit"] == False and pc.globalStatus["Lantern Lit"] == False):
                pc.globalStatus["Dark"] = True

            if(pc.globalStatus["farmhouseStudy examined"] == False):
                self.options = [
                    "Return to the Bedroom",
                    "Exit to the hallway",
                    "Read papers",
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
                            "do": "It is too dark to make out what the notes say clearly."
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
                            "do": "You read the notes.",
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
                    if(pc.globalStatus["Lantern taken"] == False):
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Pick up the Lantern",
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
                                "do": "You pick up the iron Lantern, its wick still in good shape.",
                                "takeItem": 7
                            },
                            4: {
                                "do": "It is too dark to make out what the notes say clearly."
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
                            "Read the papers",
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
                                "do": "It is too dark to make out what the notes say clearly."
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
                    if(pc.globalStatus["Lantern taken"] == False):
                        self.options = [
                            "Return to the Bedroom",
                            "Exit to the hallway",
                            "Pick up the Lantern",
                            "Read the papers",
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
                                "do": "You pick up the iron Lantern, its wick still in good shape.",
                                "takeItem": 7
                            },
                            4: {
                                "do": "You read the notes.",
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
                            "Read the papers",
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
                                "do": "You read the notes.",
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
used for stuffing; extra pillows; sheets; a small wooden box containing some personal belongings
which likely belong to Alys' son, Dareth. There is an ITEM in the box.'''
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
stars sround the edge. In the center is an ornate labyrinth.'''
            self.items.clear()

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
                    "moveTo": 13
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
area. Along a wall, tucked under a jar of canned beats, you find
a small note.'''
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
                        if(pc.globalStatus["Hidden Note 2 taken"] == False):
                            self.options = [
                                "Climb back out of the cellar",
                                "Take the alchemical powder",
                                "Grab the note",
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
                                    "do": "You take the note.",
                                    "takeItem": 9
                                },
                                4: {
                                    "do": self.description,
                                    "examine": "farmhouseCellar"
                                },
                                5: {
                                    "menu": "menu"
                                }
                            }
                        else:
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
                        if(pc.globalStatus["Hidden Note 2 taken"] == False):
                            self.options = [
                                "Climb back out of the cellar",
                                "Grab the note",
                                "Look around the area",
                                "Player Menu"
                            ]
                            self.selection = {
                                1: {
                                    "do": "You climb back out of the cellar, surfacing above ground.",
                                    "moveTo": 12
                                },
                                2: {
                                    "do": "You take the note.",
                                    "takeItem": 9
                                },
                                3: {
                                    "do": self.description,
                                    "examine": "farmhouseCellar"
                                },
                                4: {
                                    "menu": "menu"
                                }
                            }
                        else:
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

        elif (self.zoneID == 14):  # prairieBackyard (HUB)
            self.summary = '''An open prairie with a small garden. To the south is a barn, and
nearby are an outhouse, a shed, and a well. To the north is the
dense cornfield.'''
            self.description = '''The garden contains a variety of produce, as well as autumn
flowers and a handful of decorative gourds growing, ready for
harvest soon.'''
            self.items.clear()
            self.items = [5]

            if(pc.globalStatus["prairieBackyard examined"] == False):
                self.options = [
                    "Walk to the Barn",
                    "Head to the Outhouse",
                    "Go to the Shed",
                    "Walk to the Well",
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
                        "do": '''You look into the Well.''',
                        "moveTo": 15
                    },
                    5: {
                        "do": '''You start walking North, toward the cornfield.''',
                        "moveTo": 24
                    },
                    6: {
                        "do": '''You return to the front of the house.''',
                        "moveTo": 1
                    },
                    7: {
                        "do": '''You walk around the side of the house to the cellar doors.''',
                        "moveTo": 12
                    },
                    8: {
                        "do": self.description,
                        "examine": "farmhouseStairsCellar"
                    },
                    9: {
                        "menu": "menu"
                    }
                }
            else:
                if(pc.globalStatus["Gold Coin taken"] == False):
                    self.options = [
                        "Walk to the Barn",
                        "Head to the Outhouse",
                        "Go to the Shed",
                        "Walk to the Well",
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
                            "do": '''You look into the Well.''',
                            "moveTo": 15
                        },
                        5: {
                            "do": '''You start walking North, toward the cornfield.''',
                            "moveTo": 24
                        },
                        6: {
                            "do": '''You return to the front of the house.''',
                            "moveTo": 1
                        },
                        7: {
                            "do": '''You walk around the side of the house to the cellar doors.''',
                            "moveTo": 12
                        },
                        8: {
                            "do": "You bend down and pick up the coin, it's unlike normal coins you have seen.",
                            "takeItem": 5
                        },
                        9: {
                            "do": self.description,
                            "examine": "farmhouseStairsCellar"
                        },
                        10: {
                            "menu": "menu"
                        }
                    }
                else:
                    self.options = [
                        "Walk to the Barn",
                        "Head to the Outhouse",
                        "Go to the Shed",
                        "Walk to the Well",
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
                            "do": '''You look into the Well.''',
                            "moveTo": 15
                        },
                        5: {
                            "do": '''You start walking North, toward the cornfield.''',
                            "moveTo": 24
                        },
                        6: {
                            "do": '''You return to the front of the house.''',
                            "moveTo": 1
                        },
                        7: {
                            "do": '''You walk around the side of the house to the cellar doors.''',
                            "moveTo": 12
                        },
                        8: {
                            "do": self.description,
                            "examine": "farmhouseStairsCellar"
                        },
                        9: {
                            "menu": "menu"
                        }
                    }




        # |- --- ### PRAIRIE ZONES -------------------------------------------------------------- -|

        elif (self.zoneID == 15):  # prairieWell
            print(f"zone {zoneID}")
        elif (self.zoneID == 16):  # prairieShedExterior
            print(f"zone {zoneID}")
        elif (self.zoneID == 17):  # prairieShedInterior
            print(f"zone {zoneID}")
        elif (self.zoneID == 18):  # prairieOuthouse
            print(f"zone {zoneID}")




        # |- --- ### BARN ----------------------------------------------------------------------- -|

        elif (self.zoneID == 19):  # barnFront
            print(f"zone {zoneID}")
        elif (self.zoneID == 20):  # barnInterior
            print(f"zone {zoneID}")
        elif (self.zoneID == 21):  # barnLoft
            print(f"zone {zoneID}")
        elif (self.zoneID == 22):  # barnBack
            print(f"zone {zoneID}")
        elif (self.zoneID == 23):  # barnStable
            print(f"zone {zoneID}")




        # |- --- ### CORNFIELD ------------------------------------------------------------------ -|

        elif (self.zoneID == 24):  # cornfieldEdge
            print(f"zone {zoneID}")
        elif (self.zoneID == 25):  # cornfieldThick
            print(f"zone {zoneID}")
        elif (self.zoneID == 26):  # cornfieldTangle
            print(f"zone {zoneID}")
        elif (self.zoneID == 27):  # cornfieldMazeStart
            print(f"zone {zoneID}")
        elif (self.zoneID == 28):  # cornfieldMaze1
            print(f"zone {zoneID}")
        elif (self.zoneID == 29):  # cornfieldMaze2
            print(f"zone {zoneID}")
        elif (self.zoneID == 30):  # cornfieldMaze3
            print(f"zone {zoneID}")
        elif (self.zoneID == 31):  # cornfieldMaze4
            print(f"zone {zoneID}")
        elif (self.zoneID == 32):  # cornfieldMaze5
            print(f"zone {zoneID}")
        elif (self.zoneID == 33):  # cornfieldMaze6
            print(f"zone {zoneID}")
        elif (self.zoneID == 34):  # cornfieldMaze7
            print(f"zone {zoneID}")
        elif (self.zoneID == 35):  # cornfieldMaze8
            print(f"zone {zoneID}")
        elif (self.zoneID == 36):  # cornfieldMaze9
            print(f"zone {zoneID}")
        elif (self.zoneID == 37):  # cornfieldMazeCenter
            print(f"zone {zoneID}")


        else:
            print(f"No zone")





# Start out the game on a farm. The farm has a barn filled with hay, other barn stuff and the remnants of animal denizens (no animals, at least not alive, maybe a stray cat.) The farm has two fields, one dense corn, one open grass and wheat with a scarecrow. The corn breaks into a small maze, with a spiral staircase leading underground at the middle. The farm also has a farmhouse, two floors and a cellar. There is a tool shed. There is an outhouse. Also there is a well. The farm is surrounded on two sides by thick woods, and on one side by the corn rows which stretch out several acres and butt up against more woods. The fourth side (East) is an open yard facing an old dirt road (thinking of my dad's house somewhat).

# The goal of this area is to introduce mechanics, provide light gear, and get the player ready to adventure beyond. Perhaps the middle of the corn maze opens up into a fae world, revealing a staircase which stretches deep underground...

    # FARMHOUSE:
    # The central building on the land, and the most prominent. This is a drag grey brown house built long ago, with thatched roofing. It is made mostly of wood and logs, with an almost log cabin feel to the exterior. The interior is dark, but during the day there is plenty of light from outside to see.

        ### Main floor
        # Entryway / Porch
        # Kitchen / Dining Room
        # Living Room / Great Room
        # Stairs leading up to second floor
        # Fireplace
        # Side closet

        ### Upper floor
        # Stairs leading down
        # Hallway splits floor in half. Left side is
        # Master bedroom and study. Right side is
        # Storage and
        # Guest bedroom
        # End of the hall opposite the stairs is a chest in front of a window

        ### Cellar
        # open area, shelves on three sides. Storage, cold box type stuff, jam, gunpowder, alchemical stuff, etc. Secrets? Only accessible from outside, door is locked.

    # BARN:
    # This is a large barn, brown and angular, with a thatched roof. It was designed and built alongside the house, so it looks similar. Inside, the ground floor is dirt, packed, and covered with sparse hay. There is a loft which takes up half the fixe of the barn, and is used to store hay. There is a pitch fork hung on a support pillar. There are some stables and pens, none of which house animals anymore. Some of the doors are open. There is blood on the hay in one of the stables, and a scrap of clothing, covered in the same blood. Someone was killed here, and moved from the spot afterward.

    # FIELDS:
    # There are two fields, a cornfield to the North, and a wheat / grass field to the South and behind the house to the West. The latter is more of an open prairie, with patches of low wheat fields.

        ### Corn field
        # The corn is tall, taller than the player. After pushing into the field a ways, the players finds themselves in an honest-to-god corn maze. The maze twists and turns. As the player runs around, some random events happen, such as seeing a fairy or goblin, or hearing voices, or encountering items, etc. At the center of the maze is a spiral staircase leading into the ground.

        ### Prairie
        # The Prairie spans a wide area, though it's not as large as the corn field. It houses the shed, outhouse, and well, but is largely aesthetic. In the field, on the ground, the player can find a shiny silver coin. There is an ominous scarecrow in the center of the field.

        ### Outhouse
        # Very minimal. This is an outhouse, it has not been used recently. There is a crescent moon cut out in the door for light. Tacked to the door (on the outside) is a note that says the following in poorly written Common:
            # ""

        ### Shed
        # This compact shed is not insulated, and has a slanted but flat board roof. There is one door on the front, facing the barn. Inside the shed are a number of tools for ploughing, hoeing, farming, watering plants, and a variety of other like-tools.

        ### Well
        # A circular stone well with a tented wooden roof and a pulley system with bucket is nearby the farmhouse in the Prairie.
