import sys
from collections import deque

move = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

def bfs(row, col):
  MAP[row][col] = 0
  q = deque([(row, col)])

  while q:
    row, col = q.popleft()
    for change_row, change_col in move:
      new_row, new_col = row + change_row, col + change_col

      if new_row < 0 or new_col < 0 or new_row >= h or new_col >= w or MAP[new_row][new_col] == 0:
        continue

      if MAP[new_row][new_col]:
        q.append((new_row, new_col))
        MAP[new_row][new_col] = 0

while True:
  w, h = map(int, sys.stdin.readline().split())
  ans = 0
  if w == 0 and h == 0:
    break
  if w == 1 and h == 1:
    ans = 1 if int(sys.stdin.readline()) == 1 else 0
    print(ans)
  else:
    MAP = [list(map(int, sys.stdin.readline().strip().split()))for _ in range(h)]
    for i in range(h):
      for j in range(w):
        if MAP[i][j]:
          bfs(i, j)
          ans += 1
    print(ans)

