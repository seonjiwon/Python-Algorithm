import sys
from collections import deque
def bfs(start):
  global ans

  visited[start] = 1
  q = deque([start])

  while q:

    previous = q.popleft()

    for i in link[previous]:
      if not visited[i]:
        bipartite[start] = 'O'
        q.append(i)
        visited[i] = 1
        bipartite[i] = 'X' if bipartite[previous] == 'O' else 'O'
      elif bipartite[previous] == bipartite[i]:
        ans = "NO"

K = int(sys.stdin.readline())

for i in range(K):
  V, E = map(int, sys.stdin.readline().strip().split())
  link = [[] * (V+1) for _ in range(V+1)]
  visited = [0] * (V+1)
  bipartite = [0] * (V+1)
  ans = "YES"

  for i in range(E):
    u, v = map(int, sys.stdin.readline().strip().split())
    link[u].append(v)
    link[v].append(u)
  for i in range(1, V+1):
    bfs(i)
  print(ans)


