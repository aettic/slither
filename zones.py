# zones.py

class Zone:

    def __init__(self, zoneID, pc):

        self.zoneID = zoneID
        self.items = {}

        if (self.zoneID == 0):  # starting zone (road)
            self.summary = "You stand just off a dirt road. The road continues North and South. There is a farm to the West. Past the farmhouse can be seen a barn, and two small buildings."
            self.description = "You are standing just off a dirt road which stretches onward for what seems like miles to the North and South. The sun hangs overhead, slowly dipping toward the horizon behind a steady farm. Several structures dot the property, including a house, a barn, and a couple ancilliary buildings. Behind you, across the road, a wide field of beans stretches far into the distance, abutting a misty thicket of wood. Tucked into the sparse grass, in the ditch just off the road, you spot a tiny hat."
            self.items.clear()
            self.items["Fancy Hat"] = {
                "quantity": 1,
                "description": "A small decorative hat, too small to wear. It is finely crafted of black silk with green embroidery.",
                "value": 5
            }
            if(pc.globalStatus["Fancy Hat taken"] == False):
                self.options = ["Walk West toward the house", "Walk North along the road", "Walk South along the road", "Pickup the hat", "Look at your inventory", "Look around the area", "Save the game"]

                self.selection = {
                    1: {
                        "do": "You walk toward the house",
                        "moveTo": 1,
                    },
                    2: {
                        "do": "You walk up the road, but decide to head back",
                    },
                    3: {
                        "do": "You walk down the road, but decide to head back",
                    },
                    4: {
                        "do": "You pick up the small hat",
                        "takeItem": "Fancy Hat"
                    },
                    5: {
                        "pack": "You look into your backpack"
                    },
                    6: {
                        "do": self.description
                    },
                    7: {
                        "save": "saveGame"
                    }
                }
            elif(pc.globalStatus["Fancy Hat taken"] == True):
                self.options = ["Walk West toward the house", "Walk North along the road", "Walk South along the road", "Look at your inventory", "Look around the area", "Save the game"]

                self.selection = {
                    1: {
                        "do": "You walk toward the house",
                        "moveTo": 1,
                    },
                    2: {
                        "do": "You walk up the road, but decide to head back",
                    },
                    3: {
                        "do": "You walk down the road, but decide to head back",
                    },
                    4: {
                        "pack": "You look into your backpack"
                    },
                    5: {
                        "do": self.description
                    },
                    6: {
                        "save": "saveGame"
                    }
                }

        elif (self.zoneID == 1):  # farmhouse front entrance
            self.summary = "Behind the house in an open prairie are a barn, a shed, an outhouse, and a well. To the North, the property unfolds into a corn field."
            self.description = "A looming log farmhouse, nearly a two-story cabin, complete with thatched gable roofing, stands firm in front of you, here in the center of this farm property. The sun threatens to set behind it, inching closer every moment. Behind the house, a smattering of structures dot the property: A stone well close by; a farm tool shed, a cramped looking outhouse, and a large barn which dwarfs the house itself, even from so far away. The gently rolling landscape surrounding the house is comprised of wheats and grasses, with a couple small plots of beans, cabbages, and other low crops. In the distance a scarecrow watches plaintively over the crops. The Northern edge of the property fades into a dense and tall corn field. The whole property is surrounded on the outskirts by darkened and misty woods."
            self.items.clear()
            self.options = ["Enter the house", "Walk into the backyard", "Travel to the corn field", "Return to the road", "Look at your inventory", "Look around the area", "Save the game"]

            self.selection = {
                1: {
                    "do": "You walk inside the farmhouse through the porch door",
                    "moveTo": 2
                },
                2: {
                    "do": "You skirt the side of the house and walk into the prairie behind the house",
                    "moveTo": 3
                },
                3: {
                    "do": "You depart the house and head North, toward the wall of green corn stalks",
                    "moveTo": 8
                },
                4: {
                    "do": "You decide to head back toward the dirt road.",
                    "moveTo": 0
                },
                5: {
                    "pack": "You look into your backpack, remembering your note"
                },
                6: {
                    "do": self.description
                },
                7: {
                    "save": "saveGame"
                }
            }

        elif (self.zoneID == 2):  # inside farmhouse - kitchen
            self.summary = "The house is dark. You stand in the kitchen, which also serves as a dining room. There is a closet to your right, a great room behind a wall straight ahead, and a staircase at the far back of this floor leading up."
            self.description = "Only the dim evening light spills in from the windows on the West side of the wall. It appears that this place was left in a hurry. The tell-tale signs of a struggle can be seen about the room."
            self.items.clear()

            if(pc.globalStatus["Kitchen examined"] == False):
                self.options = ["Into the sitting room", "Open the closet", "Head back outside", "Look around the area", "Save the game"]

                self.selection = {
                    1: {
                        "do": "You traverse the creaking floor and head into the sitting room",
                        "moveTo": 4
                    },
                    2: {
                        "do": "You walk over to the closet door and pull it open",
                        "moveTo": 3
                    },
                    3: {
                        "do": "You step back outside the house",
                        "moveTo": 1
                    },
                    4: {
                        "do": self.description,
                        "examine": "Kitchen"
                    },
                    5: {
                        "save": "saveGame"
                    }
                }
            else:
                self.options = ["Into the sitting room", "Open the closet", "Head back outside", "Examine the signs of struggle", "Look around the area", "Save the game"]

                self.selection = {
                    1: {
                        "do": "You traverse the creaking floor and head into the sitting room",
                        "moveTo": 4
                    },
                    2: {
                        "do": "You walk over to the closet door and pull it open",
                        "moveTo": 3
                    },
                    3: {
                        "do": "You step back outside the house",
                        "moveTo": 1
                    },
                    4: {
                        "do": "You look around the room, examining the chaos and bedlam. Silverware and dishes lie scattered haphazardly. A tea kettle is overturned on the floor, a small puddle of brown tea gathered around it. It is no longer warm. A fight happened here. Is Alys okay?"
                    },
                    5: {
                        "do": self.description
                    },
                    6: {
                        "save": "saveGame"
                    }
                }


        elif (self.zoneID == 3):  # farmhouseCloset1
            print(f"zone {zoneID}")
            self.summary = "A wide open prairie"
        elif (self.zoneID == 4):  # farmhouseSittingRoom
            print(f"zone {zoneID}")
        elif (self.zoneID == 5):  # outhouse
            print(f"zone {zoneID}")
        elif (self.zoneID == 6):  # well
            print(f"zone {zoneID}")
        elif (self.zoneID == 7):  # barn entrance
            print(f"zone {zoneID}")
        elif (self.zoneID == 8):  # cornfield
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
