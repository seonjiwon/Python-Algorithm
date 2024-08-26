import sys

def solution():
  ans[0] = 0
  ans[1] = num_list[0]
  for i in range(2, N+1):
    ans[i] = (ans[i-1] + num_list[i-1])

N, M = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))
ans = [0] * (N+1)
l = [map(int , sys.stdin.readline().strip().split()) for _ in range(M)]

solution()
for i, j in l:
  print(ans[j] - ans[i-1])