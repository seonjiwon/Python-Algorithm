"""
2 20 50
50 30
20 40

1
"""
import sys
from collections import deque
input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution():
    answer = 0


    while True:
        is_changed = False
        visited = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    queue = deque([(i, j)])
                    union = [(i, j)]
                    population = countries[i][j]
                    visited[i][j] = True

                    while queue:
                        x, y = queue.popleft()
                        for dx, dy in direction:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                                if L <= abs(countries[x][y] - countries[nx][ny]) <= R:
                                    is_changed = True
                                    union.append((nx, ny))
                                    queue.append((nx, ny))
                                    population += countries[nx][ny]
                                    visited[nx][ny] = True

                    population = population // len(union)
                    while union:
                        x, y = union.pop()
                        countries[x][y] = population
        # for c in countries:
        #     print(c)
        # print()
        if is_changed:
            answer += 1
        else:
            break

    return answer


countries = []
N, L, R = map(int, input().strip().split())
for _ in range(N):
    countries.append(list(map(int, input().strip().split())))
print(solution())