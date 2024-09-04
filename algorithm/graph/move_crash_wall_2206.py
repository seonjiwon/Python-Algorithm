import sys
from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution():
  queue = deque([(0, 0, 0)])

  while queue:
    x, y, z = queue.popleft()
    if x == N-1 and y == M - 1:
      return visited[x][y][z]

    for dx, dy in directions:
      nx, ny = x + dx, y + dy

      if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue

      if graph[nx][ny] == 1 and z == 0:
        visited[nx][ny][1] = visited[x][y][0] + 1
        queue.append((nx, ny, 1))

      if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
        visited[nx][ny][z] = visited[x][y][z] + 1
        queue.append((nx, ny, z))

  return -1


N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(solution())