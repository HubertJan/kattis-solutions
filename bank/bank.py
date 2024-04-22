from math import sin, sqrt
from heapq import heappush, heappop
import sys

    
def main():
    data = sys.stdin.readline().rstrip().split(" ")
    n, t = int(data[0]), int(data[1])
    people = []
    max_t = 0
    for _ in range(n):
        data = sys.stdin.readline().rstrip().split(" ")
        c, t = int(data[0]), int(data[1])
        max_t = max(t, max_t)
        people.append([c, t])
    
    people.sort(key=lambda p: p[1], reverse=True)
    possible = []
    total = 0
    for i in reversed(range(max_t + 1)):
        while len(people) != 0 and people[0][1] >= i:
            p = people.pop(0)
            heappush(possible, -p[0])
        if len(possible) == 0:
            continue
        total += -heappop(possible)
    print(total)
if __name__ == "__main__":
    main()