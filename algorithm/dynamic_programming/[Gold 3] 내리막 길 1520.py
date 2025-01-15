import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):

    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if MAP[x][y] > MAP[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

M, N = map(int, input().strip().split())
MAP = [list(map(int, input().strip().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]

print(dfs(0, 0))