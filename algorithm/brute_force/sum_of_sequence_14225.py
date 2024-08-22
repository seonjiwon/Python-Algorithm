import sys

def dfs(idx):
  global sum

  for i in range(idx, N):
    if not visited[i]:
      sum += S[i]
      visited[i] = 1
      dfs(i+1)
      arr[sum] = 1
      sum -= S[i]
      visited[i] = 0


N = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().strip().split()))

sum = 0
visited = [0] * N
arr = [0] * 2000001

dfs(0)

print(arr[1:].index(0) + 1)
