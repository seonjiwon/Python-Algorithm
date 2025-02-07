import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def spread_virus(lab, virus):
    queue = deque(virus)
    visited = [[-1] * N for _ in range(N)]

    for x, y in virus:
        visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and lab[nx][ny] != 1:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


    return visited


def calculate_time(lab, visited):
    max_time = 0
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 0:
                if visited[i][j] == -1:
                    return float('inf')
                max_time = max(max_time, visited[i][j])
    return max_time


N, M = map(int, input().strip().split())
#0 -> 빈칸, 1 -> 벽, 2 -> 바이러스
lab = [list(map(int, input().strip().split())) for _ in range(N)]
virus_coordinates = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus_coordinates.append((i, j))

least_time = float('inf')
for virus in combinations(virus_coordinates, M):
    visited = spread_virus(lab, virus)
    time = calculate_time(lab, visited)
    least_time = min(least_time, time)

if least_time == float('inf'):
    print(-1)
else:
    print(least_time)
