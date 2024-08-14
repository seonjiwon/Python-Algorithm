import sys
from collections import deque

uprl = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs(row, col):
  cnt = 1
  graph[row][col] = '0'
  q = deque([(row, col)])

  while q:
    row, col = q.popleft()
    for change_row, change_col in uprl:
      new_row, new_col = row + change_row, col + change_col

      if new_row < 0 or new_col < 0 or new_row >= n or new_col >= n or graph[new_row][new_col] == '0':
        continue

      if graph[new_row][new_col] == '1':
        graph[new_row][new_col] = '0'
        q.append((new_row, new_col))
        cnt += 1
  return cnt



n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
ans = []
for i in range(n):
  for j in range(n):
    if graph[i][j] == '1':
      ans.append(bfs(i, j))

ans.sort()
print(len(ans))
for i in ans:
  print(i)

