import sys
input = sys.stdin.readline

def solution():
  left_hill = []
  result = 0

  for i in range(N):
    is_break = False
    for number in hills[i]:
      if number in left_hill:
        is_break = True
    if not is_break:
      result += 1
      left_hill += hills[i]
    # print(left_hill)

  return result



N = int(input())

hills = []
for _ in range(N):
  hills.append(list(map(int, input().strip().split())))

print(solution())