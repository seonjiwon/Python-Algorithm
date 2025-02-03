import itertools
import copy
from collections import deque

def spread_virus(lab, virus_positions):
  N = len(lab)
  M = len(lab[0])
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
  queue = deque(virus_positions)

  while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
        lab[nx][ny] = 2
        queue.append((nx, ny))

def get_safe_area(lab):
  safe_area = 0
  for row in lab:
    safe_area += row.count(0)
  return safe_area

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty_spaces = []
virus_positions = []

for i in range(N):
  for j in range(M):
    if lab[i][j] == 0:
      empty_spaces.append((i, j))
    elif lab[i][j] == 2:
      virus_positions.append((i, j))

max_safe_area = 0

for walls in itertools.combinations(empty_spaces, 3):
  new_lab = copy.deepcopy(lab)
  for x, y in walls:
    new_lab[x][y] = 1

  spread_virus(new_lab, virus_positions)

  max_safe_area = max(max_safe_area, get_safe_area(new_lab))

print(max_safe_area)