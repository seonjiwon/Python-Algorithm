import sys

word = list(sys.stdin.readline().strip())
result = []
i = 0

while i < len(word):
  temp_word = []
  if word[i] == '<':
    while i < len(word) and word[i] != '>':
      result.append(word[i])
      i += 1
    else:
      result.append(word[i])
      i += 1
  elif word[i] == ' ':
    while i < len(word) and word[i] == ' ':
      result.append(word[i])
      i += 1
  else:
    while i < len(word) and word[i] != ' ' and word[i] != '<':
      temp_word.append(word[i])
      i+=1
    else:
      for j in temp_word[::-1]:
        result.append(j)

print(''.join(result))
