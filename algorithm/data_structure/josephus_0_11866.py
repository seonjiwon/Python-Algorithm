from collections import deque
n, k = map(int, input().split())

n_list = deque([i for i in range(1, n+1)])
result = []

for i in range(n):
  n_list.rotate(-k + 1)
  result.append(str(n_list.popleft()))
print(f"<{', '.join(result)}>")