import sys

def solution(n, list):
  for i in range(n - 1, 0, -1):
    if list[i-1] > list[i]:
      for j in range(n-1, 0, -1):
        if list[i-1] > list[j]:
          list[j], list[i-1] = list[i-1], list[j]
          list = list[:i] + sorted(list[i:], reverse=True)
          print(' '.join(map(str, list)))
          exit()
  else:
    print("-1")


n = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().strip().split()))
solution(n, list)