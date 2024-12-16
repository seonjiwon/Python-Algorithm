import sys
input = sys.stdin.readline

def solution():
  result = 0

  for i in range(N):
    temp = A[:i] + A[i+1:]
    start = 0
    end = len(temp) - 1
    while start < end:
      total = temp[start] + temp[end]
      if total == A[i]:
        result += 1
        break
      if total > A[i]:
        end -= 1
      else:
        start += 1
  return result

N = int(input())
A = list(map(int, input().strip().split()))
A.sort()
print(solution())