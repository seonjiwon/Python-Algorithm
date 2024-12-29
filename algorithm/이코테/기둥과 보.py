"""
input:
5
[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
5
[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
"""
import sys
from ast import literal_eval
input = sys.stdin.readline

def can_build(x, y, a, n, structure):
    if a == 0:  # 기둥
        # 바닥 위
        if y == 0 or [x-1, y, 1] in structure or [x, y, 1] in structure or [x, y-1, 0] in structure:
            return True
        return False
    else:  # 보
        # 한쪽 끝이 기둥 위
        if [x, y-1, 0] in structure or [x+1, y-1, 0] in structure or [x-1, y, 1] in structure and [x+1, y, 1] in structure:
            return True
        return False

def can_delete(x, y, a, structure):
    # 일단 삭제
    structure.remove([x, y, a])

    # 남은 구조물들이 조건을 만족하는지 확인
    for frame in structure:
        if not can_build(frame[0], frame[1], frame[2], len(structure), structure):
            structure.append([x, y, a])
            return False

    # 다시 추가
    structure.append([x, y, a])
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame

        if b == 1:  # 설치
            answer.append([x, y, a])
            if not can_build(x, y, a, n, answer):
                answer.remove([x, y, a])
        else:  # 삭제
            if can_delete(x, y, a, answer):
                answer.remove([x, y, a])

    return sorted(answer)

N = int(input())
build_frame = result = literal_eval(input())
print(solution(N, build_frame))