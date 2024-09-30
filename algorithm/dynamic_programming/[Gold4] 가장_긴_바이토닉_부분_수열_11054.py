import sys

def longest_bitonic_sequence(n, list):
  dp = [1] * n
  for i in range(n):
    for j in range(i):
      if list[i] > list[i-j-1]:
        dp[i] = max(dp[i], dp[i-j-1] + 1)

  reverse_list = list[::-1]
  reverse_dp = [1] * n
  for i in range(n):
    for j in range(i):
      if reverse_list[i] > reverse_list[i-j-1]:
        reverse_dp[i] = max(reverse_dp[i], reverse_dp[i-j-1] + 1)
  reverse_dp = reverse_dp[::-1]

  result = [0] * n
  for i in range(n):
    result[i] = max(result[i], dp[i] + reverse_dp[i])
  return max(result) - 1



n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
print(longest_bitonic_sequence(n, list))