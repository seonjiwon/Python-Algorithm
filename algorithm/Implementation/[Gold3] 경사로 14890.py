import sys
input = sys.stdin.readline

def can_build_slope(line, L):
    N = len(line)
    built = [False] * N  # 경사로가 놓였는지 체크

    for i in range(1, N):
        if abs(line[i] - line[i - 1]) > 1:  # 높이 차이가 1 초과 → 불가능
            return False

        # 높이가 올라가는 경우 (현재 칸이 이전 칸보다 1 높음)
        if line[i] == line[i - 1] + 1:
            # **경사로를 놓을 `L`개 칸이 연속적으로 존재하는지 먼저 확인**
            for j in range(1, L + 1):
                if i - j < 0 or line[i - j] != line[i - 1] or built[i - j]:
                    return False  # 설치 불가능하면 즉시 종료

            # 모든 조건을 통과한 경우에만 `built` 표시
            for j in range(1, L + 1):
                built[i - j] = True

                # 높이가 내려가는 경우 (현재 칸이 이전 칸보다 1 낮음)
        elif line[i] == line[i - 1] - 1:
            # **경사로를 놓을 `L`개 칸이 연속적으로 존재하는지 먼저 확인**
            for j in range(L):
                if i + j >= N or line[i + j] != line[i] or built[i + j]:
                    return False  # 설치 불가능하면 즉시 종료

            # 모든 조건을 통과한 경우에만 `built` 표시
            for j in range(L):
                built[i + j] = True

    return True

def solution():
    answer = 0

    # 행 검사
    for r in range(N):
        if can_build_slope(MAP[r], L):
            answer += 1

    # 열 검사 (세로 방향)
    for c in range(N):
        column = [MAP[r][c] for r in range(N)]  # 열 데이터 추출
        if can_build_slope(column, L):
            answer += 1

    return answer

N, L = map(int, input().strip().split())
MAP = [list(map(int, input().strip().split())) for _ in range(N)]
print(solution())