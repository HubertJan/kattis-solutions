import sys
import re

def read_text(n):
    word_counter = {}
    matches = []
    while True:
        data = sys.stdin.readline().rstrip()
        if data == "EndOfText":
            break
        words = re.sub(r'[^a-zA-Z]+', ' ',data).split(" ")
        for w in words:
            w = w.lower()
            if w == "":
                continue
            if not w in word_counter: 
                word_counter[w] = 0
            word_counter[w] += 1
            if word_counter[w] == n:
                matches.append(w)
    return list(filter(lambda w: word_counter[w] <= n, matches))

def main():
    is_first = True
    while True:
        data = sys.stdin.readline().rstrip()
        if data == "":
            break
        if not is_first:
            print("")
        n = int(data)
        results = read_text(n)
        if len(results) == 0:
            print("There is no such word.")
        else:
            for w in sorted(results):
                print(w)
        is_first = False
        
    
    
if __name__ == "__main__":
    main()