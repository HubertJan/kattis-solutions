import sys



def always_up_policy(prefer):
    return "U"

def always_down_policy(prefer):
    return "D"

def prefer_policy(prefer):
    return prefer

def main():
    input = sys.stdin.readline().rstrip()
    adjst = 0
    currentC = input[0]
    policies = [always_up_policy, always_down_policy, prefer_policy]
    adjstPerPolicy = []
    for policy in policies:
        adjst = 0
        currentC = input[0]
        for i in range(1, len(input)):
            c = input[i]
            if currentC != c:
                adjst += 1
            p = policy(c)
            if p != c:
                adjst += 1
            currentC = p
        adjstPerPolicy.append(adjst)
    for c in adjstPerPolicy:
        print(c)
    
if __name__ == "__main__":
    main()