#!/bin/python

matrix=[]
part2=0
word="MAS"
checked=[]

def getX(r,c,i,j):
   return ([r+(len(word)-1)*i,c,-i,j],[r,c+(len(word)-1)*j,i,-j])

def scan(matrix,r,c,i,j):
    tempStr=""
    for n in range(len(word)):
        if r+i*n in range(len(matrix)) and c+j*n in range(len(matrix[0])):
            tempStr+=matrix[r+i*n][c+j*n]
            if not word.startswith(tempStr):
                return 0
        else:
            break
    if tempStr==word:
        checked.append([r,c,i,j])
        return 1
    return 0

with open("../input","r") as file:
    for line in file:
        matrix.append(line)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c]=="M":
            for (i,j) in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                if [r,c,i,j] not in checked:
                    if scan(matrix,r,c,i,j):
                        for arr in getX(r,c,i,j):
                            if arr not in checked:
                                part2 += scan(matrix,arr[0],arr[1],arr[2],arr[3])

print(part2)
