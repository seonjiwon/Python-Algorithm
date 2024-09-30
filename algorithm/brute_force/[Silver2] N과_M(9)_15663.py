import sys

def backtracking():
  if len(array) == m:
    temp = [list[i] for i in array]
    answer.append(temp)
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
tuple_answer = [tuple(i) for i in answer]
set_answer = set(tuple_answer)
list_answer = [i for i in set_answer]
list_answer.sort()

for i in list_answer:
  print(' '.join(map(str, i)))