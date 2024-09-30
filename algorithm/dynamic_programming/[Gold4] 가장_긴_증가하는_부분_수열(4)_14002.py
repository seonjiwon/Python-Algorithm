import sys

def len_of_longest_increasing_sequence(n, list):
  dp = [0] * (n+1)
  dp_arr = [[] for _ in range(n+1)]

  dp[1] = 1
  dp_arr[1].append(list[0])

  for i in range(2, n+1):
    dp[i] = 1
    dp_arr[i].append(list[i-1])
    for j in range(1, i):
      if list[i-1] > list[i-j-1]:
        if dp[i] < dp[i-j] + 1:
          dp_arr[i] = [list[i-1]]
          dp_arr[i] = dp_arr[i-j] + dp_arr[i]
        dp[i] = max(dp[i], dp[i-j] + 1)
  print(max(dp))
  print(' '.join(map(str, dp_arr[dp.index(max(dp))])))




n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
len_of_longest_increasing_sequence(n, list)