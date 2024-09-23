import sys

n = int(sys.stdin.readline())
MOD = 1000000007

# n번 째 피보나치 수는 행렬 (1 1, 1 0)^n 의 1행 2열 값이다(단, n>=1일때)

def mul(A, B):
  n = len(A)
  Z = [[0]*n for _ in range(n)]

  for row in range(n):
    for col in range(n):
      e = 0
      for i in range(n):
        e += A[row][i] * B[i][col]
      Z[row][col] = e % MOD

  return Z

def square(matrix, k):
  if k == 1:
    for x in range(len(matrix)):
      for y in range(len(matrix)):
        matrix[x][y] %= MOD
    return matrix

  tmp = square(matrix, k//2)
  if k % 2:
    return mul(mul(tmp, tmp), matrix)
  else:
    return mul(tmp, tmp)

fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])