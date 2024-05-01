import math
import sys

def prime_factors(n, min_p):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if min_p <= i:
                factors.append(i)
    if n > 1:
        if min_p <= n:
            factors.append(n)
    return factors

def main():
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        data = sys.stdin.readline().rstrip().split(" ")
        a, b, p = int(data[0]), int(data[1]), int(data[2])
        
        offset = int(min(a, p))
        sets = [i for i in range(min(a, p), b + 1)]
        
        def find(x):
            if sets[x - offset] != x:
                sets[x - offset] = find(sets[x - offset])
            return sets[x - offset]
        
        def union(x, y):
            found = find(sets[x - offset])
            other = find(sets[y - offset])
            sets[other - offset] = found
        
        for num in range(a, b + 1):
            factors = prime_factors(num, p)
            for f in factors:
                union(num, f)
        s = set()
        for num in sets[(a - offset):(b - offset) + 1]:
            s.add(find(num))
        
        print(f"Case #{i + 1}: {len(s)}")

    
if __name__ == "__main__":
    main()