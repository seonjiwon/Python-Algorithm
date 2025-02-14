import sys
input = sys.stdin.readline

def solution():
    dp = [float('inf')] * (k+1)

    for coin in coins:
        if coin > k:
            continue
        dp[coin] = 1
        for c in range(coin, k+1):
            dp[c] = min(dp[c], dp[c - coin] + 1)

    return dp[k] if dp[k] != float('inf') else -1

n, k = map(int, input().strip().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
print(solution())