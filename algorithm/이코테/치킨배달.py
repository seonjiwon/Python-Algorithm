"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5
"""

import sys
from itertools import combinations
input = sys.stdin.readline

def find_coordinates(type):
    coordinates = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == type:
                coordinates.append([i+1, j+1])
    return coordinates


def solution():
    houses = find_coordinates(1)
    chickens = find_coordinates(2)
    answer = float('inf')

    for chosen_chickens in combinations(chickens, M):
        total_distance = 0
        for r1, c1 in houses:
            length = float('inf')
            for r2, c2 in chosen_chickens:
                temp = abs(r1-r2) + abs(c1-c2)
                length = min(length, temp)
            total_distance += length
        answer = min(answer, total_distance)
    return answer


N, M = map(int, input().strip().split())
MAP = [list(map(int, input().strip().split())) for _ in range(N)]
print(solution())
