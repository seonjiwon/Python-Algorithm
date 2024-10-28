import sys
import heapq

def solution():
  result = 0

  while queue:
    if len(queue) == 1:
      break
    C1 = heapq.heappop(queue)
    C2 = heapq.heappop(queue)
    heapq.heappush(queue, C1 + C2)
    result += C1 + C2

  return result


T = int(sys.stdin.readline())
for _ in range(T):
  K = T = int(sys.stdin.readline())
  queue = list(map(int, sys.stdin.readline().strip().split()))
  #queue를 heapq 정렬로 바꿈
  heapq.heapify(queue)
  print(solution())