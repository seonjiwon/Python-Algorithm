import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

queue = []
for i in range(N):
  hand = list(input().strip().split())
  name, left_hand, right_hand = hand[0], int(hand[1]), int(hand[2])
  queue.append((left_hand, name))
  queue.append((right_hand, name))
queue.sort()
print(queue[(K-1) % (2*N)][1])