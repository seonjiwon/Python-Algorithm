"""
3 3
0 0 0
1 0 0
0 1 1
1 1 1
1 1 0
1 0 1

3 2
1 1 0
1 1 0
1 1 1
0 1
0 1
"""
import sys

input = sys.stdin.readline


def rotate(key):
    M = len(key)
    rotate_key = [[0] * (M) for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotate_key[i][j] = key[M - j - 1][i]
    return rotate_key


def solution(key, lock):
    M, N = len(key), len(lock)
    answer = False

    for _ in range(4):
        key = rotate(key)

        for start_x in range(N + M):  # 1부터가 아닌 0부터 시작
            for start_y in range(N + M):
                match = True
                expansion_lock = [[0] * (N + 2 * M) for _ in range(N + 2 * M)]

                for i in range(N):
                    for j in range(N):
                        expansion_lock[i + M][j + M] = lock[i][j]

                for i in range(M):
                    for j in range(M):
                        if key[i][j] == 1:
                            if expansion_lock[start_x + i][start_y + j] == 1:
                                expansion_lock[start_x + i][start_y + j] = 0
                                break
                            else:
                                expansion_lock[start_x + i][start_y + j] = 1

                for i in range(M, M + N):
                    for j in range(M, M + N):
                        if expansion_lock[i][j] != 1:
                            match = False
                            break
                if match:
                    answer = True
                    return answer  # match가 True면 바로 반환

    return answer


N, M = map(int, input().strip().split())
key = []
lock = []
for _ in range(N):
    key.append(list(map(int, input().strip().split())))
for _ in range(M):
    lock.append(list(map(int, input().strip().split())))

print(solution(key, lock))
