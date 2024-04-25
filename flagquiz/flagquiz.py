import sys

def calculate_cost(a, b):
    cost = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cost += 1
    return cost

def print_answer(a):
    line = ""
    is_first = True
    for e in a:
        if not is_first:
            line += ", "
        is_first = False
        line += e
    print(line)

def main():
    sys.stdin.readline()
    n = int(sys.stdin.readline().rstrip())
    answers = []
    for _ in range(n):
        answers.append(sys.stdin.readline().rstrip().split(", "))
    best_min_changes = 0
    costs = [0] * n
    for i in range(len(answers)):
        a = answers[i]
        max_cost = 0
        for b in answers:
            cost = calculate_cost(a, b)
            max_cost = max(cost, max_cost)
        costs[i] = max_cost
    min_cost = min(costs)
    for i in range(len(answers)):
        if min_cost == costs[i]:
            print_answer(answers[i])
    
if __name__ == "__main__":
    main()