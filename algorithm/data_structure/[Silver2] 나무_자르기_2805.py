import sys

N, M = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))
left, right = 0, max(trees)

while left <= right:
  mid = (left + right) // 2
  total = 0

  for tree in trees:
    if tree >= mid:
      total += tree - mid

  if total >= M:
    left = mid + 1
  else:
    right = mid - 1

print(right)
