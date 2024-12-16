import sys
input = sys.stdin.readline

def is_possible(dist):
  count = 1 # 공유기의 갯수 1개는 무조건 설치
  current = houses[0] # 현재 설치한 공유기의 위치

  for i in range(1, N):
    if houses[i] - current >= dist: # 설치하고자 하는 위치 - 현재위치 > mid의 거리
      count += 1 # 설치하겠다
      current = houses[i] # 현재위치 변경

  return count >= C # 설치 하고자 하는 공유기의 수보다 크면 true

def solution():
  result = 0
  start = 1 # 최소 거리
  end = houses[-1] - houses[0] # 최대 거리

  while start <= end:
    mid = (start + end) // 2

    if is_possible(mid): # 공유기의 설치가 mid 의 거리로 가능 하다면
      result = mid
      start = mid + 1 # 더 큰 거리의 탐색
    else:
      end = mid - 1 # 더 작은 거리의 탐색

  return result

N, C = map(int, input().split())
houses = []
for _ in range(N):
  houses.append(int(input()))
houses.sort()

print(solution())