import sys
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(x, y, distance):
  queue = deque([(x, y, distance)])
  while queue:
    tx, ty, td = queue.popleft()
    for dx, dy in direction:
      nx, ny = tx + dx, ty + dy
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
        visited[nx][ny] = 1
        graph[nx][ny] = td
        queue.append((nx, ny, td + 1))





n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
start_x = start_y = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      start_x, start_y = i, j
graph[start_x][start_y] = 0
visited[start_x][start_y] = 1
solution(start_x, start_y, 1)

for i in range(n):
  for j in range(m):
    if visited[i][j] == 0 and graph[i][j] != 0:
      graph[i][j] = -1

for i in graph:
  print(*i)