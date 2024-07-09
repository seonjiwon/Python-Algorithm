parenthesis = list(input())

stick = 0
count = 0

for i in range(len(parenthesis)):
  if parenthesis[i] == ')':
    if parenthesis[i-1] == '(':
      stick -= 1
      count += stick
    else:
      stick -= 1
      count += 1
  else:
    stick += 1
print(count)



