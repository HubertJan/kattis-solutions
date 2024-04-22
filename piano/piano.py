from math import sin, sqrt
from heapq import heappush, heappop
import sys

def evaluate_plan():
    data = sys.stdin.readline().rstrip().split(" ")
    m, p = int(data[0]), int(data[1])
    max_day = 0
    days = [[] for _ in range(101)]
    
    for _ in range(m):
        data = sys.stdin.readline().rstrip().split(" ")
        fromDay, untilDay = int(data[0]), int(data[1])
        days[untilDay].append(fromDay)
        max_day = max(max_day, untilDay)
    
    isPossible = True
    perDay = int(p/2)
    isWorkingAtWeekends = False
    while True:
        if not isPossible and not isWorkingAtWeekends:
            isPossible = True
            isWorkingAtWeekends = True
        if not isPossible and isWorkingAtWeekends:
            break
        q = []
        for day in reversed(range(1, max_day + 1)):
            for order in days[day]:
                heappush(q, -order)
            if not isWorkingAtWeekends and ((day % 7) % 6 == 0 or day % 7 == 0):
                continue
            for _ in range(perDay):
                if len(q) == 0:
                    break
                order = -heappop(q)
                if order > day:
                    isPossible = False
                    break
        if len(q) != 0:
            isPossible = False
        if isPossible:
            break
    if isPossible and isWorkingAtWeekends:
        print("weekend work")
    elif isPossible:
        print("fine")
    else:
        print("serious trouble")

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        evaluate_plan()
    
if __name__ == "__main__":
    main()