import sys


N, K = map(int, sys.stdin.readline().strip().split())
things = [(0, 0)]

for _ in range(N):
  W, V = map(int, sys.stdin.readline().strip().split())
  things.append((W, V))

ans_list = [[0] * (K + 1) for _ in range(N+1)]

for i in range(1, N + 1):
  for j in range(1, K+1):
    weight = things[i][0]
    value = things[i][1]
    if j < weight:
      ans_list[i][j] = ans_list[i-1][j]
    else:
      ans_list[i][j] = max(value + ans_list[i-1][j-weight], ans_list[i-1][j])
print(ans_list[N][K])
