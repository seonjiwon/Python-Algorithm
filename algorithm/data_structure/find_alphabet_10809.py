word = input()
alphabet_list = [-1 for i in range(ord('z') - ord('a') + 1)]

for i in range(len(word)):
  if alphabet_list[ord(word[i]) - ord('a')] == -1:
    alphabet_list[ord(word[i]) - ord('a')] = i
print(' '.join(map(str, alphabet_list)))