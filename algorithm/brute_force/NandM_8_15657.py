import sys

def backtracking(list):
  if len(array) == m:
    print(' '.join(map(str, array)))
    return

  for i in list:
    if len(array) > 0:
      if i >= array[-1]:
        array.append(i)
      else:
        continue
    else:
      array.append(i)
    backtracking(list)
    array.pop()


n, m = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
list.sort()
array = []

backtracking(list)