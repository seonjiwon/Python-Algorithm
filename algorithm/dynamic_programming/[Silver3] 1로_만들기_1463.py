import sys

def min_operations(n):
  dp = [0 for i in range(n+1)]

  for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
      dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
      dp[i] = min(dp[i], dp[i//3] + 1)

  return dp[n]


n = int(sys.stdin.readline().strip())
print(min_operations(n))
