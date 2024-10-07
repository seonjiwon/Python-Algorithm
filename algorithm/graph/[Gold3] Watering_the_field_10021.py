import heapq
import sys


def prim(N, C, points):
  visited = [False] * N
  min_cost = 0
  edges = [(0, 0)]  # (cost, node)
  connected = 0 #연결된 node의 수

  #모든 노드가 연결될 때 까지 반복
  while edges and connected < N:
    #가장 작은 비용의 간선을 꺼냄
    cost, node = heapq.heappop(edges)

    if visited[node]:
      continue

    #방문 처리, 연결된 노드의 수 증가
    visited[node] = True
    connected += 1

    if connected > 1:  # 첫 번째 노드의 비용은 무시
      min_cost += cost

    #node 에서 다른 모든 node로의 간선을 고려
    for next_node in range(N):
      if not visited[next_node]:
        next_cost = (points[node][0] - points[next_node][0])**2 + (points[node][1] - points[next_node][1])**2
        if next_cost >= C:
          heapq.heappush(edges, (next_cost, next_node))

  return min_cost if connected == N else -1


N, C = map(int, sys.stdin.readline().strip().split())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = prim(N, C, points)
print(result)
