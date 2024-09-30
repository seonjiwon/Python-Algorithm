words = input()
rot_word = ""
for s in words:
  if ord('a') <= ord(s) <= ord('z') or ord('A') <= ord(s) <= ord('Z'):
    if ord('a') <= ord(s) <= ord('z'):
      rot_word += chr((((ord(s) + 13) - ord('a')) % 26) + ord('a'))
    else:
      rot_word += chr((((ord(s) + 13) - ord('A')) % 26) + ord('A'))
  else:
    rot_word += s
print(rot_word)