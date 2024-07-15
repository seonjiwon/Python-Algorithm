import sys

def purchase_count(n, count_list):
  dp = [0] * (n+1)
  for i in range(1, n+1):
    for j in range(1, i+1):
      dp[i] = max(dp[i], dp[i-j] + count_list[j-1])
  return dp[n]


n = int(sys.stdin.readline().strip())
count_list = list(map(int, sys.stdin.readline().strip().split()))
print(purchase_count(n, count_list))