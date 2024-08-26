import sys

def solution(n):
  dp = []
  if n >= 0:
    dp.append([1, 0])
  if n >= 1:
    dp.append([0, 1])
  for i in range(2, n+1):
    dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

  return dp[-1]

T = int(sys.stdin.readline())
for i in range(T):
  n = int(sys.stdin.readline())
  print(" ".join(map(str, solution(n))))