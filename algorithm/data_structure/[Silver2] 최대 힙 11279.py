"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if len(queue) == 0:
            print(0)
        else:
            print(-heapq.heappop(queue))
    else:
        heapq.heappush(queue, -cmd)
