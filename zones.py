# zones.py


class Zone:

    def __init__(self, zoneID):

        self.zoneID = zoneID
        self.items = {}

        if (self.zoneID == 0):  # starting zone (road)
            print(f"zone {zoneID}")
            self.summary = "You stand just off a dirt road. The road continues North and South. There is a farm to the West. Past the farmhouse can be seen a barn, and two small buildings."
            self.description = "You are standing just off a dirt road which stretches onward for what seems like miles to the North and South. The sun hangs overhead, slowly dipping toward the horizon behind a steady farm. Several structures dot the property, including a house, a barn, and a couple ancilliary buildings. Behind you, across the road, a wide field of beans stretches far into the distance, abutting a misty thicket of wood. Tucked into the sparse grass, in the ditch just off the road, you spot a tiny hat."
            self.items.clear()
            self.items["Fancy Hat"] = {
                "quantity": 1,
                "description": "A small decorative hat, too small to wear. It is finely crafted of black silk with green embroidery.",
                "value": 5
            }
            self.options = ["Walk West toward the house", "Walk North along the road", "Walk South along the road", "Pickup the hat", "Look at your inventory"]

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
                }
            }

        elif (self.zoneID == 1):  # farmhouse
            print(f"zone {zoneID}")
            self.summary = "There is a two-story farm house"
        elif (self.zoneID == 2):  # barn
            print(f"zone {zoneID}")
            self.summary = "There is a tall barn"
        elif (self.zoneID == 3):  # prairie
            print(f"zone {zoneID}")
            self.summary = "A wide open prairie"
        elif (self.zoneID == 4):  # shed
            print(f"zone {zoneID}")
        elif (self.zoneID == 5):  # outhouse
            print(f"zone {zoneID}")
        elif (self.zoneID == 6):  # well
            print(f"zone {zoneID}")
        elif (self.zoneID == 7):  # cornfield
            print(f"zone {zoneID}")
        elif (self.zoneID == 8):  # cornmaze
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
