import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

N, M = map(int, input().strip().split())

parent = [i for i in range(N+1)]
edges = []

for _ in range(M):
  u, v, cost = map(int, input().strip().split())
  edges.append((cost, u, v))

edges.sort()

result = 0
max_cost = 0

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    max_cost = max(max_cost, cost)


print(result - max_cost)