"""
0
1
3
2
:
-
- -
- -   - -         - -   - -
- -   - -
"""
import sys
input = sys.stdin.readline

def solution(n):
    if n == 0:
        return "-"

    prev= solution(n - 1)
    blank = " " * (3 ** (n-1))

    return prev + blank + prev

while True:
    try:
        N = int(input())
        print(solution(N))
    except:
        break