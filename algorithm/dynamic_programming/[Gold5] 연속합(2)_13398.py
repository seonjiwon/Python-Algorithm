import sys

def continuous_number_sum(n, list):
  dp = [[0] * n for _ in range(2)]
  dp[0][0] = dp[1][0] = list[0]

  for i in range(1, n):
    dp[0][i] = max(list[i], dp[0][i-1] + list[i])
    if list[i-1] < 0:
      dp[1][i] = max(dp[1][i-1]+list[i], dp[0][i-2] + list[i])
    else:
      dp[1][i] = max(list[i], dp[1][i-1] + list[i])
  return max(max(dp[0]), max(dp[1]))


n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
print(continuous_number_sum(n, list))
