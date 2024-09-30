import sys

def longest_descending_sequence(n, arr):
  dp = [0] * n
  dp[0] = 1

  for i in range(1, n):
    dp[i] = 1
    for j in range(i):
      if(arr[i] < arr[i-j-1]):
        dp[i] = max(dp[i], dp[i-j-1] + 1)
  return max(dp)

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split()))
print(longest_descending_sequence(n, arr))