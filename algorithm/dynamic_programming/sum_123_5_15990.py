import sys
MOD = 1000000009

def sum123(max_n):

  dp = [[0] * 4 for _ in range(max_n+1)]

  if max_n >= 1:
    dp[1][1] = 1
  if max_n >= 2:
    dp[2][2] = 1
  if max_n >= 3:
    dp[3][1] = 1
    dp[3][2] = 1
    dp[3][3] = 1

  for i in range(4, max_n+1):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD
  return dp


hei = int(sys.stdin.readline().strip())
list = []
for i in range(hei):
  n = int(sys.stdin.readline().strip())
  list.append(n)
max_n = max(list)
dp = sum123(max_n)
for i in list:
  print((dp[i][1] + dp[i][2] + dp[i][3])%MOD)