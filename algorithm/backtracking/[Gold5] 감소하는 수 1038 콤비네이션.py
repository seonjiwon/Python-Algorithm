import sys
import itertools
input = sys.stdin.readline

def solution():
    result = []
    for i in range(1, 11):
        for temp in itertools.combinations(range(10), i):
            temp = list(temp)
            temp.sort(reverse=True)
            result.append(int(''.join(map(str, temp))))
    return result



N = int(input())
result = solution()
result.sort()
try:
    print(result[N])
except:
    print(-1)
