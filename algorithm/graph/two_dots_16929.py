import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def cycle(target, x, y, cnt, start_x, start_y):
  global ans
  if ans is True:
    return

  for i in range(4):

    nx, ny = x + dx[i], y + dy[i]

    if nx < 0 or ny < 0 or nx >= n or ny >=m:
      continue
    if cnt >= 4 and nx == start_x and ny == start_y:
      ans = True
      return
    if board[nx][ny] == target and visited[nx][ny] == 0:
      visited[nx][ny] = 1
      cycle(target, nx, ny, cnt + 1, start_x, start_y)
      visited[nx][ny] = 0





n, m = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[0]* m for _ in range(n)]
ans = False

for i in range(n):
  for j in range(m):
    start_x, start_y = i, j
    visited[start_x][start_y] = 1
    cycle(board[i][j], i, j, 1, start_x, start_y)
if ans:
  print("Yes")
else:
  print("No")