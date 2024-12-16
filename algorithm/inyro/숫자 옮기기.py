import sys
input = sys.stdin.readline

def operation():
  SLICE = list[start-1:end]
  temp = list[:start-1] + list[end:]
  result = []
  for i in range(idx):
    result.append(temp[i])
  result += SLICE + temp[idx:]
  return result


N, M = map(int, input().strip().split())
list = [i for i in range(1, N+1)]

for _ in range(M):
  start, end, idx = map(int, input().strip().split())
  list = operation()
  # print(list)
for i in list:
  print(i)