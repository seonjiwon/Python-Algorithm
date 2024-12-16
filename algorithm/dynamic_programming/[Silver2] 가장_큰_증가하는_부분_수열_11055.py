import sys

def biggest_ascending_number(n, list):
  dp = [0] * n
  dp[0] = list[0]

  for i in range(1, n):
    dp[i] = list[i]
    for j in range(i):
      if(list[i] > list[i-j-1]):
        dp[i] = max(dp[i], dp[i-j-1] + list[i])
  print(dp)
  return max(dp)

n = int(sys.stdin.readline().strip())
number_list = list(map(int, sys.stdin.readline().strip().split()))
print(biggest_ascending_number(n, number_list))