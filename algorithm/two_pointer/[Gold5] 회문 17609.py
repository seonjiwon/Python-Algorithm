import sys
input = sys.stdin.readline

def is_palindrome(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True

def solution(word):
    left = 0
    right = len(word)-1


    while left < right:
        if word[left] != word[right]:
            if is_palindrome(word, left + 1, right) or is_palindrome(word, left, right - 1):
                return 1
            else:
                return 2
        left += 1
        right -= 1

    return 0


T = int(input())
for _ in range(T):
    word = list(input().strip())
    print(solution(word))