import math
import sys

list = [True for i in range(1000001)]
for i in range(2, int(math.sqrt(len(list)))):
  if list[i]:
    for j in range(2 * i, 1000001, i):
      list[j] = False
while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  for i in range(3, n, 2):
    if list[i] == True and list[n-i] == True:
      print(f"{n} = {i} + {n-i}")
      break
  else:
    print('"Goldbach\'s conjecture is wrong."')
