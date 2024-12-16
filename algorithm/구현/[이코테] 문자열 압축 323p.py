"""
aabbaccc -> 2a2ba3c = 7
ababcdcdababcdcd -> 2ababcdcd = 9
"""
import sys
input = sys.stdin.readline

# def solution(s):
#   answer = len(s)  # 압축하지 않은 문자열 길이로 초기화
#
#   # 1부터 문자열 길이의 절반까지 단위로 자르기 시도
#   for unit in range(1, len(s)//2 + 1):
#     compressed = ""
#     prev = s[0:unit]  # 이전 문자열
#     count = 1
#
#     # unit 크기만큼 문자열 비교
#     for i in range(unit, len(s), unit):
#       current = s[i:i+unit]
#       if prev == current:
#         count += 1
#       else:
#         if count > 1:
#           compressed += str(count)
#         compressed += prev
#         prev = current
#         count = 1
#
#     # 마지막 문자열 처리
#     if count > 1:
#       compressed += str(count)
#     compressed += prev
#
#     # 최소 길이 갱신
#     answer = min(answer, len(compressed))
#
#   return answer

def solution(s):
  answer = len(s)

  for unit in range(1, len(s)//2 + 1):
    compressed = ""
    prev = s[:unit]
    count = 1
    for i in range(unit, len(s), unit):
      current = s[i:i+unit]
      if prev == current:
        count += 1
      else:
        if count > 1:
          compressed += str(count)
        compressed += prev
        prev = current
        count = 1

    if count > 1:
      compressed += str(count)
    compressed += prev

    answer = min(answer, len(compressed))


  return answer


s = input()
print(solution(s))