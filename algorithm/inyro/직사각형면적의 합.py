import sys
input = sys.stdin.readline


T = int(input())
for i in range(T):
  graph = [[0] * 30000 for _ in range(30000)]
  result = 0
  N = int(input())
  for j in range(N):
    x1, y1, x2, y2 = map(int, input().strip().split())
    for x in range(x1, x2):
      for y in range(y1, y2):
        if graph[x][y] == 0:
          result += 1
          graph[x][y] = 1
  print(result)

