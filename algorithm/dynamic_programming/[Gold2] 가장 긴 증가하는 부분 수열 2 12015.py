"""
6
10 20 10 30 20 50
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

def solution():
    LIS = [sequence[0]]

    for s in sequence:
        if LIS[-1] < s:
            LIS.append(s)
        else:
            idx = bisect_left(LIS, s)
            LIS[idx] = s
    return len(LIS)

A = int(input())
sequence = list(map(int, input().strip().split()))
print(solution())