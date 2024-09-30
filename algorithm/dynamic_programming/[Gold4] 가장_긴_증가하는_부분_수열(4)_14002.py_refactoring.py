import sys

def len_of_longest_increasing_sequence(n, list):
  dp = [1] * n
  prev = [-1] * n


  for i in range(1, n):
    for j in range(i):
      if list[i] > list[j] and dp[i] < dp[j] + 1:
        dp[i] = dp[j] + 1
        prev[i] = j

  max_len = max(dp)
  max_index = dp.index(max_len)

  # LIS 구성하기
  lis = []
  while max_index != -1:
    lis.append(list[max_index])
    max_index = prev[max_index]

  lis.reverse()

  print(max_len)
  print(' '.join(map(str, lis)))

n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
len_of_longest_increasing_sequence(n, list)