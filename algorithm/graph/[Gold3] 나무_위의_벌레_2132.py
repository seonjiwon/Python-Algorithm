import sys
from collections import deque

def bfs(start):
  visited = [-1] * (n+1)
  q = deque([start])
  visited[start] = fruit_num[start]
  max_weight = fruit_num[start]
  # max_node = start

  while q:
    node = q.popleft()
    for next_node in tree[node]:
      if visited[next_node] == -1:
        visited[next_node] = visited[node] + fruit_num[next_node]
        q.append(next_node)

      if visited[next_node] > max_weight:
        max_weight = visited[next_node]
        # max_node = next_node

  max_node = visited.index(max_weight)

  return max_node, max_weight



n = int(sys.stdin.readline())
fruit_num = [0] + list(map(int, sys.stdin.readline().strip().split()))
tree = [[] for _ in range(n+1)]

for i in range(n-1):
  u, v = map(int, sys.stdin.readline().split())
  tree[u].append(v)
  tree[v].append(u)


node_a, _= bfs(1)

max_node, max_weight = bfs(node_a)

print(max_weight, min(max_node, node_a))