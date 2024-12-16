import sys
input = sys.stdin.readline

N = int(input())
A = map(int, input().strip().split())
q = []
for i in A:
  q.append(-i)
q.sort()
B = list(map(int, input().strip().split()))

B.sort()
result = 0

for i in range(N):
  result += B[i] * -(1 * (q[i]))

print(result)
