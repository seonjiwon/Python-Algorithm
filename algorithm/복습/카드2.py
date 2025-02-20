import sys
from collections import deque
input = sys.stdin.readline


def solution():
    queue = deque([])
    for i in range(1, N+1):
        queue.append(i)

    while queue:
        queue.popleft()
        # print(queue)
        if len(queue) == 1:
            break
        queue.append(queue.popleft())
        # print(queue)
    return queue.pop()


N = int(input())
print(solution())