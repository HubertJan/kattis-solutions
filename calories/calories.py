import sys


cal_per_gram = [9, 4, 4, 4, 7]

def calculate_calories(input):
    total_non_fat_calories = 0
    total_perc_non_fat_cal = 0
    total_fat_cal = 0
    total_perc_fat_cal = 0
    for i, value in enumerate(input, start=0):
        unit = value[-1]
        num = int(value[:-1])
        if i != 0:
            match unit:
                case "g":
                    total_non_fat_calories += num * (cal_per_gram[i])
                case "C":
                    total_non_fat_calories += num
                case "%":
                    total_perc_non_fat_cal += num
        else:
            match unit:
                case "g":
                    total_fat_cal += num * (cal_per_gram[i])
                case "C":
                    total_fat_cal += num
                case "%":
                    total_perc_fat_cal += num
    if total_perc_fat_cal != 0:
        total = total_non_fat_calories   
        total += (total / (1 - (total_perc_non_fat_cal + total_perc_fat_cal) / 100)) * ((total_perc_non_fat_cal + total_perc_fat_cal)/100)
        return (total, (total_perc_fat_cal / 100) * total)
    total = total_non_fat_calories + total_fat_cal
    total += (total / (1 - (total_perc_non_fat_cal / 100)))  * (total_perc_non_fat_cal/100)
    return (total, total_fat_cal)


def main():
    total_calories = 0
    total_fat_calories = 0
    is_new_food = True
    while True:
        input = sys.stdin.readline().rstrip().split()
        if len(input) == 1:
            if is_new_food:
                break
            print(f"{round((total_fat_calories/total_calories) * 100)}%")
            is_new_food = True
            continue
        if is_new_food:
            total_calories = 0
            total_fat_calories = 0
            is_new_food = False
        t, ct = calculate_calories(input)
        total_calories += t
        total_fat_calories += ct
        
 
    
if __name__ == "__main__":
    main()