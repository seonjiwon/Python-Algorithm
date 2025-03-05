import sys

def backtracking(list):
  if len(array) == m:
    print(' '.join(map(str, array)))
    return

  for i in list:
    array.append(i)
    backtracking(list)
    array.pop()


n, m = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
list.sort()
array = []

backtracking(list)