import sys
input = sys.stdin.readline

n = int(input())
words = list(input().strip().split())

count = 0

for word in words:
  for i in word:
    if not(ord('A') <= ord(i) <= ord('Z') or ord('a') <= ord(i) <= ord('z')):
      count += 1
print(count)