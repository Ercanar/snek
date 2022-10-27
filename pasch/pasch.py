#!/usr/bin/env python3

import numpy
import random as ran

DICE_SIZE = 6
THROW_COUNT = 3
SEL_COUNT = 5
TURN_COUNT = 15

cube = range(1, DICE_SIZE + 1)

# TODO: rule function logic:
# wurf -> zahl | return None

zettel = {
    "1en": (0, None),
    "2en": (0, None),
    "3en": (0, None),
    "4en": (0, None),
    "5en": (0, None),
    "6en": (0, None),
    "1paar": (0, None),
    "2paar": (0, None),
    "3gl": (0, None),
    "4gl": (0, None),
    "fully": (0, None),
    "kl.str": (0, None),
    "gr.str": (0, None),
    "pasch": (0, None),
    "chance": (0, None),
}

def printWurf(wurf):
    for w in wurf:
        print(w, "", end="")
    print()

# TODO: make fancy uwu
def printZettel(zettel):
    print(zettel)

def runTurn():
    wurf = []
    tempwurf = []

    for throwcount in range(THROW_COUNT):
        tempwurf = [ran.choice(cube) for _ in range(SEL_COUNT - len(wurf))]
        tempwurf = list(map(lambda x: "[31;1m" + str(x) + "[m", wurf)) + list(map(lambda x: str(x), tempwurf))
        printWurf(tempwurf)

        if throwcount < THROW_COUNT - 1:
            b = input("Welchen behalten? ").strip()
            if len(b) > 0:
                wurf = [tempwurf[i] for i in map(lambda x: int(x) - 1, b.split(" "))]
            else:
                wurf = []
        else:
            wurf = list(map(lambda x: int(x
                .replace("[31;1m", "")
                .replace("[m", "")
            ), tempwurf))

        if len(wurf) >= SEL_COUNT or throwcount >= THROW_COUNT:
            break

    printZettel(zettel)

    # TODO: check valid field name
    # TODO: invoke rule function
    zettel[input("welches Feld? ")] = sum(wurf)
    printZettel(zettel)

for turn in range(TURN_COUNT):
    runTurn()
