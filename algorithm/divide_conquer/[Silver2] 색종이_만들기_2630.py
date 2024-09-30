import sys

def separate_color_paper(x, y, N):
  color = paper[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if color != paper[i][j]:
        separate_color_paper(x, y, N//2)
        separate_color_paper(x+N//2, y, N//2)
        separate_color_paper(x, y+N//2, N//2)
        separate_color_paper(x+N//2, y+N//2, N//2)
        return
  if color == 0:
    result[0] += 1
  elif color == 1:
    result[1] += 1



N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
result = [0, 0]

separate_color_paper(0, 0, N)
print(result[0])
print(result[1])