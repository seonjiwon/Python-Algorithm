import math
import sys

n = int(input())

for i in range(n):
  sum = 0
  numbers = list(map(int, sys.stdin.readline().split()))
  for i in range(1, len(numbers)):
    for j in range(i+1, len(numbers)):
      sum += math.gcd(numbers[i], numbers[j])
  print(sum)