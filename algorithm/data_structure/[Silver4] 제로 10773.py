"""
4
3
0
4
0
"""
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    numbers = int(input())
    if numbers == 0:
        stack.pop()
    else:
        stack.append(numbers)
print(sum(stack))