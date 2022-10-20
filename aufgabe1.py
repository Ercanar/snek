#!/usr/bin/env python3

import numpy

list = []
while True:
    a = input("Welche Zahl? ")
    if a == "OwO":
        print("UwU")
    elif a != "":
        try:
            list.append(int(a))
        except ValueError:
            print("Bitte ne Zahl, Spacko")
    else:
        break

print(sum(list))
