"""
5
2 3 1 2 2
"""

import sys
input = sys.stdin.readline

def solution():
  result = 0
  count = 0
  for i in fear:
    count += 1
    # 공포도 < 남은 모험가 수 - 1
    if count >= i:
      result += 1
      count = 0
  return result



N = int(input())
fear = list(map(int, input().strip().split()))
fear.sort()
print(solution())