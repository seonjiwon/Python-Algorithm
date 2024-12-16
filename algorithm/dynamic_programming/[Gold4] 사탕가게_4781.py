import sys
input = sys.stdin.readline

while True:
  n, m = input().strip().split()
  n = int(n)
  m = int(float(m) * 100 + 0.5)  # 소수점 오차 방지

  if n == 0 and m == 0:
    break

  # dp[i]: i원으로 살 수 있는 최대 칼로리
  dp = [0] * (m + 1)

  # 각 사탕에 대해
  for _ in range(n):
    c, p = input().strip().split()
    calorie = int(c)
    price = int(float(p) * 100 + 0.5)  # 소수점 오차 방지

    if price <= m:  # 가격이 예산보다 작은 경우만 처리
      # 각 금액에 대해 최대 칼로리 계산
      for i in range(price, m + 1):
        dp[i] = max(dp[i], dp[i - price] + calorie)

  print(dp[m])