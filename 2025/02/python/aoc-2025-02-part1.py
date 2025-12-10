#!/bin/python3

c = 0

with open("../input", "r") as f:
    for r in f.read().strip().split(","):
        r = r.split("-")
        r = [int(t) for t in r]
        print(r)
        for id in range(r[0],r[1]+1):
            id = str(id)
            l = len(id)
            hl = int(l/2)
            if l%2==0:
                if id[:hl]==id[hl:]:
                    print(id)
                    print(id[:hl])
                    print(id[hl:])
                    print()
                    c += int(id)

print(c)
