import sys
import heapq

input = sys.stdin.readline

N = int(input())
sumu = list(map(int, input().strip().split()))
heapq.heapify(sumu)

hill = []
temp = list(map(int, input().strip().split()))
for i in temp:
  heapq.heappush(hill, -i)


M = int(input())
for _ in range(M):
  command = int(input())
  if command == -1:
    heapq.heappush(hill, -1 * heapq.heappop(sumu))
  else:
    heapq.heappush(sumu, -1 * heapq.heappop(hill))

print(sumu[0], -hill[0])