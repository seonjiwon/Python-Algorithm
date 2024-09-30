import sys

def solution(n):
  left, right = 0, len(n) - 1
  pelindrome = "yes"
  while left < right:
    if n[left] != n[right]:
      pelindrome = "no"
    left += 1
    right -= 1
  return pelindrome

while True:
  n = int(sys.stdin.readline().strip())
  if  n == 0:
    exit()
  print(solution(list(str(n))))
