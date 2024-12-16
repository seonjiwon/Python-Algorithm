import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[float('inf')] * (n+1) for _ in range(n+1)]
path = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
  graph[i][i] = 0

for _ in range(m):
  a, b, c = map(int, input().strip().split())
  graph[a][b] = min(c, graph[a][b])
  path[a][b] = b

for k in range(1, n+1):
  for u in range(1, n+1):
    for v in range(1, n+1):
      if graph[u][v] > graph[u][k] + graph[k][v]:
        graph[u][v] = graph[u][k] + graph[k][v]
        path[u][v] = path[u][k]


for i in range(1, n+1):
  for j in range(1, n+1):
    if graph[i][j] != float('inf'):
      print(graph[i][j], end=" ")
    else:
      print(0, end=" ")
  print()

def print_path(start, end):
  if path[start][end] == 0:
    return []
  ans = [start]
  while start != end:
    start = path[start][end]
    ans.append(start)
  return ans

for s in range(1, n+1):
  for e in range(1, n+1):
    if path[s][e] == float('inf'):
      print(0)
    result = print_path(s, e) #여기에 작업을 쳐서 상위로의 호출
    print(len(result), *result)

