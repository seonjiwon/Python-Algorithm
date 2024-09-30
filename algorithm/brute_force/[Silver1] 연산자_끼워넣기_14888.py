import sys

def dfs():
  global max_num, min_num
  if len(opList) == O:
    temp = numberList[0]
    for i in range(O):
      if opList[i] == 0:
        temp = temp + numberList[i+1]
      elif opList[i] == 1:
        temp = temp - numberList[i+1]
      elif opList[i] == 2:
        temp = temp * numberList[i+1]
      elif opList[i] == 3:
        if temp < 0 and numberList[i+1] > 0:
          temp = ((temp * (-1)) // numberList[i+1]) * (-1)
        else:
          temp = temp // numberList[i+1]
    max_num = max(max_num, temp)
    min_num = min(min_num, temp)
    return

  for i in range(4):
    if operator[i] > 0:
      operator[i] -= 1
      opList.append(i)
      dfs()
      opList.pop()
      operator[i] += 1


N = int(sys.stdin.readline())
numberList = list(map(int, sys.stdin.readline().strip().split()))
operator = list(map(int, sys.stdin.readline().strip().split()))
O = sum(operator)

visited = [0] * N
opList = []
max_num = -float('inf')
min_num = float('inf')
dfs()
print(max_num)
print(min_num)