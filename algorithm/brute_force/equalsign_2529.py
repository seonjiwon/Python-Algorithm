import sys

def backtracking(previous):
  if len(arr) == k+1:
    if ans.count(0) == 2:
      ans[0] = arr[:]
    else:
      ans[1]  = arr[:]
    return


  for i in range(9, -1, -1):
    idx = len(arr) - 1
    if not visited[i]:
      if len(arr) > 0:
        if list[idx] == "<":
          if previous > i:
            continue
        elif list[idx] == ">":
          if previous < i:
            continue
        visited[i] = 1
        arr.append(i)
        backtracking(i)
      else:
        visited[i] = 1
        arr.append(i)
        backtracking(i)
      arr.pop()
      visited[i] = 0




k = int(sys.stdin.readline())
list = list(sys.stdin.readline().strip().split())
arr = []
visited = [0] * 10
ans = [0, 0]
backtracking(0)
print(''.join(map(str, ans[0])))
print(''.join(map(str, ans[1])))