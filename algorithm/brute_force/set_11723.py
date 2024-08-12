import sys

n = int(sys.stdin.readline())
arr= [0 for i in range(21)]
for i in range(n):
  order = list(sys.stdin.readline().strip().split())
  if len(order) == 1:
    if order[0] == 'all':
      arr = [1 for i in range(21)]
    elif order[0] == 'empty':
      arr = [0 for i in range(21)]
  else:
    command = order[0]
    num = int(order[1])
    if command == 'add':
      if arr[num] == 0:
        arr[num] = 1
    elif command == 'remove':
      if arr[num] == 1:
        arr[num] = 0
    elif command == 'check':
      if arr[num] == 1:
        print(1)
      else:
        print(0)
    elif command == 'toggle':
      if arr[num] == 1:
        arr[num] = 0
      else:
        arr[num] = 1
