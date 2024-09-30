import sys

def dfs(previous, now, cost):
  global ans
  if now >= n:
    if now - t_list[previous] <= n and previous + t_list[previous] != n:
      cost -= p_list[previous]
    if ans < cost:
      ans = cost
    return


  for i in range(now, n):
    dfs(i, i + t_list[i], cost + p_list[i])


n = int(sys.stdin.readline())
t_list = []
p_list = []
for i in range(n):
  t, p = map(int, sys.stdin.readline().strip().split())
  t_list.append(t)
  p_list.append(p)

visited = [0] * n
ans = 0
for i in range(n):
  dfs(i,i, 0)
print(ans)