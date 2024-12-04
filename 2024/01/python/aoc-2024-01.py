#!/bin/python

list1=[]
list2=[]

with open("../input","r") as file:
    for line in file:
        print(line.split(" "))
        list1.append(int(line.split(" ")[0]))
        list2.append(int(line.split(" ")[-1]))

part1=0
part2=0
list1.sort()
list2.sort()
for i in range(len(list1)):
    part1+=abs(list1[i]-list2[i])
    print(str(list1[i])+" "+str(list2[i]))
    part2+=list1[i]*list2.count(list1[i])

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
