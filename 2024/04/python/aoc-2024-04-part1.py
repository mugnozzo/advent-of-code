#!/bin/python

matrix=[]
part1=0
word="XMAS"

def scan(matrix,r,c,i,j):
    tempStr=""
    for n in range(len(word)):
        if r+i*n in range(len(matrix)) and c+j*n in range(len(matrix[0])):
            tempStr+=matrix[r+i*n][c+j*n]
            if not word.startswith(tempStr):
                return 0
        else:
            return 0
    if tempStr==word:
        return 1
    return 0

with open("../input","r") as file:
    for line in file:
        matrix.append(line)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c]=="X":
            for (i,j) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                part1+=scan(matrix,r,c,i,j)

print(part1)
