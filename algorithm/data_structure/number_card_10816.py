import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().strip().split()))
n_dict = {}
for i in N_list:
  if i in n_dict:
    n_dict[i] += 1
  else:
    n_dict[i] = 1
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().strip().split()))

for i in M_list:
  if i in n_dict:
    print(n_dict[i], end=" ")
  else:
    print(0, end=" ")