import sys
input = sys.stdin.readline

def solution(N, M , coins):
    dp = [0] * (M+1)
    dp[0] = 1

    for coin in coins:
        for j in range(coin, M+1):
            dp[j] += dp[j - coin]

    return dp[M]

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().strip().split()))
    M = int(input())
    print(solution(N, M, coins))