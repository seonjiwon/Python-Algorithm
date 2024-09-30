import sys

def LCS(s1, s2):
  n = len(s1)
  m = len(s2)
  dp = [[0] * (m+1) for _ in range(n+1)]

  for i in range(1, n+1):
    for j in range(1, m+1):
      if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  result = 0
  for p in dp:
    for q in p:
      result = max(result, q)
  return result


s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

print(LCS(s1, s2))