import sys

def AC_lang(arr):
  result = []
  direction = 1
  start_point = 0
  end_point = len(arr)
  for command in p:
    if command == "R":
      direction *= -1
      temp = start_point
      start_point = end_point
      end_point = temp
    elif command == "D":
      if start_point == end_point:
        return "error"
      elif direction == 1:
        start_point += 1
      elif direction == -1:
        start_point -= 1

  if direction == 1:
    result = arr[start_point:end_point]
  else:
    for i in range(start_point-1, end_point-1, -1):
      result.append(arr[i])

  return "[" + ",".join(map(str, result)) + "]"



T = int(sys.stdin.readline())

for i in range(T):
  p = list(sys.stdin.readline().strip())
  n = int(sys.stdin.readline())
  temp_X = sys.stdin.readline().strip()
  if n == 0:
    X = []
  else:
    X = list(map(int, temp_X[1:len(temp_X)-1].split(',')))

  result = AC_lang(X)
  print(result)
