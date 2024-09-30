n = int(input())
sum = 1

for i in range(1, n + 1):
  sum *= i

sum = str(sum)[::-1]

is_zero = False
for i in range(0, len(sum)):
  if sum[i] != '0' and is_zero == True:
    print(i)
    break
  elif sum[i] == '0':
    is_zero = True

if is_zero == False:
  print(0)