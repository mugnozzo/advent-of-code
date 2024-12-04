#!/bin/python

def sign(num):
    return (num>0)-(num<0)

def getSafe2Lists(lineList):
    lineLists = []
    for i in range(len(lineList)):
        lineLists.append(lineList[:i]+lineList[i+1:])
    print("Safe2Lists:")
    print(lineLists)
    return lineLists

def getLineDiff(lineList):
    lineDiff = []
    for i in range(len(lineList)-1):
        lineDiff.append(lineList[i+1]-lineList[i])
    print("lineDiff: "+str(lineDiff))
    return lineDiff

def checkSafe1(lineList):
    diff = getLineDiff(lineList)
    inc = sign(diff[0])
    for i in diff:
        if sign(i)!=inc:
            print(i)
            return False
        if i==0 or abs(i)>3:
            return False
    return True

part1 = 0
count = 0
part2add = 0

with open("input","r") as file:
    for line in file:
        print("\ncount: "+str(count))
        lineList = [int(i) for i in line.split(" ")]
        print(lineList)
        print("length: "+str(len(lineList)))
        if checkSafe1(lineList):
            print("Safe1")
            part1+=1
        else:
            print("Unsafe1")
            for partList in getSafe2Lists(lineList):
                if checkSafe1(partList):
                    print("Safe2")
                    part2add+=1
                    break
                else:
                    print("Unsafe2")
        count += 1

print("\n"+str(part1))
part2 = part1 + part2add
print("\n"+str(part2))
