import sys
input = sys.stdin.readline

def solution():
    dp = [0] * (k+1)

    dp[0] = 1

    for coin in coins:
        for c in range(coin, k+1):
            dp[c] += dp[c - coin]

    # print(dp)
    return dp[k]

n, k = map(int, input().strip().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(solution())