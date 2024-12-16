import sys
input = sys.stdin.readline

def solution():
  x1, y1, x2, y2 = float('inf'), float('inf'), 0, 0
  is_D = False

  for row in range(N):
    for column in range(M):
      if folder[row][column] == 'D':
        x1 = min(x1, row)
        y1 = min(y1, column)
        x2 = max(x2, row)
        y2 = max(y2, column)
        is_D = True
  if not is_D:
    print(0)
  else:
    print(x1, y1, x2+1, y2+1)


N, M = map(int, input().strip().split())
folder = [list(input().strip()) for _ in range(N)]
solution()