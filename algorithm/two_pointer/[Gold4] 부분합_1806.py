import sys
input = sys.stdin.readline

def solution():
  start, end = 0, 0
  result = float('inf')
  sum_n = 0
  count_n = 0

  while end < N:
    sum_n += numbers[end]
    count_n += 1

    while sum_n >= S:
      result = min(result, count_n)
      sum_n -= numbers[start]
      count_n -= 1
      start += 1
    else:
      end += 1

  return result if result != float('inf') else 0

N, S = map(int, input().strip().split())
numbers = list(map(int, input().strip().split()))
print(solution())
