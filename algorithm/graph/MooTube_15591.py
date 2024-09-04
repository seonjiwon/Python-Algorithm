import sys
from collections import deque

def recommend_algorithm(k, v):
  cnt = 0
  queue = deque([v])

  while queue:
    node = queue.popleft()
    for next_node, weight in USADO[node]:
      if visited[next_node] == float('inf'):
        # print(next_node)
        visited[next_node] = min(visited[node], weight)
        queue.append(next_node)
  visited[v] = 0
  # print(visited)
  for i in range(1, N+1):
    if visited[i] >= k:
      cnt += 1
  return cnt



N, Q = map(int, sys.stdin.readline().strip().split())
USADO = [[] for _ in range(N+1)]
for _ in range(N-1):
  p, q, r = map(int, sys.stdin.readline().strip().split())
  USADO[p].append((q, r))
  USADO[q].append((p, r))

for _ in range(Q):
  k, v = map(int, sys.stdin.readline().strip().split())
  visited = [float('inf')] * (N+1)
  print(recommend_algorithm(k, v))