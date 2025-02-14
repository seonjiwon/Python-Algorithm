import sys
input = sys.stdin.readline

def solution():
    max_cost = sum(costs)
    dp = [0] * (max_cost + 1)

    for i in range(N):
        memory, cost = memories[i], costs[i]
        for c in range(max_cost, cost - 1, -1):
            dp[c] = max(dp[c], dp[c-cost] + memory)

    for i in range(max_cost + 1):
        if dp[i] >= M:
            return i


N, M = map(int, input().strip().split())
memories = list(map(int, input().strip().split()))
costs = list(map(int, input().strip().split()))
print(solution())