import sys


def isHorizontalClear(data, startY):
    foundQ = False
    for x in range(0, len(data[0])):
        found = data[startY][x]
        if found and foundQ:
            return False
        if found:
            foundQ = True
    return True

def isVerticalClear(data, startX):
    foundQ = False
    for y in range(0, len(data)):
        found = data[y][startX]
        if found and foundQ:
            return False
        if found:
            foundQ = True
    return True

def isCrossRightClear(data, startX, startY):
    foundQ = False
    for i in range(0, len(data)):
        x = startX + i
        y = startY + i
        if x >= len(data[0]) or y >= len(data):
            return True
        found = data[y][x]
        if found and foundQ:
            return False
        if found:
            foundQ = True
    return True

def isCrossLeftClear( data, startX, startY):
    foundQ = False
    for i in range(0, len(data)):
        x = startX - i
        y = startY + i
        if x < 0 or y >= len(data):
            return True
        found = data[y][x]
        if found and foundQ:
            return False
        if found:
            foundQ = True
    return True

rows = []
for i in range(8):
    rows.append(sys.stdin.readline().rstrip())
    
data = [[c == '*' for c in line] for line in rows]

def isQueenCountFine(data):
    count = 0
    if len(data) != 8:
            return False
    for y in range(0, len(data)):
        if len(data[y]) != 8:
            return False
        for x in range(0, len(data[y])):
            if data[y][x] == True:
                count +=1
            if count > 8:   
                return False
    return count == 8

def isBoardFine(data):
    for x in range(0, len(data[0])):
        for y in range(0, len(data)):
            if not isVerticalClear(data, x): return False
            if not isCrossRightClear(data, x, y): return False
            if not isCrossLeftClear(data, x, y): return False
            if not isHorizontalClear(data, y): return False
    return True


print("valid" if isQueenCountFine(data) and isBoardFine(data) else "invalid")