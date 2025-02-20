"""
5
4 1 5 2 3
5
1 3 7 9 5
"""

import sys
input = sys.stdin.readline


def solution(i):
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        # print(f"i = {i}, mid = {mid}")
        if N_list[mid] == i:
            return 1

        if N_list[mid] > i:
            right = mid - 1
        else:
            left = mid + 1
    return 0


N = int(input())
N_list = list(map(int, input().strip().split()))
N_list.sort()
M = int(input())
M_list = list(map(int,input().strip().split()))
for i in M_list:
    print(solution(i))