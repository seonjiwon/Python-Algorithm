"""
2 5
1 2
3 4
:
69 558
337 406
"""
import sys
input = sys.stdin.readline

def mul(U, V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            Z[row][col] = e % 1000

    return Z

def square(metrix, B):
    if B == 1:
        for x in range(len(metrix)):
            for y in range(len(metrix)):
                metrix[x][y] %= 1000
        return metrix

    tmp = square(metrix, B//2)
    if B % 2:
        return mul(mul(tmp, tmp), metrix)
    else:
        return mul(tmp, tmp)

N, B = map(int, input().split())
metrix = [list(map(int, input().strip().split())) for _ in range(N)]

result = square(metrix, B)
for r in result:
    print(*r)