import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
  a, b = map(int, sys.stdin.readline().strip().split())
  graph[a][b] = graph[b][a] = True

visited = [False] * (N+1)

def bfs():
  cnt = 0
  for i in range(1, N+1):
    if not visited[i]:
      cnt += 1
      q = deque([i])
      visited[i] = True
      while q:
        v = q.popleft()
        for j in range(1, N+1):
          if not visited[j] and graph[v][j]:
            q.append(j)
            visited[j] = True
  return cnt

print(bfs())