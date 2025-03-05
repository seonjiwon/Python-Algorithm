"""
4
-6 -8 7 -4
-5 -5 14 11
11 11 -1 -1
4 9 -2 -4
: 11
"""
import sys
input = sys.stdin.readline

def cnn(row, col, n):
    if n == 2:
        rank = [board[row][col], board[row+1][col], board[row][col+1], board[row+1][col+1]]
        rank.sort()
        return [rank[-2]]

    temp = [[0] * (n // 2) for _ in range(n//2)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            temp[i//2][j//2] = cnn(i, j, 2)[0]
    # print(temp)
    return temp

N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]

while True:
    board = cnn(0, 0, len(board))
    if len(board) == 1:
        print(board[0])
        break
