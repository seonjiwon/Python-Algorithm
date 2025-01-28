"""
위상 정렬 문제
log(V+E)
"""
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    result = []
    q = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        n = q.popleft()
        result.append(n)
        for g in graph[n]:
            in_degree[g] -= 1
            if in_degree[g] == 0:
                q.append(g)


    return result

N, M = map(int, input().strip().split())
in_degree = [0] * (N+1)

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    in_degree[b] += 1

result = topology_sort()
print(*result)

