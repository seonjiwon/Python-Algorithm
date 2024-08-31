import sys
from collections import deque

def hide_and_seek(N, K):
  global cnt
  S = 0
  queue = deque([(N, S)])
  visited[N] = 1

  while queue:
    node, node_S = queue.popleft()
    if node == K:
      print(node_S)
      return
    graph[node].append(node-1)
    graph[node].append(node+1)
    graph[node].append(node*2)
    for i in graph[node]:
      if i >= 0 and i < 200001:
        if not visited[i]:
          visited[i] = 1
          queue.append((i, node_S+1))
    cnt += 1


N, K = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(200001)]
visited = [0] * 200001
cnt = 0
hide_and_seek(N, K)
