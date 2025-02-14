import sys
input = sys.stdin.readline

# def solution(n, k, materials):
#     #dp[i][w]를 “i번째 물건까지 고려했을 때, 무게 w일 때의 최대 가치”
#     dp = [[0] * (k+1) for _ in range(n+1)]
#
#     for i in range(1, N+1):
#         weight, value = materials[i]
#         for w in range(1, K+1):
#             if w >= weight:
#                 dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight] + value)
#             else:
#                 dp[i][w] = dp[i-1][w]
#     return dp[n][k]

def solution(k, materials):
    dp = [0] * (k+1)

    for weight, value in materials:
        for w in range(K, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[k]




N, K = map(int, input().strip().split())
materials = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().strip().split())
    materials.append((W, V))
print(solution(K, materials))