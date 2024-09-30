import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = min(c, graph[a][b])

for i in range(1, n + 1):
  for r in range(1, n + 1):
    for c in range(1, n + 1):
      graph[r][c] = min(graph[r][c], graph[r][i] + graph[i][c])


for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] == float('inf'):
      print(0, end=" ")
    else:
      print(graph[i][j], end=" ")
  print()