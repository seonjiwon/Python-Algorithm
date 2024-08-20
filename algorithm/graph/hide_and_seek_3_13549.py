import sys
from collections import deque

def bfs(V):
  q = deque([(V, 0)])
  ans = float('inf')

  while q:
    V, S = q.popleft()
    if V == K:
      ans = min(ans, S)
    if V > 100000 or V < 0:
      continue
    link[V][0] = (V-1)
    second[V][0] = S + 1
    link[V][1] = (V+1)
    second[V][1] = S + 1
    link[V][2] = (2*V)
    second[V][2] = S

    for i in range(3):
      if visited[link[V][i]] < 3:
        visited[link[V][i]] += 1
        q.append((link[V][i], second[V][i]))
  return ans



N, K = map(int, sys.stdin.readline().strip().split())
link = [[0] * 3 for _ in range(200001)]
second = [[0] * 3 for _ in range(200001)]
visited = [0] * 200001

print(bfs(N))