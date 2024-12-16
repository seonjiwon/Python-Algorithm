import sys
input = sys.stdin.readline

n, m, r = map(int, input().strip().split())
item = list(map(int, input().strip().split()))
graph = [[float('inf')] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(r):
  a, b, l = map(int, input().strip().split())
  graph[a][b], graph[b][a] = l, l

for k in range(1, n+1):
  for u in range(1, n+1):
    for v in range(1, n+1):
      graph[u][v] = min(graph[u][v], graph[u][k] + graph[k][v])

result = 0
for i in range(1, n+1):
  temp = 0
  for j in range(1, n+1):
    if graph[i][j] != float('inf') and graph[i][j] <= m:
      temp += item[j-1]
  result = max(result, temp)

print(result)