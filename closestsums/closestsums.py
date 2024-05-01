import sys

def find_closest(numbers, target):
    l, r = 0, len(numbers) - 1
    current_best = (sum(numbers) + target * 2) 
    while l != r:
        current = numbers[l] + numbers[r]
        if abs(target - current) < abs(target - current_best):
            current_best = current
        if target == current:
            return target
        if current > target:
            r -= 1
        if current < target:
            l += 1
    return current_best
            

def main():
    i = 1
    while True:
        data = sys.stdin.readline().rstrip()
        if data == "":
            break
        n = int(data)
        print(f"Case {i}:")
        numbers = []
        for _ in range(n):
            numbers.append(int(sys.stdin.readline().rstrip()))
        numbers.sort()
        m = int(sys.stdin.readline().rstrip())
        targets = []
        for _ in range(m):
            t = int(sys.stdin.readline().rstrip())
            closest = find_closest(numbers, t)
            print(f"Closest sum to {t} is {closest}.")
        i += 1
        

    
if __name__ == "__main__":
    main()