import sys
input = sys.stdin.readline


def backtracking(n):
    numbers.append(n)

    last_number = n % 10
    for i in range(last_number):
        backtracking(n * 10 + i)



N = int(input())
numbers = []
for i in range(10):
    backtracking(i)
numbers.sort()
print(numbers[N] if N < len(numbers) else -1)