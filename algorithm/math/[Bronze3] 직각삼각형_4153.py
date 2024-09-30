import sys

def solution(l):
  n3 = max(l)
  l.remove(n3)
  ans = "right"
  if l[0] ** 2 + l[1] ** 2 != n3 ** 2:
    ans = "wrong"
  if l[0] + l[1] < n3:
    ans = "wrong"
  return ans


while True:
  l = list(map(int, sys.stdin.readline().strip().split()))
  if l[0] == l[1] == l[2] == 0:
    exit()
  print(solution(l))