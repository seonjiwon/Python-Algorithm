import sys
sys.setrecursionlimit(100000)


def find_parent(parent, x):
  #루트 노드를 찾을때 까지 재귀 호출
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


V, E = map(int, sys.stdin.readline().strip().split())
parent = [0] * (V+1)

edges = []
result = 0

#부모 노드를 자기 자신으로 초기화
for i in range(1, V+1):
  parent[i] = i

for _ in range(E):
  a, b, cost = map(int, sys.stdin.readline().strip().split())
  #비용 순으로 정렬하기 위해 cost를 제일 앞에 위치
  edges.append((cost, a, b))

edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
print(result)