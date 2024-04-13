from math import sin, sqrt
import sys

def solve_watering(data):
    n, l, w = int(data[0]), int(data[1]), int(data[2])
    springlers = []
    for _ in range(n):
        data = sys.stdin.readline().rstrip().split(" ")
        x, r = int(data[0]), int(data[1])
        if r < w/2:
            continue
        radius_width = sqrt(r*r -(w/2)**2)
        springlers.append((x - radius_width, x + radius_width))
    springlers.sort(key=lambda x: x[0])
    highest = 0
    lower = 0
    count = 0
    i = 0
    while i != len(springlers) and highest != l:
        i += 1
        if springlers[i - 1][1] > highest and springlers[i - 1][0] <= highest:
            highest = min(springlers[i - 1][1], l)
            while i != len(springlers) and springlers[i][0] <= lower:
                highest = min(max(springlers[i][1], highest), l)
                i += 1
            lower = highest
            count += 1
    if highest < l:
        count = -1
    print(count)
    
    
def main():
    data = sys.stdin.readline().rstrip()
    while data != "":
        solve_watering(data.split(" "))
        data = sys.stdin.readline().rstrip()
    
if __name__ == "__main__":
    main()