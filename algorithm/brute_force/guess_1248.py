import sys

def dfs(depth):
  if depth == n:
    print(' '.join(map(str, arr)))
    exit()

  for i in range(-10, 11):
    arr.append(i)
    valid = True
    current_sum = 0

    for j in range(depth, -1, -1):
      current_sum += arr[j]
      if S[j][depth] == '+' and current_sum <= 0:
        valid = False
        break
      if S[j][depth] == '-' and current_sum >= 0:
        valid = False
        break
      if S[j][depth] == '0' and current_sum != 0:
        valid = False
        break

    if valid:
      dfs(depth + 1)
    arr.pop()


n = int(sys.stdin.readline())
list = list(sys.stdin.readline().strip())
S = []
for i in range(n, 0, -1):
  temp = ['' for _ in range(n-i)]
  temp += list[:i]
  S.append(temp)
  list = list[i:]

arr = []
dfs(0)