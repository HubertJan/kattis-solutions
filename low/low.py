import sys

def is_possible(delta, n, k, numbers):
    numOfMachines = 0
    batteryIndex = 0
    while numOfMachines < n:
        if batteryIndex > numOfMachines * 2 * k:
            return False
        if numbers[batteryIndex + 1] - numbers[batteryIndex] <= delta:
            numOfMachines += 1
            batteryIndex += 1
        batteryIndex += 1
    return True
    

def main():
    data = sys.stdin.readline().rstrip().split(" ")
    n, k = int(data[0]), int(data[1])
    data =sys.stdin.readline().rstrip().split(" ")
    numbers = sorted([int(x) for x in data])
    max_num = numbers[-1]
    l, r = 0, max_num
    while l < r:
        mid = (l + r) / 2
        if is_possible(mid, n, k, numbers):
            r = mid
        else:
            l = mid + 1
    print(int(l))
    
if __name__ == "__main__":
    main()