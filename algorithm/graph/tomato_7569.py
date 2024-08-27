import sys
from collections import deque

def bfs():
  direction = [(0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)]
  q = deque()

  for h in range(H):
    for i in range(N):
      for j in range(M):
        if whole_basket[h][i][j] == 1:
          q.append((i, j, h))

  while q:
    x, y, z = q.popleft()
    for dx, dy, dz in direction:
      nx, ny, nz = x + dx, y + dy, z + dz
      if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and whole_basket[nz][nx][ny] == 0:
        whole_basket[nz][nx][ny] = whole_basket[z][x][y] + 1
        q.append((nx, ny, nz))

  max_days = 0
  for basket in whole_basket:
    for row in basket:
      for val in row:
        if val == 0:
          return -1
        max_days = max(max_days, val)
  return max_days - 1


M, N, H = map(int, sys.stdin.readline().strip().split())
whole_basket = []
for i in range(H):
  basket = []
  for _ in range(N):
    basket.append(list(map(int, sys.stdin.readline().strip().split())))
  whole_basket.append(basket)

max_days = bfs()
print(max_days)