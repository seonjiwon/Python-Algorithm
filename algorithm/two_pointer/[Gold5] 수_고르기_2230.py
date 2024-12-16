import sys
input = sys.stdin.readline

def solution():
  start, end = 0, 0
  result = float('inf')

  while start < N:
    if numbers[end] - numbers[start] >= M:
      result = min(result, numbers[end] - numbers[start])
      start += 1
    else:
      if end < N-1:
        end += 1
      else:
        start += 1

  return result


N, M = map(int, input().strip().split())
numbers = []

for _ in range(N):
  numbers.append(int(input()))
numbers.sort()
print(solution())