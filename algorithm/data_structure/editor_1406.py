import sys
word1 = list(sys.stdin.readline().strip())
word2 = []
n = int(sys.stdin.readline().strip())

for i in range(n):
  order = sys.stdin.readline().strip()
  if order == "L":
    if word1:
      word2.append(word1.pop())
  elif order == "D":
    if word2:
      word1.append(word2.pop())
  elif order == "B":
    if word1:
      word1.pop()
  elif order.startswith("P"):
    _, insert_word = order.split()
    word1.append(insert_word)

print(''.join(word1 + word2[::-1]))
