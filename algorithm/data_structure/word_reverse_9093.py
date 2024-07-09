import sys

n = int(input())

for i in range(n):
  word = sys.stdin.readline().strip().split()
  for w in word:
    w = ''.join(reversed(w))
    print(w, end = " ")
