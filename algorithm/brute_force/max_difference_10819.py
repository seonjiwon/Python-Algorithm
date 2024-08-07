import sys

def backtracking():
  if len(array) == n:
    temp_arr = [list[i] for i in array]
    temp = 0
    for i in range(n-1):
      temp += abs(temp_arr[i] - temp_arr[i+1])
    different.append(temp)

  for i in range(n):
    if i not in array:
      array.append(i)
      backtracking()
      array.pop()

n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().strip().split()))
array = []
different = []
backtracking()
print(max(different))