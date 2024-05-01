import sys
from itertools import chain, combinations

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

def calculate_dif(set):
    sum = 0
    prod = 1
    for s in set:
        sum += s[1]
        prod *= s[0]
    return abs(sum - prod)


def main():
    n = int(sys.stdin.readline())
    ingredients = [None] * n
    for i in range(n):
        data = sys.stdin.readline().rstrip().split(" ")
        ingredients[i] = [int(data[0]), int(data[1])]
    best_min = calculate_dif(ingredients)
    for subset in all_subsets(ingredients):
        if len(subset) == 0:
            continue
        best_min = min(best_min, calculate_dif(subset))
    print(best_min)
    
if __name__ == "__main__":
    main()