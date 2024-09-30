words = input()

alphabet_list = [0 for i in range(ord('z') - ord('a') + 1)]
for s in words:
  alphabet_list[ord(s) - ord('a')] += 1
print(' '.join(map(str, alphabet_list)))