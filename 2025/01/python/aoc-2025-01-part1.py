#!/bin/python3

n = 50
c = 0

with open("../input", "r") as f:
    for l in f:
        l = l.strip()
        op = 1 if l[0]=="R" else -1
        n = (n + int(l[1:]) * op) % 100
        if n==0:
            c += 1

print(c)
