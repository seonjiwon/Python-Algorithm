"""
3
3 3 0 1
4 2 1 3
4 2 2 1
: 4

"""
import sys
input = sys.stdin.readline

#동(0), 북(1), 서(2), 남(3)
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def dragon_curve(x, y, d, g):
    curve = [d]


    for _ in range(g):
        temp = []
        #현재 까지의 모든 방문을 역순으로 확인
        for i in range(len(curve) - 1, -1, -1):
            #다음 방향 = (현재 방향 + 1) % 4
            next_d = (curve[i] + 1) % 4
            temp.append(next_d)
        curve.extend(temp)

    coordinates[y][x] = 1

    #드래곤 커브의 모든 좌표를 표시
    nx, ny = x, y
    for d in curve:
        dx, dy = directions[d]
        nx += dx
        ny += dy
        if 0 <= nx < 101 and 0 <= ny < 101:
            coordinates[ny][nx] = 1


def count_square():
    answer = 0
    for i in range(100):
        for j in range(100):
            if coordinates[i][j] == 1 and coordinates[i+1][j] == 1 and coordinates[i][j+1] and coordinates[i+1][j+1] == 1:
                answer += 1
    return answer


N = int(input())
coordinates = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().strip().split())
    dragon_curve(x, y, d, g)

print(count_square())

