from math import sqrt
import sys

def read_coordinates():
    data = sys.stdin.readline().rstrip().split(" ")
    return (int(data[0]), int(data[1]))

def check_route():
    n = int(sys.stdin.readline().rstrip())
    shops = []
    home = read_coordinates()
    for _ in range(n):
        shops.append(read_coordinates())
    target = read_coordinates()
    nodes = [home] + [s for s in shops] + [target]
    parent = [i for i in range(2 + n)]
    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]
    
    def union(u, v):
        parent[find(v)] = find(u)
        
    def calulateDistance(uPos, vPos):
        return abs(uPos[0] - vPos[0]) + abs(uPos[1] - vPos[1])

    for u in range(n + 2):
        for v in range(n + 2):
            if calulateDistance(nodes[u], nodes[v]) <= 1000 and find(u) != find(v):
                union(u, v)
    
    if find(0) == find(n + 2 - 1):
        return "happy"
    return "sad"

def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(0, n):
        print(check_route())

if __name__ == "__main__":
    main()