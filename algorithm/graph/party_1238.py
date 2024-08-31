import sys
import heapq

def dijkstra(start, end):
  distance_list = [float('inf')] * (N+1)
  distance_list[start] = 0
  q = [(0, start)]

  while q:
    distance, node = heapq.heappop(q)
    if distance > distance_list[node]:
      continue
    for target, weight, in load[node]:
      temp_weight = distance + weight
      if distance_list[target] > temp_weight:
        distance_list[target] = temp_weight
        heapq.heappush(q, (temp_weight, target))

  return distance_list[end]

N, M, X = map(int, sys.stdin.readline().strip().split())
load = [[] for _ in range(N+1)]
for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  load[u].append((v, w))

max_distance = 0
for i in range(1, N+1):
  max_distance = max(max_distance, dijkstra(i, X) + dijkstra(X, i))
print(max_distance)