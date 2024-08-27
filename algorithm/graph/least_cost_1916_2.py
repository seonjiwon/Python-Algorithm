import sys
import heapq

def dijkstra(start, end):
  distance_list = [float('inf')] * (N+1)
  distance_list[start] = 0
  q = [(0, start)]

  while q:
    current_distance, current_node = heapq.heappop(q)
    if current_distance > distance_list[current_node]:
      continue
    for target, weight in graph[current_node]:
      temp_weight = weight + current_distance
      if distance_list[target] > temp_weight:
        distance_list[target] = temp_weight
        q.append((temp_weight, target))

  return distance_list[end]



N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 버스 정보 입력 처리
for i in range(M):
  A, B, C = map(int, sys.stdin.readline().strip().split())
  graph[A].append((B, C))

# 출발점과 도착점 입력 처리
start, end = map(int, sys.stdin.readline().strip().split())

# 다익스트라 알고리즘 수행
result = dijkstra(start, end)
print(result)