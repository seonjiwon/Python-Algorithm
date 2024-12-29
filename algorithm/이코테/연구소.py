"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27
"""

import sys
import itertools
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def spread_virus(lab, viruses):
    queue = deque(viruses)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y +dy
            if 0 <= nx < N and 0 <= ny < M and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx, ny))
    return lab

def get_safe_area(lab):
    result = 0

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                result += 1

    return result

N, M = map(int, input().strip().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, input().strip().split())))

blank = []
viruses = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            blank.append((i,j))
        if lab[i][j] == 2:
            viruses.append((i, j))

max_safe_area = 0
for combination in itertools.combinations(blank, 3):
    new_lab = deepcopy(lab)

    for r, c in combination:
        new_lab[r][c] = 1

    new_lab = spread_virus(new_lab, viruses)

    max_safe_area = max(max_safe_area, get_safe_area(new_lab))
print(max_safe_area)