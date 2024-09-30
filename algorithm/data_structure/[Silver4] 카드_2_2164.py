import sys
from collections import deque

def solution():
  stack = deque([])
  for i in range(1, N+1):
    stack.append(i)
  while stack:
    stack.popleft()
    if len(stack) == 1:
      print(stack.popleft())
      exit()
    stack.append(stack.popleft())

N = int(sys.stdin.readline())
if N == 1:
  print(1)
  exit()
solution()