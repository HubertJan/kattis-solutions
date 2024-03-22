import sys


def main():
    input = sys.stdin.readline().rstrip().split()
    n = int(input[1])
    counter = 0
    hay_dict = {}
    is_dict = True
    score = 0
    while True:
        input = sys.stdin.readline().rstrip().split()
        if is_dict and len(input) == 2 and input[1].isnumeric:
            hay_dict[input[0]] = int(input[1])
            continue
        if len(input) == 1 and input[0] == ".":
            print(score)
            score = 0
            counter += 1
            if counter == n:
                break
            continue
        is_dict = False
        for word in input:
            if not word in hay_dict:
                continue
            score += hay_dict[word]
        

if __name__ == "__main__":
    main()