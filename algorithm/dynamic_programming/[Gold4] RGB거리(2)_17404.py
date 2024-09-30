import sys

def paint_house(n, arr):
  dp_r = [[0] * n for _ in range(3)]
  dp_g = [[0] * n for _ in range(3)]
  dp_b = [[0] * n for _ in range(3)]

  dp_r[0][0] = arr[0][0]
  dp_r[1][0] = float('inf')
  dp_r[2][0] = float('inf')

  dp_g[0][0] = float('inf')
  dp_g[1][0] = arr[0][1]
  dp_g[2][0] = float('inf')

  dp_b[0][0] = float('inf')
  dp_b[1][0] = float('inf')
  dp_b[2][0] = arr[0][2]

  for i in range(1, n):
    for j in range(3):
      dp_r[j][i] = arr[i][j] + min(dp_r[j-2][i-1], dp_r[j-1][i-1])
      dp_g[j][i] = arr[i][j] + min(dp_g[j-2][i-1], dp_g[j-1][i-1])
      dp_b[j][i] = arr[i][j] + min(dp_b[j-2][i-1], dp_b[j-1][i-1])

  min_r = min(dp_r[1][n-1], dp_r[2][n-1])
  min_g = min(dp_g[0][n-1], dp_g[2][n-1])
  min_b = min(dp_b[0][n-1], dp_b[1][n-1])

  return min(min_r, min_g, min_b)


n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
  arr.append(list(map(int, sys.stdin.readline().strip().split())))
print(paint_house(n, arr))