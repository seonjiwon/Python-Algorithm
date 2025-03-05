import sys
from collections import deque

input = sys.stdin.readline

def shifting(idx, direction):
    queue = [(idx, direction)]
    visited[idx] = direction

    while queue:
        cur, dir = queue.pop()

        if cur > 0 and visited[cur - 1] == 0 and cogwheels[cur - 1][2] != cogwheels[cur][6]:
            visited[cur - 1] = -dir  # 반대 방향으로 회전
            queue.append((cur - 1, -dir))

        # 오른쪽 검사
        if cur < 3 and visited[cur + 1] == 0 and cogwheels[cur][2] != cogwheels[cur + 1][6]:
            visited[cur + 1] = -dir  # 반대 방향으로 회전
            queue.append((cur + 1, -dir))

    # 회전 적용 (BFS 결과 반영)
    for i in range(4):
        if visited[i] != 0:
            cogwheels[i].rotate(visited[i])


# 입력 받기
cogwheels = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())

for _ in range(K):
    idx, direction = map(int, input().split())
    visited = [0] * 4  # 방문 여부 초기화
    shifting(idx - 1, direction)

# 점수 계산
result = sum((cogwheels[i][0] * (2 ** i)) for i in range(4))
print(result)