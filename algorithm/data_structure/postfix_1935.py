import sys
import operator

ops = {
  "+" : operator.add,
  "-" : operator.sub,
  "*" : operator.mul,
  "/" : operator.truediv
}

n = int(sys.stdin.readline())
postfix = list(sys.stdin.readline().strip())
stack = []

dict = {}
for i in range(n):
  dict[chr(ord('A') + i)] = int(sys.stdin.readline())

for i in range(len(postfix)):
  if postfix[i] in dict.keys():
    stack.append(dict[postfix[i]])
  else:
    second = stack.pop()
    first = stack.pop()
    calculate = ops[postfix[i]](first, second)
    stack.append(calculate)
print(f"{stack[0]:.2f}")