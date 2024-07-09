import math

m, n = map(int, input().split())
answer = []

for i in range(m, n+1):
  if i == 1:
    continue
  if i == 2:
    print(i)
    continue
  for j in range(2, math.trunc(math.sqrt(i)) + 1):
    if(i % j == 0):
      break
  else:
    print(i)
