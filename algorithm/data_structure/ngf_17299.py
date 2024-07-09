import sys

n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
count = [0 for i in range(1000001)]

for i in num_list:
  count[i] += 1

stack = []
result = [-1 for i in range(n)]
for i in range(n):
  while stack and count[num_list[stack[-1]]] < count[num_list[i]]:
    result[stack.pop()] = num_list[i]
  stack.append(i)
print(' '.join(map(str, result)))