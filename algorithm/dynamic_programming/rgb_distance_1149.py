import sys

def paint_rgb_cost(n, house_paint_cost_list):
  dp = [[0] * 3 for _ in range(n+1)]
  dp[1] = house_paint_cost_list[0]

  for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house_paint_cost_list[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house_paint_cost_list[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house_paint_cost_list[i-1][2]
  return min(dp[n])


n = int(sys.stdin.readline().strip())
house_paint_cost_list = []
for i in range(n):
  rgb_cost_list = list(map(int, sys.stdin.readline().strip().split()))
  house_paint_cost_list.append(rgb_cost_list)
print(paint_rgb_cost(n, house_paint_cost_list))