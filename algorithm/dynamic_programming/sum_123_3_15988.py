import sys

MOD = 1000000009
def sum123():
  dp = [0] * 1000001

  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  for i in range(4, 1000001):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % MOD
  return dp

hei = int(sys.stdin.readline().strip())
n_list = []
for i in range(hei):
  n = int(sys.stdin.readline().strip())
  n_list.append(n)
dp = sum123()
for i in n_list:
  print(dp[i] % MOD)