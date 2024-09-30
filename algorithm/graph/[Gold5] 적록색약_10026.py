import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(target, x, y):
  q = deque([(x, y)])

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue

      if not visited[nx][ny] and target == graph[nx][ny]:
        visited[nx][ny] = 1
        q.append((nx, ny))


def blind_bfs(target, x, y):
  q = deque([(x, y)])

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if nx < 0 or ny < 0 or nx >= N or ny >= N:
        continue

      if not blind_visited[nx][ny] and (target == graph[nx][ny] or (target == "R" and graph[nx][ny] == "G") or (target == "G" and graph[nx][ny] == "R")):
        blind_visited[nx][ny] = 1
        q.append((nx, ny))



N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]

not_blind_cnt = 0
blind_cnt = 0

visited = [[0] * N for _ in range(N)]
blind_visited = [[0] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    if not visited[i][j]:
      bfs(graph[i][j], i, j)
      not_blind_cnt += 1
    if not blind_visited[i][j]:
      blind_bfs(graph[i][j], i, j)
      blind_cnt += 1


print(not_blind_cnt, blind_cnt)
