#!/usr/bin/env python3

# konstanten
pi = 3.1414
adminaccount = "root"

# Diese Funktion fragt den Nutzer nach seinem Namen
# und bittet ihn, ehrlich zu sein
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
