import sys
from collections import deque

def bfs(V):
  q = deque([V])
  cnt = 0
  visited[V] = 1

  while q:
    V = q.popleft()
    for i in link[V]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1
        cnt += 1
  return cnt

computer_num = int(sys.stdin.readline())
link_num = int(sys.stdin.readline())
link = [[] for _ in range(computer_num + 1)]
visited = [0] * (computer_num + 1)
for _ in range(link_num):
  u, v = map(int, sys.stdin.readline().strip().split())
  link[u].append(v)
  link[v].append(u)

print(bfs(1))