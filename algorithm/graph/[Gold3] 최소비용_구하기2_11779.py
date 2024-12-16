import sys
import heapq
input = sys.stdin.readline

def solution(s, e):
  distance = [float('inf')] * (n+1)
  distance[s] = 0
  queue = [(0, start)]

  while queue:
    dist, u = heapq.heappop(queue)
    if dist > distance[u]:
      continue

    for v, w in graph[u]:
      if distance[v] > dist + w:
        distance[v] = dist + w
        heapq.heappush(queue, (dist + w, v))
        path[v] = u
  return distance[e]

def find_path(visit):
  ans = []

  while visit != start:
    ans.append(visit)
    visit = path[visit]
  ans.append(start)
  ans.reverse()
  print(len(ans))
  print(*ans)



n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
path = [i for i in range(n+1)]

for _ in range(m):
  u, v, w = map(int, input().strip().split())
  graph[u].append((v, w))

start, end = map(int, input().strip().split())
print(solution(start, end))
find_path(end)
