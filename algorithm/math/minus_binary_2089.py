import sys

def decimal_to_minus_binary(n):
  result = []
  while n != 0:
    if n == 1:
      result.append(1)
      break
    else:
      result.append(abs(n%-2))
      if n%-2 == 0:
        n = n//-2
      else:
        n = n//-2 + 1
  return ''.join(map(str, result[::-1])) or 0


n = int(sys.stdin.readline().strip())
print(decimal_to_minus_binary(n))