import sys

def extract_players(game):
    return [int(game[0]) - 1, int(game[2]) - 1]

def who_wins(game):
    a = game[1]
    b = game[3]
    if a == b:
        return 0
    match a:
        case "rock":
            match b:
                case "paper":
                    return 2
                case "scissors":
                    return 1
        case "scissors":
            match b:
                case "rock":
                    return 2
                case "paper":
                    return 1
        case "paper":
            match b:
                case "scissors":
                    return 2
                case "rock":
                    return 1

def main():
    input = sys.stdin.readline().rstrip().split()
    if len(input) == 1:
        return
    while True:
        n = int(input[0])
        k = int(input[1])
        gamesInTotal = (k * n * (n-1))/2
        streak = []
        for _ in range(0, n):
            streak.append([0,0,0])
        while True:
            input = sys.stdin.readline().rstrip().split()
            if len(input) != 4:
                break
            game = input
            players = extract_players(game)
            streak[players[0]][2] += 1
            streak[players[1]][2] += 1
            match who_wins(game):
                case 1:
                    streak[players[0]][0] += 1
                    streak[players[1]][1] += 1
                case 2:
                    streak[players[0]][1] += 1
                    streak[players[1]][0] += 1
        for i in range(0, n):
            total = streak[i][2]  
            if streak[i][0] + streak[i][1] != 0:
                rate = streak[i][0]/(streak[i][0] + streak[i][1])
            else:
                print("-")
                continue
            print("%.3f" % rate)
        if len(input) == 1:
            break
        print("")
                    
if __name__ == "__main__":
    main()