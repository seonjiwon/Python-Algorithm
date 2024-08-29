import sys
import heapq

def dijkstra(start):
  distance = [float('inf')] * (V+1)
  distance[start] = 0
  q = [(0, start)]

  while q:
    current_distance, current_node, = heapq.heappop(q)
    if current_distance > distance[current_node]:
      continue
    for next_node, weight in graph[current_node]:
      temp_cost = weight + current_distance
      if distance[next_node] > temp_cost:
        distance[next_node] = temp_cost
        heapq.heappush(q, (temp_cost, next_node))

  return distance

V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  graph[u].append((v, w))

distance = dijkstra(K)
for i in distance[1:]:
  print(i if i != float('inf') else "INF")