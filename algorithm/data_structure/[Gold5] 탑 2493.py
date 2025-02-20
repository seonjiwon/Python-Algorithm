"""
5
6 9 5 7 4
: 0 0 2 2 4
"""
import sys
input = sys.stdin.readline

def solution():
    answer = [0] * N

    stack = []

    for i in range(N):
        height, order = TOP.pop()
        if len(stack) > 0:
            while stack:
                s_height, s_order = stack.pop()
                if s_height <= height:
                    answer[s_order-1] = order
                else:
                    stack.append((s_height, s_order))
                    break
        stack.append((height, order))

    return answer

N = int(input())
temp = list(map(int, input().strip().split()))
# (길이, 순서)
TOP = []
for i in range(1, N+1):
    TOP.append((temp[i-1], i))
print(*solution())