a, b = map(int, input().split())
m = int(input())
a_list = list(map(int, input().split()))[::-1]

decimal = 0
for i in range(m):
  decimal += a_list[i] * (a**i)

octal = []

while decimal != 0:
  octal.append(decimal % b)
  decimal //= b

print(' '.join(map(str, octal[::-1])))