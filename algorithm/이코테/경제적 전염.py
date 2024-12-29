"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3
"""
import sys
import heapq
input = sys.stdin.readline
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(queue, S, X, Y):

    for _ in range(S):
        temp = []
        while queue:
            virus, x, y = heapq.heappop(queue)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and lab[nx][ny] == 0:
                    lab[nx][ny] = virus
                    temp.append([virus, nx, ny])
        #     for l in lab:
        #         print(l)
        #     print()
        # print(temp)
        for virus, x, y in temp:
            heapq.heappush(queue, (virus, x, y))

    return lab[X-1][Y-1]



N, K = map(int, input().strip().split())
lab = []
for _ in range(N):
    lab.append(list(map(int, input().strip().split())))
S, X, Y = map(int, input().strip().split())

queue = []

for i in range(N):
    for j in range(N):
        if lab[i][j] != 0:
            heapq.heappush(queue, (lab[i][j], i, j))
print(solution(queue, S, X, Y))