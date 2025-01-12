import sys
input = sys.stdin.readline

def solution(numbers):
    answer = 0
    even_numbers = []
    odd_numbers = []
    for n in numbers:
        if n > 0:
            even_numbers.append(n)
        else:
            odd_numbers.append(n)
    odd_numbers.reverse()

    while even_numbers:
        if len(even_numbers) > 1:
            n1 = even_numbers.pop()
            n2 = even_numbers.pop()
            if n1 + n2 > n1 * n2:
                answer += (n1 + n2)
            else:
                answer += (n1 * n2)
        else:
            answer += even_numbers.pop()

    while odd_numbers:
        if len(odd_numbers) > 1:
            n1 = odd_numbers.pop()
            n2 = odd_numbers.pop()
            if n1 + n2 > n1 * n2:
                answer += (n1 + n2)
            else:
                answer += (n1 * n2)
        else:
            answer += odd_numbers.pop()
    return answer

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
print(solution(numbers))