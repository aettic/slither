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
import player

def printArgs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))


def doSomething():
    print("I did something!");

if __name__ == "__main__":
    # print("Slither! - A Zorklike Game (WIP)");

    print("Testing")

    newPlayer = player.Player()
    newPlayer.characterCreation()


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
