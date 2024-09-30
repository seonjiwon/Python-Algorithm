import sys

def min_value(n, prices):
  dp = [0] + prices

  for i in range(1, n+1):
    for j in range(1, i+1):
      dp[i] = min(dp[i], dp[i-j] + prices[j-1])
  return dp[n]


n = int(sys.stdin.readline().strip())
prices = list(map(int, sys.stdin.readline().strip().split()))
print(min_value(n, prices))