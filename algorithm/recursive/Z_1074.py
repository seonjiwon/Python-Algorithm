import sys

def z(n, r, c):
  if n == 0:
    return 0
  half = 2 ** (n - 1)
  if r < half and c < half:
    # 1사분면
    return z(n-1, r, c)
  elif r < half and c >= half:
    # 2사분면
    return half * half + z(n-1, r, c-half)
  elif r >= half and c < half:
    # 3사분면
    return 2 * half * half + z(n-1, r-half, c)
  else:
    # 4사분면
    return 3 * half * half + z(n-1, r-half, c-half)

N, r, c = map(int, sys.stdin.readline().strip().split())
print(z(N, r, c))