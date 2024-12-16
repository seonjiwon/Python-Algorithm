import sys
input = sys.stdin.readline

def solution():
  if total % 2 != 0:
    return 0
  target = total // 2
  dp = [0] * (target + 1)
  dp[0] = 1

  for coin, cnt in queue:
    # target부터 0까지 역순으로 순회
    for money in range(target, -1, -1):
      if dp[money]:
        for k in range(1, cnt + 1):
          next_money = money + coin * k
          if next_money <= target:
            dp[next_money] = 1
  return dp[target]

for _ in range(3):
  N = int(input())
  total = 0
  queue = []
  for _ in range(N):
    coin, coin_cnt = map(int ,input().strip().split())
    total += coin * coin_cnt
    queue.append((coin, coin_cnt))
  print(solution())