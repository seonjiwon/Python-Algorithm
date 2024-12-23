import sys
from collections import deque
input = sys.stdin.readline

def solution(start, end):
  visited[start] = 1
  queue = deque([start])

  while queue:
    node = queue.popleft()
    for i in link[node]:
      if not visited[i]:
        queue.append(i)
        visited[i] = visited[node] + 1

  return visited[end]



#역의 수, 서로 연결하는 역의 갯수, 하이퍼 튜브의 갯수
N, K, M = map(int, input().strip().split())

link = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
  stations = list(map(int, input().strip().split()))
  for i in stations:
    for j in stations:
      if i != j:
        link[i][j] = j

visited = [0] *(N+1)
result = solution(1, N)
print(result if result != float('inf') else -1)