import sys
input = sys.stdin.readline

def solution():
    result = [0] * 3

    closest_zero = float('inf')

    for i in range(N-2):
        fixed = liquid[i]
        left, right = i+1, N-1
        while left < right:
            SUM = fixed + liquid[left] + liquid[right]
            if abs(closest_zero) > abs(SUM):
                closest_zero = SUM
                result[0], result[1], result[2] = fixed, liquid[left], liquid[right],

            if SUM > 0:
                right -= 1
            else:
                left += 1

    return result

N = int(input())
liquid = list(map(int, input().strip().split()))
liquid.sort()
# print(liquid)
print(*solution())