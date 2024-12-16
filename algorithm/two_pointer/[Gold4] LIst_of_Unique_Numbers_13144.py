import sys
input = sys.stdin.readline

def solution():
  result = 0
  start= 0
  numbers = [0] * (100000+1)

  # end를 늘려가면서 연속된 부분 수열 찾기
  for end in range(N):
    # end 위치의 숫자가 이미 있다면
    while numbers[sequence[end]] > 0:
      # start를 이동시키면서 중복 제거
      numbers[sequence[start]] -= 1
      start += 1

    # end 위치의 숫자 추가
    numbers[sequence[end]] += 1
    # start부터 end까지의 가능한 부분 수열 개수 추가
    result += (end - start + 1)

  return result




N = int(input())
sequence = list(map(int, input().strip().split()))
print(solution())