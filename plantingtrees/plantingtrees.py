import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    seedlings = list(map(lambda t: int(t), sys.stdin.readline().rstrip().split(" ")))
    seedlings.sort(reverse=True)
    latestDay = 1
    currentDay = 1
    for seed in seedlings:
        latestDay = max(currentDay + seed, latestDay)
        currentDay += 1.
    print(latestDay + 1)
    
if __name__ == "__main__":
    main()