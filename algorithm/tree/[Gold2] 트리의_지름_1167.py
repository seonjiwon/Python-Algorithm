import sys
from collections import deque

def solution(start):
  visited = [-1] * (V+1)
  q = deque([start])
  visited[start] = 0
  max_distance = 0
  max_node = start

  while q:
    node = q.popleft()
    for next_node, weight, in tree[node]:
      if visited[next_node] == -1:
        visited[next_node] = visited[node] + weight
        q.append(next_node)
        if max_distance < visited[next_node]:
          max_distance = visited[next_node]
          max_node = next_node

  return max_node, max_distance



V = int(sys.stdin.readline().strip())
tree = [[] for _ in range(V+1)]
for i in range(V):
  temp = list(map(int , sys.stdin.readline().strip().split()))
  u = temp[0]
  for i in range(1, len(temp) - 1, 2):
    v, w = temp[i], temp[i+1]
    tree[u].append((v, w))

node_a, _ = solution(1)

node_b, max_distance = solution(node_a)

print(max_distance)