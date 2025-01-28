import sys
from collections import deque

def bfs():
  q = deque([1])
  visited[1] = 1

  while q:
    V = q.popleft()
    for i in link[V]:
      if not visited[i]:
        parent[i] = V
        visited[i] = 1
        q.append(i)

N = int(sys.stdin.readline())
link = [[] for _ in range(N+1)]
for i in range(N-1):
  left, right = map(int, sys.stdin.readline().strip().split())
  link[left].append(right)
  link[right].append(left)

parent = [0] * (N+1)
visited = [0] * (N+1)
bfs()

for i in range(2, N+1):
  print(parent[i])