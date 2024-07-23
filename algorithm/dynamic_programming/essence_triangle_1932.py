import sys


def max_root(n, triangle):
  dp = [[0] * i for i in range(1, n+1)]

  dp[0][0] = triangle[0][0]

  if n > 1:
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]

  for i in range(2, n):
    for j in range(i + 1):
      if j == 0:
        dp[i][j] = dp[i-1][j] + triangle[i][j]
      elif j == i:
        dp[i][j] = dp[i-1][j-1] + triangle[i][j]
      else:
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

  return max(dp[n-1])


n = int(sys.stdin.readline().strip())
triangle = []
for i in range(n):
  triangle.append(list(map(int, sys.stdin.readline().strip().split())))
print(max_root(n, triangle))