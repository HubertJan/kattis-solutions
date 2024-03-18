import sys
import string

def print_result(case, result):
    print(f"Case #{case}: {result}")

def convert(input):
    mapping = [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3 +  [6] * 3+ [7] * 4 + [8] * 3 + [9] * 4
    output = ""
    for c in input:
        if c == " ":
            if len(output) != 0 and output[len(output) - 1] == "0":
                output += " "
            output += "0"
            continue
        if not c.isalpha():
            continue
        index = string.ascii_lowercase.index(c)
        letters = f"{mapping[index]}"
        if len(output) != 0 and output[len(output) - 1] == letters:
            output += " "
        for i in range(index - 1, -1, -1):
            if mapping[index]  == mapping[i]:
                letters += f"{mapping[index]}"
            else:
                break
        output += f"{letters}"
    return output

def main():
    numberOfLines = int(sys.stdin.readline().rstrip())
    lines = [""] * numberOfLines
    for i in range(0, numberOfLines):
        lines[i] = sys.stdin.readline()
        print_result(i + 1, convert(lines[i]))

    
if __name__ == "__main__":
    main()