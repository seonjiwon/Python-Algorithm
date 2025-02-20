"""
mirkovC4nizCC44
C4
: mirkovniz

12ab112ab2ab
12ab
:FRULA
"""
import sys
input = sys.stdin.readline

def solution(str):
    bomb_len = len(bomb)

    stack = []

    for i in range(len(str)):
        stack.append(str[i])
        if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb:
            for _ in range(bomb_len):
                stack.pop()

    return ''.join(stack) if len(stack) != 0 else "FRULA"


str = input().strip()
bomb = input().strip()

print(solution(str))