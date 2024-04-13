import sys

def track_friendships():
    n = int(sys.stdin.readline().rstrip())
    parents = {}
    total_friends = {}
    def find(x):
        if not x in parents.keys():
            parents[x] = x
            total_friends[x] = 1
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    def union(x,y):
        parents[find(y)] = find(x)
    def friends(x):
        return total_friends[find(x)]
    
    for _ in range(0, n):
        names = sys.stdin.readline().rstrip().split(" ")
        a, b = names[0], names[1]
        if find(a) != find(b):
            total_friends[find(a)] += total_friends[find(b)]
            union(a, b)
        print(friends(a))

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(0, n):
        track_friendships()

if __name__ == "__main__":
    main()