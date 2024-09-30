import sys

def max_score(n, sk):
  dp = [[0] * n for _ in range(2)]

  dp[0][0] = sk[0][0]
  dp[1][0] = sk[1][0]

  if n >= 2:
    dp[0][1] = sk[0][1] + sk[1][0]
    dp[1][1] = sk[0][0] + sk[1][1]

  for i in range(2, n):
    dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sk[0][i]
    dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sk[1][i]
  return max(dp[0][n-1], dp[1][n-1])

t = int(sys.stdin.readline().strip())
for i in range(t):
  sticker = []
  n = int(sys.stdin.readline().strip())
  sticker.append(list(map(int, sys.stdin.readline().strip().split())))
  sticker.append(list(map(int, sys.stdin.readline().strip().split())))
  print(max_score(n, sticker))
