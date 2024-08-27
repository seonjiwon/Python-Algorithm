import sys
from collections import deque

def dfs(start, end, temp_cost):
  global cost

  if start == end:
    # print(cost, temp_cost)
    cost = min(cost, temp_cost)
    return

  for i in range(len(link[start])):
    if not visited[link[start][i]]:
      # print(f"start = {start}, arrive = {link[start][i]}, cost = {weight[start][link[start][i]]}, sum_cost = {temp_cost}")
      visited[link[start][i]] = 1
      dfs(link[start][i], end, temp_cost + weight[start][link[start][i]])
      visited[link[start][i]] = 0



N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
link = [[] for _ in range(N + 1)]
weight = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
  u, v, w = map(int, sys.stdin.readline().strip().split())
  link[u].append(v)
  weight[u][v] = w


start, end = map(int, sys.stdin.readline().strip().split())

visited = [0] * (N+1)
visited[start] = 1
cost = float('inf')
dfs(start, end, 0)
print(cost)