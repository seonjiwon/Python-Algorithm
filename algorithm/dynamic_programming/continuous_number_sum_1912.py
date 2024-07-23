import sys

def sum_continous_number(n, list):
  dp = [-1000] * (n+1)

  for i in range(1, n+1):
    dp[i] = max(list[i-1], list[i-1] + dp[i-1])

  return max(dp)

n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
print(sum_continous_number(n, list))