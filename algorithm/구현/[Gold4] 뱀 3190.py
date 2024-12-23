import sys
from collections import deque
input = sys.stdin.readline

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solution(board):
    answer = 0
    length = 1
    x, y = 0, 0
    queue = deque([(x, y)])
    direction = 0
    board[x][y] = 1

    t, d = change_directions.popleft()

    while True:
        answer += 1
        dx, dy = directions[direction]
        x, y = x + dx, y + dy
        if x < 0 or x >= N or y < 0 or y >= N:
            break
        if board[x][y] == 1:
            break

        if board[x][y] != 'A':
            i, j = queue.popleft()
            board[i][j] = 0
        board[x][y] = 1
        queue.append((x, y))

        if int(t) == answer:
            if d == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            if change_directions:
                t, d = change_directions.popleft()


    return answer

N = int(input())
K = int(input())
apples = []
for _ in range(K):
    apples.append(list(map(int, input().strip().split())))

L = int(input())
change_direction = []
for _ in range(L):
    change_direction.append(list(input().strip().split()))
change_directions = deque(sorted(change_direction,key=lambda x: int(x[0])))


board = [[0] * N for _ in range(N)]
for apple in apples:
    row, col = apple
    board[row-1][col-1] = 'A'
print(solution(board))