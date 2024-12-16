import sys
input = sys.stdin.readline

C, N = map(int, input().strip().split())
l = []
dp = [float('inf')] * (1101)
for _ in range(N):
  cost, customer = map(int, input().strip().split())
  dp[customer] = min(cost, dp[customer])
  for i in range(customer, 1101):
    dp[i] = min(dp[i], dp[i-customer] + cost)
print(min(dp[C:]))