import sys

def octal_to_binary(n):
  result = ''

  for i in range(len(n)):
    int_n = int(n[i])
    temp = ''
    for _ in range(3):
      temp = str(int_n % 2) + temp
      int_n //= 2
    result += temp
  return result.lstrip('0') or 0


n = str(int(sys.stdin.readline().strip()))
print(octal_to_binary(n))