import sys

def solve_case():
    is_correct = True
    text = input()
    n = int(text)
    tree = [False] * 10
    for _ in range(0, n):
        current = tree
        total_num = input()
        for c in total_num[:-1]:
            num = int(c)
            if current[num] == True:
                is_correct = False
                break
            if current[num] == False:
                current[num] = [False] * 10
            current = current[num]
        if not is_correct:
            break
        num = int(total_num[-1])
        if current[num] != False:
            is_correct = False
            break
        current[num] = True
    print("YES" if is_correct else "NO")

def main():
    t = int(sys.stdin.readline())
    for _ in range(0, t):
        solve_case()
    
if __name__ == "__main__":
    main()