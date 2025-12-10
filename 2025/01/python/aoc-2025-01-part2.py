#!/bin/python3

n = 50
c = 0

with open("../input", "r") as f:
    for l in f:
        l = l.strip()
        r = int(l[1:])
        s = 1 if l[0]=="R" else -1
        for i in range(r):
            n += s
            n %= 100
            if n==0:
                c += 1

print(c)
