words = input()
list = []

for w in range(len(words)):
  list.append(words[w::])

list.sort()
print('\n'.join(list))