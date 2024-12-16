import sys
input = sys.stdin.readline

def solution(R, B, M):
  for month in range(1, 1201):
    B = B + int((B*R)/100 + 0.5)
    B -= M
    if B <= 0:
      return month
  return "impossible"


tc = int(input())

for _ in range(tc):
  R, B, M = map(float, input().strip().split())
  print(solution(R, B, M))