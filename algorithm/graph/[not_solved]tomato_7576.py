import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def solution():
  for i in range(4):



M, N = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
print(solution())