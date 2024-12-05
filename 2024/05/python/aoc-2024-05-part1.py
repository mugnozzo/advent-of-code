#!/bin/python

import math

part1=0
rules=[]
updates=[]

with open("../input","r") as file:
    for line in file:
        if "|" in line:
            rules.append(line)
        elif "," in line:
            updates.append(line.split(","))

for u in updates:
    correct = 1
    for i in range(len(u)-1):
        for j in range(i+1,len(u)):
            if str(int(u[j]))+"|"+str(int(u[i]))+"\n" in rules:
                correct = 0
                break
        if correct == 0:
            break
    part1 += correct*(int(u[math.floor(len(u)/2)]))

print(part1)

