n = int(input())
number_list = []

for i in range(n):
  number_list.append(int(input()))

stack = []
result = []
ascending_number = 1

for number in number_list:
  while ascending_number <= number:
    stack.append(ascending_number)
    result.append("+")
    ascending_number += 1
  if stack[-1] == number:
    result.append("-")
    pop = stack.pop()
  else:
    print("NO")
    break
else:
  print("\n".join(result))



