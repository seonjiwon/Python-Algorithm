import sys

def backtracking():
  if len(array) == n:
    print(' '.join(map(str, array)))
    return

  for i in range(1, n+1):
    if i not in array:
      array.append(i)
      backtracking()
      array.pop()

n = int(sys.stdin.readline())
array = []

backtracking()