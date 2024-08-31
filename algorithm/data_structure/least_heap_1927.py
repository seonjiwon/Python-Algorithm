import sys
import heapq

N = int(sys.stdin.readline().strip())
q = []
for _ in range(N):
  command = int(sys.stdin.readline().strip())
  if command > 0:
    heapq.heappush(q, command)
  elif command == 0:
    if len(q) == 0:
      print(0)
    else:
      print(heapq.heappop(q))