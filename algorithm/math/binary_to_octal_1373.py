import sys


def binary_to_octal(n):
  result = []
  temp = 0
  for i in range(len(n)):
    temp += (2**(2 - i%3))*int(n[i])
    if i%3 == 2:
      result .append(str(temp))
      temp = 0
  return ''.join(result)

n = sys.stdin.readline().strip()
padding = (3 - len(n) % 3) % 3
n = '0' * padding + n
print(binary_to_octal(n))
