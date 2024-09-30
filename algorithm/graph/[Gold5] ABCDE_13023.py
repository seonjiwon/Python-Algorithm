import sys

n, m = map(int, sys.stdin.readline().strip().split())
link = [[] * n for _ in range(n)]

for _ in range(m):
  a, b = map(int, sys.stdin.readline().strip().split())
  link[a].append(b)
  link[b].append(a)


def dfs(V, cnt):
  if cnt == 5:
    print(1)
    exit()

  visited[V] = 1
  for i in link[V]:
    if not visited[i]:
      dfs(i, cnt+1)
      visited[i] = 0


for i in range(n):
  visited = [0] * n
  dfs(i, 1)

print(0)