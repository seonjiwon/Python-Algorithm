import math
import sys

def least_sum_of_square_number(n):
  dp = [100000 for _ in range(n+1)]
  dp[0] = 0
  square_list = []

  for i in range(int(math.sqrt(n)) + 1):
    square_list.append(i**2)

  for i in range(1, n+1):
    for square in square_list:
      if i < square:
        break
      dp[i] = min(dp[i], dp[i-square] + 1)
  return dp[n]

n = int(sys.stdin.readline().strip())
print(least_sum_of_square_number(n))