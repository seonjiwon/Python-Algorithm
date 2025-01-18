import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(target):
    if dp[target] != -1:
        return dp[target]

    max_time = 0
    for prev in orders[target]:
        max_time = max(max_time, solution(prev))

    dp[target] = max_time + times[target-1]

    return dp[target]


T = int(input())
for _ in range(T):
    N, K = map(int, input().strip().split())
    times = list(map(int, input().strip().split()))
    orders = [[] for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().strip().split())
        orders[Y].append(X)
    W = int(input())

    dp = [-1] * (N+1)

    print(solution(W))
