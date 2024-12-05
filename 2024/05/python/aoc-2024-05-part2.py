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
    wrong = 0
    for i in range(len(u)-1):
        for j in range(i+1,len(u)):
            if str(int(u[j]))+"|"+str(int(u[i]))+"\n" in rules:
                wrong = 1
                app=u[i]
                u[i]=u[j]
                u[j]=app
                j-=1
    part1 += wrong*(int(u[math.floor(len(u)/2)]))

print(part1)

