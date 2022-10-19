#!/usr/bin/env python3

list = [1, 2, 3]
print(len(list))

for i in list:
    print(i)

list.append(5)
list.insert(1, 6)
list.insert(1000, 4)
list.pop(0)
list.remove(3)
print(list)

list2 = range(13, 42)
print(len(list2))
#print(list2)

for i in list2:
    print(i)

while list2[2] == 14:
    list2[2] += 1

#for i in list2:
#    print(i)

list3 = [*list2]

while list3[1] == 14:
    list3[1] += 1

#print(list3)

list4 = list + list3
print(list4)

print("llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"[3])

a = "abc"
a += "def"
print(a)
