import sys

def backtracking():
  if len(array) == m:
    print(' '.join(map(str, array)))
    return

  for i in range(1, n+1):
    if len(array) > 0:
      if i >= array[-1]:
        array.append(i)
      else:
        continue
    else:
      array.append(i)
    backtracking()
    array.pop()


n, m = map(int, sys.stdin.readline().strip().split())
array = []

backtracking()