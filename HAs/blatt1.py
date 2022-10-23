#!/usr/bin/env python3

#Aufgabe 1

def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2 == 1

list = [*range(1,11)]
list2 = [*filter(isOdd, range(1, 101))]
list3 = [*filter(isEven, range(0, 100))]
list4 = [*range(ord("a"), ord("z")+1)]
i = 0
a = 0

while True:
    if a < len(list):
        print(list[a])
        a += 1
    else:
        break

while i < len(list2):
    print(list2[i])
    i += 1

for i in list3:
    print(i)

for i in list4:
    print(chr(i))


#Aufgabe 2

array = [2,3,5,9,15,23,45,82,94,95,97,99]
for i in array:
    print(i)


#Aufgabe 4

satz = [*input("What shall I sort? ")]
satz.sort()
print("".join(satz))
