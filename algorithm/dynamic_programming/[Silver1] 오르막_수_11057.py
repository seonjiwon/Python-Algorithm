import sys


def ascending_number(n):
  MOD = 10007
  dp = [[0]*10 for _ in range(n+1)]

  for i in range(10):
    dp[1][i] = 1

  for i in range(2, n+1):
    for j in range(10):
      dp[i][j] = sum(dp[i-1][j::]) % MOD
  return sum(dp[n]) % MOD



n = int(sys.stdin.readline().strip())
print(ascending_number(n))