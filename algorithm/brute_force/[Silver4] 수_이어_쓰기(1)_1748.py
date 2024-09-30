import sys

n = int(sys.stdin.readline())
answer = 0
for i in range(len(str(n)), 0, -1):
  answer += (n - (10**(i-1)) + 1) * i
  n = n - (n - (10**(i-1)) + 1)
print(answer)