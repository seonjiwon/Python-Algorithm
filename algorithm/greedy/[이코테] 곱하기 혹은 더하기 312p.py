"""
02984 -> 576
567 -> 210
"""

import sys
input = sys.stdin.readline

def solution(num):
  result = int(num[0])
  num = num[1:]
  while len(num) > 0:
    n = int(num[0])
    if n == 0:
      result += n
    else:
      if result == 0:
        result += n
      else:
        result *= n
    num = num[1:]
  return result

N = input().strip()
print(solution(N))