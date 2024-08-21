import sys

N = int(sys.stdin.readline())
char_dict = {}

for i in range(N):
  temp = list(sys.stdin.readline().strip())
  exponent = len(temp) - 1

  for j in range(exponent, -1, -1):
    ch = temp[exponent - j]
    if not ch in char_dict:
      char_dict[ch] = 10**j
    else:
      char_dict[ch] += 10**j


char_dict = dict(sorted(char_dict.items(), key=lambda x:x[1], reverse=True))
char_num = 9
answer = 0

for c in char_dict:
  answer += char_dict[c] * char_num
  char_num -= 1
print(answer)