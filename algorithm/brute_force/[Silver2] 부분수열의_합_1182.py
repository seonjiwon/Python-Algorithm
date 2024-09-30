import sys

def dfs(idx):
  global cnt
  if sum(ans) == s and len(ans) > 0:
    cnt += 1


  for i in range(idx, n):
    ans.append(list[i])
    dfs(i+1)
    ans.pop()


n, s = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
ans = []
cnt = 0
dfs(0)
print(cnt)
