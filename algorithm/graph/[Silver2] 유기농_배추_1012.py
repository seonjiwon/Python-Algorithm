import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
  q = deque([(x, y)])
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
      if graph[nx][ny]:
        graph[nx][ny] = 0
        q.append((nx, ny))


T = int(sys.stdin.readline())
for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().strip().split())
  cnt = 0
  graph = [[0] * M for _ in range(N)]
  for _ in range(K):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[v][u] = 1
  for i in range(N):
    for j in range(M):
      if graph[i][j]:
        graph[i][j] = 0
        bfs(i, j)
        cnt += 1
  print(cnt)
