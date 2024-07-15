import sys

def stair_number_count(n):
  dp = [[0] * 10 for _ in range(n+1)]
  dp[1] = [0,1,1,1,1,1,1,1,1,1]

  for i in range(2, n+1):
    for j in range(10):
      if j == 0:
        dp[i][j] = dp[i-1][j+1]
      elif j == 9:
        dp[i][j] = dp[i-1][j-1]
      else:
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
  return sum(dp[n]) % 1000000000

n = int(sys.stdin.readline().strip())
print(stair_number_count(n))