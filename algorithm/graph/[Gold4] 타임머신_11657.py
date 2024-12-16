import sys
input = sys.stdin.readline

def bellman_ford():
  dist = [float('inf')] * (N+1)
  dist[1] = 0

  for i in range(N):
    for j in range(M):
      u, v, w = graph[j]
      if dist[v] > dist[u] + w:
        if i == N-1:
          return -1
        dist[v] = dist[u] + w

  return dist[2:]


N, M = map(int, input().strip().split())
graph = []
for _ in range(M):
  A, B, C = map(int, input().strip().split())
  graph.append((A, B, C))

result = bellman_ford()
if result != -1:
  for i in result:
    if i == float('inf'):
      print(-1)
    else:
      print(i)
else:
  print(-1)