import sys

def dfs(start, now, cost, depth):
  global ans
  if depth == n:
    if costs[now][start]:
      cost += costs[now][start]
      if ans > cost:
        ans = cost
    return


  for i in range(n):
    if visited[i] == 0 and costs[now][i]:
      visited[i] = 1
      dfs(start, i, cost + costs[now][i], depth + 1)
      visited[i] = 0

n = int(sys.stdin.readline())
costs = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
ans = sys.maxsize
visited = [0] * n

for i in range(n):
  visited[i] = 1
  dfs(i, i, 0, 1)
  visited[i] = 0
print(ans)