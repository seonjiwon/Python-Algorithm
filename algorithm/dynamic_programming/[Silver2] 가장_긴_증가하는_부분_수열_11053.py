import sys

def len_of_longest_increasing_sequence(n, list):
  dp = [0] * (n+1)
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = 1
    for j in range(1, i):
      if list[i-1] > list[i-j-1]:
        dp[i] = max(dp[i], dp[i-j] + 1)
  print(dp)
  return max(dp)



n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
print(len_of_longest_increasing_sequence(n, list))