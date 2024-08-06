import sys

def backtracking():
  if len(array) == m:
    temp = [list[i] for i in array]
    if temp not in answer:
      answer.append(temp)
      print(' '.join(map(str, temp)))
    return

  for i in range(n):
    if i not in array:
      array.append(i)
      backtracking()
      array.pop()


n, m = map(int, sys.stdin.readline().strip().split())
list = list(map(int, sys.stdin.readline().strip().split()))
list.sort()
array = []
answer = []

backtracking()