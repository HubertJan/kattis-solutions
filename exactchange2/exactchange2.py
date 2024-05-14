from math import sin, sqrt, gcd
import sys

import math

def solve_coins():
    total_price = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())
    coins = [0] * n
    for i in range(n):
        coins[i] = int(sys.stdin.readline().rstrip())
    coins.sort()
    total_price = int(total_price)
    dp = [10001] * 19999
    dp[0] = 0
    for coin in coins:
        price = total_price - 1
        while price  >= 0:
            if dp [price] == 10001:
                price -= 1
                continue
            if dp[price + coin] > dp[price] + 1:
                dp[price + coin] = dp[price] + 1
            price -= 1
    i = total_price
    while True:
        if dp[i] != 10001:
            break
        i += 1

    return (i, dp[i])
    
def main():
    n = int(sys.stdin.readline().rstrip())
    for _ in range(n):
        result = solve_coins()
        print(f"{result[0]} {result[1]}")
    
if __name__ == "__main__":
    main()