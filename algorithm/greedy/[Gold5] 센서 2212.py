import sys
import heapq
input = sys.stdin.readline

def solution():
    answer = 0
    length = []
    if len(sensor) == 1:
        return 0

    for i in range(1, N):
        heapq.heappush(length, -(sensor[i] - sensor[i-1]))

    for _ in range(K-1):
        heapq.heappop(length)

    for i in length:
        answer -= i

    return answer


N = int(input())
K = int(input())
sensor = list(map(int, input().strip().split()))

sensor.sort()
print(solution())