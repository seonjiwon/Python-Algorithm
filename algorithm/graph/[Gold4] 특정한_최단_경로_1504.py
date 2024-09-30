import sys
import heapq

def dijkstra(v1, v2):
  distance = [float('inf')] * (N+1)
  distance[v1] = 0
  q = [(0, v1)]

  while q:
    current_distance, current_node = heapq.heappop(q)
    if current_distance > distance[current_node]:
      continue
    for next_node, weight in graph[current_node]:
      temp_cost = current_distance + weight
      if distance[next_node] > temp_cost:
        distance[next_node] = temp_cost
        heapq.heappush(q, (temp_cost, next_node))

  return distance[v2]


N, E = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  graph[u].append((v, w))
  graph[v].append((u, w))

v1, v2 = map(int, sys.stdin.readline().strip().split())
result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
if result == float('inf'):
  print(-1)
else:
  print(result)
