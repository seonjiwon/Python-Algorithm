import sys

def divide_sum(n, k):
  MOD = 1000000000
  dp = [[0] *(k+1) for _ in range(n+1)]

  for i in range(1, k+1):
    dp[1][i] = i

  for i in range(2, n+1):
    dp[i][1] = 1
    for j in range(2, k+1):
      dp[i][j] = dp[i][j-1] + dp[i-1][j]
  print(dp[n][k] % MOD)

n, k = map(int, sys.stdin.readline().strip().split())
divide_sum(n, k)
