#!/bin/python3

c = 0

def divisors(n):
    a = [n]
    for i in range(2,n):
        if n%i==0:
            a.append(i)
    return a

def check(s, n):
    part = 0
    l = len(s)
    if l%n!=0:
        return False
    for i in range(n):
        sz = l//n
        chnk = s[i*sz:i*sz+sz]
        if part==0:
            part = chnk
        elif part != chnk:
            return False
    return True

with open("../input", "r") as f:
    for r in f.read().strip().split(","):
        r = r.split("-")
        r = [int(t) for t in r]
        for id in range(r[0],r[1]+1):
            id = str(id)
            l = len(id)
            hl = int(l/2)
            if l>1:
                for div in divisors(l):
                    if check(id, div):
                        c += int(id)
                        break

print(c)
