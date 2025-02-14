import sys
sys.setrecursionlimit(100000)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a


V, E = map(int, sys.stdin.readline().strip().split())
parent = [0] * (V+1)

for i in range(1, V+1):
  parent[i] = i

edges = []
for _ in range(E):
  a, b, cost = map(int, input().strip().split())
  edges.append((cost, a, b))
edges.sort()

result = 0
for cost, a, b in edges:
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)