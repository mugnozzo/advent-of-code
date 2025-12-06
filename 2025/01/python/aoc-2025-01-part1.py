#!/bin/python3

n = 50
c = 0

with open("../input", "r") as f:
    for l in f:
        l = l.strip()
        r = int(l[1:])
        if l[0]=="R":
            r *= -1
        n = (n + r) % 100
        if n==0:
            c += 1
        print(f"{l} - {r} - {n} - {c}")

print(c)
