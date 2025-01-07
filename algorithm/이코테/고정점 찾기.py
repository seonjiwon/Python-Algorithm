"""
5
-15 -6 1 3 7
-> 3

7
-15 -4 2 8 9 13 15
-> 2

7
-15 -4 3 8 9 13 15
-> -1
"""
import sys
from bisect import bisect_left
input = sys.stdin.readline

# def solution(nums):
#     answer = -1
#     for n in nums:
#         index = bisect_left(nums, n)
#         if index == n:
#             answer = n
#             break
#     return answer

def solution(nums):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == mid:
            return mid

        if nums[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return -1




N = int(input())
nums = list(map(int, input().strip().split()))
print(solution(nums))