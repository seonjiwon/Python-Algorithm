import sys
from collections import deque
input = sys.stdin.readline

monkey_move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
horse_move = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

def bfs():
  visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
  queue = deque([(0, 0, K)])

  while queue:
    x, y, count_horse = queue.popleft()

    if x == H-1 and y == W-1:
      return visited[x][y][count_horse]

    if count_horse > 0:
      for dx, dy in horse_move:
        nx, ny = x + dx, y + dy
        if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][count_horse-1] == 0 and MAP[nx][ny] != 1:
          visited[nx][ny][count_horse-1] = visited[x][y][count_horse] + 1
          queue.append((nx, ny, count_horse-1))

    for dx, dy in monkey_move:
      nx, ny = x + dx, y + dy
      if 0 <= nx < H and 0 <= ny < W and visited[nx][ny][count_horse] == 0 and MAP[nx][ny] != 1:
        visited[nx][ny][count_horse] = visited[x][y][count_horse] + 1
        queue.append((nx, ny, count_horse))

  return -1



K = int(input())
W, H = map(int, input().strip().split())
MAP = []
for _ in range(H):
  MAP.append(list(map(int, input().strip().split())))

print(bfs())