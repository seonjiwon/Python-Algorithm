import sys

def count_pinary_number(n):
  dp = [[0] * 2 for _ in range(n + 1)]
  dp[1] = [0, 1]

  for i in range(2, n + 1):
    for j in range(2):
      if j == 0:
        dp[i][0] += dp[i-1][0]
        dp[i][1] += dp[i-1][0]
      else:
        dp[i][0] += dp[i-1][1]
  return sum(dp[n])



n = int(sys.stdin.readline().strip())
print(count_pinary_number(n))