#!/usr/bin/python

# Slither v0.1

# --- Brainstorming goals for this project --- #

    ### Slither can be just about anything, and in fact it can be multiple things. I want to be able to use it for playing around and experimenting with Python in particular. As such, I should create an initial program idea.

    ### A Game
    # My first idea is to create a small graphical game, such as worm / snake, because I've always wanted to do something that like, and never actually done it. Plus it could be more interesting than trying to make, say, a database.

    ### Bloodborne
    # One possible option would be to recreate everything about Javaborne in Python, in other words, basically abandon the Java version and start over in this language. The problem is, while I don't necessarily like Java, the whole point of building that game is to learn Java. So I will probably not do this. I don't want to ruin the steam on that project either.

    # Zorklike
    # However, another text based adventure game - and even one with a graphical component would be pretty interesting. I think I'm going to do this.


import sys

def printArgs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))


def doSomething():
    print("I did something!");

if __name__ == "__main__":
    print("Slither! - A Zorklike Game (WIP)");

    # printArgs()
    # doSomething()

    # Zorklike (name pending)

    ### Scope:
    # To create a text based adventure game that is contained, and makes use of graphical features while rendering the graphics using ASCII text - just not in a terminal.

    ### Objectives:
    # - Learn to render a window
    # - Learn to output text to that window
    # - Create a small fantasy world
    # - Construct elements and objects for playing the Game
    # - Develop or steal an input method for text based input
    # - Have fun

    ### World / Story creation
    # I've always been partial to high fantasy, sword and sorcery style, with grand adventures. But for this I'd like to start small at least; Zork was one of my favorite text-based adventure games, and I think it provides some decent inspiration. The world felt somewhat large, but also simultaneously condensed and approachable. The house at the beginning always served as a good introduction to the mechanics - it had items, it had some puzzles for getting around / opening the trap door, and it even had a grue in the dark attic.

    # Start out the game on a farm. The farm has a barn filled with hay, other barn stuff and the remnants of animal denizens (no animals, at least not alive, maybe a stray cat.) The farm has two fields, one dense corn, one open grass and wheat with a scarecrow. The corn breaks into a small maze, with something at the middle. The farm also has a farmhouse, two floors and a cellar. There is a tool shed. Also there is a well. The farm is surrounded on two sides by thick woods, and on one side by the corn rows which stretch out several acres and butt up against more woods. The fourth side (East) is an open yard facing an old dirt road (thinking of my dad's house somewhat).

    # The goal of this area is to introduce mechanics, provide light gear, and get the player ready to adventure beyond. Perhaps the middle of the corn maze opens up into a fae world, revealing a staircase which stretches deep underground...

        # FARMHOUSE:
        # The central building on the land, and the most prominent. This is a drag grey brown house built long ago, with thatched roofing. It is made mostly of wood and logs, with an almost log cabin feel to the exterior. The interior is dark, but during the day there is plenty of light from outside to see.

            ### Main floor
            # Entryway / Porch
            # Kitchen / Dining Room
            # Living Room / Great Room
            # Stairs leading up to second floor
            # Fireplace
