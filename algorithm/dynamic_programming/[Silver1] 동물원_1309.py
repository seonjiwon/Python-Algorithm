import sys

def count(n):
  MOD = 9901
  dp = [[0]*3 for _ in range(n+1)]
  dp[1][0] = dp[1][1] = dp[1][2] = 1
  for i in range(2, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
  return sum(dp[n]) % MOD

n = int(sys.stdin.readline().strip())
print(count(n))