n = int(input())

divide = 2
while n != 1:
  if n % divide == 0:
    print(divide)
    n //= divide
  elif n % divide != 0:
    divide += 1
