#!/usr/bin/env python3

# konstanten
pi = 3.1414
adminaccount = "root"

def getusername():
    print("Willkommen zum krassen system")
    print("lügen verboten")
    return input("Was ist dein Name")

def rechte(name):
    if name == adminaccount:
        print("alle", pi)
    else:
        print("nun")

rechte(getusername())
