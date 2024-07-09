import sys

class Stack:
  def __init__(self):
    self._stack = []

  def push(self, number):
    self._stack.append(number)

  def pop(self):
    if self._stack:
      print(self._stack.pop())
    else:
      print(-1)

  def size(self):
    print(len(self._stack))

  def empty(self):
    if self._stack:
      print(0)
    else:
      print(1)

  def top(self):
    if self._stack:
      print(self._stack[-1])
    else:
      print(-1)

  def top(self):
    if len(self._stack) > 0:
      print(self._stack[-1])
    else:
      print(-1)


s = Stack()
n = int(input())

for i in range(n):
  order = sys.stdin.readline().strip()
  if order.startswith("push"):
    _, num = order.split()
    s.push(int(num))
  elif order == "pop":
    s.pop()
  elif order == "size":
    s.size()
  elif order == "empty":
    s.empty()
  elif order == "top":
    s.top()



