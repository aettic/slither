#!/usr/bin/python

# Slither v0.1

# Brainstorming goals for this project:
    # Slither can be just about anything, and in fact it can be multiple things.


import sys

def printArgs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))


def doSomething():
    print("I did something!");

if __name__ == "__main__":
    print("Slither!");

    # printArgs()
    doSomething()
