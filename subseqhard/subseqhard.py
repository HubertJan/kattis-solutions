import sys

def count_subsequence():
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print(0)
    numbers = list(map(lambda x: int(x) , sys.stdin.readline().rstrip().split(" ")))
    sums = {} 
    counter = 0
    for num in numbers:
        other_sums = {}
        for k, v in sums.items():
            other_sums[k + num] = v
        sums = other_sums
        if not num in sums:
            sums[num] = 0
        sums[num] += 1
        if 47 in sums:
            counter += sums[47]
    print(counter)
    
def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(0, n):
        sys.stdin.readline()
        count_subsequence()
    
if __name__ == "__main__":
    main()