import sys

input = sys.stdin.readline

# CCTV 감시 방향 (순서: 우, 좌, 하, 상)
directions = [
    [],
    [[(0, 1)], [(0, -1)], [(1, 0)], [(-1, 0)]],  # CCTV 1 (→, ←, ↓, ↑)
    [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],  # CCTV 2 (↔, ↕)
    [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(0, -1), (-1, 0)], [(0, -1), (1, 0)]],  # CCTV 3 (ㄱ)
    [[(-1, 0), (0, 1), (1, 0)], [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)], [(0, -1), (-1, 0), (0, 1)]],  # CCTV 4
    [[(-1, 0), (0, 1), (1, 0), (0, -1)]]  # CCTV 5 (+)
]

# 입력 받기
N, M = map(int, input().split())
MAP = []
cctvs = []
for i in range(N):
    row = list(map(int, input().split()))
    MAP.append(row)
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j], i, j))  # (CCTV 유형, 행, 열)

# 최소 사각지대
min_blind_spots = float('inf')

# CCTV 감시 영역 표시
def watch(temp_map, x, y, dirs):
    marked = []  # 백트래킹을 위한 복구 리스트

    for dx, dy in dirs:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not (0 <= nx < N and 0 <= ny < M) or temp_map[nx][ny] == 6:  # 범위 초과 또는 벽이면 종료
                break
            if temp_map[nx][ny] == 0:
                temp_map[nx][ny] = -1  # 감시 지역 표시
                marked.append((nx, ny))  # 원복을 위해 저장

    return marked  # 감시한 좌표 반환 (백트래킹에서 원복하기 위해)

# 백트래킹 (DFS)
def dfs(idx):
    global min_blind_spots

    if idx == len(cctvs):  # 모든 CCTV 배치가 끝나면 사각지대 계산
        count = sum(row.count(0) for row in MAP)
        min_blind_spots = min(min_blind_spots, count)
        return

    cctv_type, x, y = cctvs[idx]

    for i in range(len(directions[cctv_type])):  # CCTV 회전 방향 탐색
        marked = watch(MAP, x, y, directions[cctv_type][i])  # CCTV 감시 표시
        dfs(idx + 1)  # 다음 CCTV 탐색

        # 백트래킹 (감시 지역 원복)
        for nx, ny in marked:
            if MAP[nx][ny] == -1:  # 원래 0이었던 곳만 원복
                MAP[nx][ny] = 0

# 실행
dfs(0)
print(min_blind_spots)