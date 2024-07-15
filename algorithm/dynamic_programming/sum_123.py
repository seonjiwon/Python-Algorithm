import sys

def count(n):
  dp = [0, 1, 2, 4]

  for i in range(4, n+1):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])
  return dp[n]

hei = int(sys.stdin.readline().strip())
for i in range(hei):
  n = int(sys.stdin.readline().strip())
  print(count(n))