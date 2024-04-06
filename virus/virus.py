import sys

def find_difference(text, modified):
    while modified != "" and text != "" and modified[0] == text[0]:
        modified = modified[1:]
        text = text[1:]
    while modified != "" and text != "" and modified[-1] == text[-1]:
        modified = modified[:-1]
        text = text[:-1]
    print(len(modified))
        

def main():
    original = sys.stdin.readline().rstrip()
    infected = sys.stdin.readline().rstrip()
    
    find_difference(original, infected)
    
if __name__ == "__main__":
    main()