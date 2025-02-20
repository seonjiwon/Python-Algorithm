"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""

import sys
input = sys.stdin.readline

def solution(str):
    answer = "YES"
    stack = []

    for i in str:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if len(stack) >= 1:
                stack.pop()
            else:
                answer = "NO"
                break


    return answer if len(stack) == 0 else "NO"


N = int(input())
for _ in range(N):
    INPUT = list(input())
    print(solution(INPUT))