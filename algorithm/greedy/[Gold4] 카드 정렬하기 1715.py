import heapq
import sys
input = sys.stdin.readline

def solution():
  result = 0
  while cards:
    if len(cards) >= 2:
      n1 = heapq.heappop(cards)
      n2 = heapq.heappop(cards)
      heapq.heappush(cards, n1 + n2)
      result += n1 + n2
    else:
      break
  return result

N = int(input())
cards = [int(input()) for _ in range(N)]
heapq.heapify(cards)
print(solution())