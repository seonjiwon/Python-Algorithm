import sys

N = int(sys.stdin.readline())
N_list = set(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().strip().split()))

for i in M_list:
  if i in N_list:
    print(1)
  else:
    print(0)