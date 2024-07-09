import sys
from collections import deque

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for i in range(n)]

for i in range(n):
  while stack and num_list[stack[-1]] < num_list[i]:
    result[stack.pop()] = num_list[i]
  stack.append(i)
print(' '.join(map(str, result)))