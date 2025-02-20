"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
: ((110(0101))(0010)1(0001))
"""
import sys
input = sys.stdin.readline

def quad_tree(row, column, length):
    SUM = 0

    for i in range(length):
        for j in range(length):
            SUM += int(MAP[row + i][column + j])

    if SUM == 0:
        return '0'
    elif SUM == length ** 2:
        return '1'

    else:
        temp = "("
        quad_1 = quad_tree(row, column, length // 2)
        quad_2 = quad_tree(row, column + length // 2, length // 2)
        quad_3 = quad_tree(row + length // 2, column, length // 2)
        quad_4 = quad_tree(row + length // 2, column + length // 2, length // 2)
        temp += quad_1 + quad_2 + quad_3 + quad_4 + ")"

    return temp




N = int(input())
MAP = [list(input().strip()) for _ in range(N)]

print(quad_tree(0, 0, N))
