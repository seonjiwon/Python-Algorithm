from collections import deque
import sys

def bfs():
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
  q = deque()

  # 익은 토마토가 있는 모든 위치를 큐에 추가
  for i in range(N):
    for j in range(M):
      if grid[i][j] == 1:
        q.append((i, j))

  while q:
    x, y = q.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
        grid[nx][ny] = grid[x][y] + 1
        q.append((nx, ny))

  # 결과 계산
  max_days = 0
  for row in grid:
    for val in row:
      if val == 0:
        return -1
      max_days = max(max_days, val)

  return max_days - 1

M, N = map(int, sys.stdin.readline().strip().split())
grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

result = bfs()
print(result)