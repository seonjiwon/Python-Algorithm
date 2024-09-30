import sys

def max_drink(n, wl):
  dp = [0] * (n+1)

  if n == 1:
    return wl[0]
  if n == 2:
    return wl[0] + wl[1]
  if n >=3:
    dp[1] = wl[0]
    dp[2] = wl[0] + wl[1]
    dp[3] = max(wl[0] + wl[2], wl[0] + wl[1], wl[1] + wl[2])

  for i in range(4, n + 1):
    dp[i] = max(dp[i-1], dp[i-2] + wl[i-1], dp[i-3] + wl[i-2] + wl[i-1])
  return dp[n]

n = int(sys.stdin.readline().strip())
wine_list = []
for i in range(n):
  wine = int(sys.stdin.readline().strip())
  wine_list.append(wine)
print(max_drink(n, wine_list))
