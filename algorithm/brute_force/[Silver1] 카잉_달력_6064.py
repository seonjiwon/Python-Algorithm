import sys

def calc_k(m, n, x, y):
  answer = 0
  a = b = 0
  for i in range(m):
    if (n*b + (y-x)) % m == 0:
      answer = n * b + y
      break
    b += 1
  else:
    answer = -1
  return answer


n = int(sys.stdin.readline())
for i in range(n):
  m, n, x, y = map(int, sys.stdin.readline().strip().split())
  print(calc_k(m, n, x, y))