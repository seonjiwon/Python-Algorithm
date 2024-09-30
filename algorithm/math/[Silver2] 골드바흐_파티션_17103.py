import math
import sys

eratosthenes = [True for i in range(1000001)]

for i in range(2, int(math.sqrt(len(eratosthenes)))):
  if eratosthenes[i]:
    for j in range(2 * i, 1000001, i):
      eratosthenes[j] = False

n = int(sys.stdin.readline().strip())
for i in range(n):
  num = int(sys.stdin.readline().strip())
  count = 0
  for j in range(2, int(num/2) + 1):
    if eratosthenes[j] == True and eratosthenes[num-j] == True:
      count += 1
  print(count)

