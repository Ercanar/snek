#!/usr/bin/env python3

import socket

#list=[1,3,3,7]
#list2=["1337", "42", "4321"]

#def isEven(number):
    #return number % 2 == 0

#def doppel(para):
    #return [2*i for i in para]

#print(doppel(list))

#print([*map(lambda x: x * 2, [1,3,3,7])])

#print([*filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, range(0, 10)))])

#print([*range(1, 11)])
#print([*filter(lambda x: x%2 == 1, range(1, 101))])
#print([*filter(isEven, range(0, 100))])

#print([*map(lambda x: int(x), list2)])

#datei = open("foo", "w+")
#datei.write("Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch")
#datei.close()

#datei2 = open("git", "r")
#print(datei2.readline(3))
#print(datei2.seek(0))
#datei2.close()

#with open("foo", "r+") as datei:
    #datei.seek(1)
    #print(datei.read(7))

auto = {"wheels": 4, "doors": 5, "name": "GT"}
print(auto["doors"])
auto["doors"] = 900
print(auto["doors"])
