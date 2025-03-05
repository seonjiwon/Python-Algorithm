"""
10101111
01111101
11001110
00000010
2
3 -1
1 1
: 7
"""
import sys
from collections import deque
input = sys.stdin.readline

def shifting(idx, direction):
    if visited[idx] != 0:
        return
    #회전
    visited[idx] = direction

    if idx - 1 >= 0 and cogwheels[idx-1][2] != cogwheels[idx][6]:
        shifting(idx-1, direction * (-1))
    if idx + 1 < 4 and cogwheels[idx][2] != cogwheels[idx+1][6]:
        shifting(idx+1, direction * (-1))

    return




cogwheels = []

for _ in range(4):
    cogwheel = deque([])
    temp = input().strip()
    for t in temp:
        cogwheel.append(int(t))
    cogwheels.append(cogwheel)

K = int(input())
for _ in range(K):
    idx, direction = map(int, input().strip().split())
    visited = [0] * 4
    # print(visited)
    shifting(idx-1, direction)

    # print(visited)
    for i in range(4):
        if visited[i] != 0:
            cogwheels[i].rotate(visited[i])
        # print(cogwheels[i])

result = 0
weight = 1
for cogwheel in cogwheels:
    if cogwheel[0] == 1:
        result += weight
    weight *= 2
print(result)