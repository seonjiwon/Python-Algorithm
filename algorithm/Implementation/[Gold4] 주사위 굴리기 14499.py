"""
4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2
:
0
0
3
0
0
8
6
3
"""
import sys
input = sys.stdin.readline
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def roll_dice(dice, x, y):

    for c in cmd:
        dx, dy = direction[c-1]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        dice = rotate_dice(c, dice)

        print(dice[3])

        if MAP[nx][ny] == 0:
            MAP[nx][ny] = dice[0]
        else:
            dice[0] = MAP[nx][ny]
            MAP[nx][ny] = 0
        x, y = nx, ny


def rotate_dice(c, dice):
    # 주사위 굴리기
    if c == 1:
        dice = [dice[5], dice[1], dice[2], dice[4], dice[0], dice[3]]
    elif c == 2:
        dice = [dice[4], dice[1], dice[2], dice[5], dice[3], dice[0]]
    elif c == 3:
        dice = [dice[2], dice[0], dice[3], dice[1], dice[4], dice[5]]
    elif c == 4:
        dice = [dice[1], dice[3], dice[0], dice[2], dice[4], dice[5]]
    return dice


N, M, x, y, K = map(int, input().strip().split())
MAP = []
dice = [0] * 6
for i in range(N):
    MAP.append(list(map(int, input().strip().split())))

cmd = list(map(int, input().strip().split()))

roll_dice(dice, x, y)