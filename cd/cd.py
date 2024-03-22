import sys

def do_case():
    input = sys.stdin.readline().rstrip().split()
    N = int(input[0])
    M = int(input[1])
    if N == 0 and M == 0:
        return False
    jacks = []
    for _ in range(0, N):
        n = int(sys.stdin.readline().rstrip())
        jacks.append(n)
    jills = []
    for _ in range(0, M):
        n = int(sys.stdin.readline().rstrip())
        jills.append(n)
    i, j = 0,0
    count = 0
    while i < N and j < M:
        if jacks[i] == jills[j]:
            count += 1
            i += 1
            j += 1
            continue
        if jacks[i] < jills[j]:
            i += 1
        else:
            j += 1
    print(count)
    return True

def main():
    is_running = True
    while is_running:
        is_running = do_case()
        


if __name__ == "__main__":
    main()