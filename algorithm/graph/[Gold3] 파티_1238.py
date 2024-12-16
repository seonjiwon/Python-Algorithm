import sys
import heapq

def dijkstra(start, end):
  distance = [float('inf')] * (N+1)
  distance[start] = 0
  q = [(0, start)]

  while q:
    dist, u = heapq.heappop(q)
    if dist > distance[u]:
      continue
    for v, w in load[u]:
      if distance[v] > dist + w:
        distance[v] = dist + w
        heapq.heappush(q, (dist + w, v))

  return distance[end]

N, M, X = map(int, sys.stdin.readline().strip().split())
load = [[] for _ in range(N+1)]
for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  load[u].append((v, w))

max_distance = 0
for i in range(1, N+1):
  max_distance = max(max_distance, dijkstra(i, X) + dijkstra(X, i))
print(max_distance)