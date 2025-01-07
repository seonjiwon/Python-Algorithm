import sys
input = sys.stdin.readline

def is_possible(dist):
    count = 1
    current = houses[0]

    for i in range(1, N):
        if houses[i] - current >= dist:
            count += 1
            current = houses[i]
    return count >= C


def solution():
    result = 0
    start = 1
    end = houses[-1] - houses[0]

    while start <= end:
        mid = (end + start) // 2

        if is_possible(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result
    


N, C = map(int, input().strip().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
print(solution())