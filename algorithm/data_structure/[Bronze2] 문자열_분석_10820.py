
while True:
  try:
    anal_list = [0 for i in range(4)]
    string_list = list(input())
    for s in string_list:
      if s == ' ':
        anal_list[3] += 1
      elif ord('0') <= ord(s) <= ord('9'):
        anal_list[2] += 1
      elif ord('a') <= ord(s) <= ord('z'):
        anal_list[0] += 1
      else :
        anal_list[1] += 1
    print(' '.join(map(str, anal_list)))
  except:
    break
