import sys
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(x, y, depth, total):
  global result

  if depth == 4:
    result = max(result, total)
    return

  for dx, dy in direction:
    nx = x + dx
    ny = y + dy

    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
      if depth == 2:
        visited[nx][ny] = True
        for dx2, dy2 in direction:
          nx2, ny2 = x + dx2, y + dy2
          if 0 <= nx2 < N and 0 <= ny2 < M and not visited[nx2][ny2]:
            solution(x, y, depth+2, total + board[nx][ny] + board[nx2][ny2])
        visited[nx][ny] = False

      visited[nx][ny] = True
      solution(nx, ny, depth + 1, total + board[nx][ny])
      visited[nx][ny] = False



N, M = map(int, input().strip().split())
board = []
result = 0
for _ in range(N):
  row = list(map(int, input().strip().split()))
  board.append(row)

visited = [[False] * M for _ in range(N)]
for i in range(N):
  for j in range(M):
    visited[i][j] = True
    solution(i, j, 1, board[i][j])
    visited[i][j] = False
print(result)