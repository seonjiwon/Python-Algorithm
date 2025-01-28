import sys
from collections import deque

def bfs(start):
  visited = [-1] * (N+1)
  q = deque([start])
  visited[start] = 0
  max_distance = 0
  max_node = start

  while q:
    node = q.popleft()
    for next_node, weight in tree[node]:
      if visited[next_node] == -1:
        visited[next_node] = visited[node] + weight
        q.append(next_node)

        if visited[next_node] > max_distance:
          max_distance = visited[next_node]
          max_node = next_node

  return max_node, max_distance

N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v, w = map(int, sys.stdin.readline().split())
  tree[u].append((v, w))
  tree[v].append((u, w))

#임의의 노드 에서 가장 먼 노드를 찾음
node_a, _ = bfs(1)

#node_a에서 가장 먼 노드를 찾음
_, max_distance = bfs(node_a)

print(max_distance)
