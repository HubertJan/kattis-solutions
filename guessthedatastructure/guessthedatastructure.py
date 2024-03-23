import sys
from heapq import heappop, heappush

def guess_data_structure(n):
    can_be_queue = True
    can_be_stack = True
    can_be_prio = True
    queue = []
    stack = []
    prio = []
    for _ in range(0, n):
        input = sys.stdin.readline().rstrip().split()
        operation = int(input[0])
        value = int(input[1])
        match operation:
            case 2:
                if len(stack) == 0 or stack.pop() != value:
                    can_be_stack = False
                if len(queue) == 0 or queue.pop(0) != value:
                    can_be_queue = False
                if len(prio) == 0 or -heappop(prio) != value:
                    can_be_prio = False
            case 1:
                stack.append(value)
                queue.append(value)
                heappush(prio, -value)
    
    if [can_be_stack, can_be_queue, can_be_prio].count(True) > 1:
        return "not sure"
    if can_be_queue:
        return "queue"
    if can_be_stack:
        return "stack"
    if can_be_prio:
        return "priority queue"
    return "impossible"

def main():
    while True:
        input = sys.stdin.readline().rstrip().split()
        if len(input) == 0:
            break
        print(guess_data_structure(int(input[0])))

        

if __name__ == "__main__":
    main()