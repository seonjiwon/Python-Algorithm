import sys

n = int(input())

for i in range(n):
  parenthesis = list(sys.stdin.readline().strip())
  count_left_parenthesis = 0
  count_right_parenthesis = 0
  for p in range(len(parenthesis)):
    if parenthesis[p] == "(":
      count_left_parenthesis += 1
    elif parenthesis[p] == ")":
      count_right_parenthesis += 1

    if count_left_parenthesis < count_right_parenthesis:
      print("NO")
      break

  if count_right_parenthesis < count_left_parenthesis:
    print("NO")
  elif count_right_parenthesis == count_left_parenthesis:
    print("YES")
