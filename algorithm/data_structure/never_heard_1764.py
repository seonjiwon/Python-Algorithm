import sys

N, M = map(int, sys.stdin.readline().strip().split())
never_heard = set()
for i in range(N):
  never_heard.add(sys.stdin.readline().strip())

never_sought = set()
for i in range(N):
  never_sought.add(sys.stdin.readline().strip())


ans = sorted(list(never_sought & never_heard))

print(len(ans))
for i in ans:
  print(i)