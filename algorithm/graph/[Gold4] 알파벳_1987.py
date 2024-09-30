import sys
from collections import deque

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_max_move(x, y, cnt):
  global max_cnt
  if cnt > max_cnt:
    max_cnt = cnt

  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if 0 <= nx < R and 0 <= ny < C and dict[board[nx][ny]] == 0:
      dict[board[nx][ny]] = 1
      get_max_move(nx, ny, cnt + 1)
      dict[board[nx][ny]] = 0



R, C = map(int, sys.stdin.readline().strip().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

dict = {}
for i in range(ord('A'), ord('Z') + 1):
  dict[chr(i)] = 0

dict[board[0][0]] = 1
max_cnt = 0
get_max_move(0, 0, 1)

print(max_cnt)