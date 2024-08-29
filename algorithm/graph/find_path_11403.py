import sys
from collections import deque

def find_link(x):
  queue = deque([x])
  check = [0 for _ in range(N)]

  while queue:
    V = queue.popleft()
    for i in range(N):
      if check[i] == 0 and graph[V][i] == 1:
        queue.append(i)
        check[i] = 1
        visited[x][i] = 1


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
  find_link(i)

for i in visited:
  print(*i)