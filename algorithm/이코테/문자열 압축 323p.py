"""
aabbaccc -> 2a2ba3c = 7
ababcdcdababcdcd -> 2ababcdcd = 9
"""
import sys
input = sys.stdin.readline

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