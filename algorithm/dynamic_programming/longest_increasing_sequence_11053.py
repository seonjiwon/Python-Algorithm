import sys

def len_of_longest_increasing_sequence(n, list):
  list.sort()
  count = 0
  for i in range(1, n):
    if list[i] > list[i-1]:
      count += 1
  if count > 0:
    count += 1
  return count

n = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
print(len_of_longest_increasing_sequence(n, list))