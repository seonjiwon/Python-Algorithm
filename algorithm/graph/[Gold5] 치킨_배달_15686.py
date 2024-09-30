import sys
import itertools


def solution(selected_chicken):
  total_distance = 0
  for nx, ny in houses:
    distance = float('inf')
    for cx, cy in selected_chicken:
      distance = min(distance, abs(cx - nx) + abs(cy - ny))
    total_distance += distance

  return total_distance




N, M = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

houses = []
chickens = []
for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      houses.append((i, j))
    if graph[i][j] == 2:
      chickens.append((i, j))

min_cost = float('inf')
for selected_chicken in itertools.combinations(chickens, M):
  min_cost = min(min_cost, solution(selected_chicken))

print(min_cost)