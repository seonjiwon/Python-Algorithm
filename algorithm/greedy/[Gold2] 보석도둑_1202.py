import heapq
import sys
input = sys.stdin.readline

def solution():
  result = 0
  temp = []

  while bag:
    w = heapq.heappop(bag)
    while jewel and w >= jewel[0][0]:
      weight, price = heapq.heappop(jewel)
      if weight <= w:
        heapq.heappush(temp, -price)

    if temp:
      result -= heapq.heappop(temp)
  return result

N, K = map(int ,input().strip().split())
jewel = []
bag = []

for _ in range(N):
  M, V = map(int, input().strip().split())
  heapq.heappush(jewel, (M, V))

for _ in range(K):
  C = int(input())
  heapq.heappush(bag, C)
print(solution())
