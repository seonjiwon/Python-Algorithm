import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
student = []

for i in range(N):
  student.append((i, 3))


for _ in range(M):
  command = input().strip().split()
  cmd = command[0]

  if cmd == "SET":
    ID, Y = int(command[1]), int(command[2])
    student[ID-1] = (ID, Y)

  elif cmd == "ADD":
    Y, Z = int(command[1]), int(command[2])
    for s in range(N):
      ID, SCORE = student[s][0], student[s][1]
      if SCORE == Y:
        if Y + Z >= 4:
          student[ID-1] = (ID, 4)
        elif Y + Z <= 0:
          student[ID-1] = (ID, 0)
        else:
          student[ID-1] = (ID, SCORE + Z)

  elif cmd == "PRN":
    ID = int(command[1])
    score = student[ID-1][1]
    if score == 0:
      print("F")
    elif score == 1:
      print("D")
    elif score == 2:
      print("C")
    elif score == 3:
      print("B")
    elif score == 4:
      print("A")

  elif cmd == "CNT":
    result = 0
    Y = int(command[1])
    for s in range(N):
      ID, SCORE = student[s][0], student[s][1]
      if SCORE == Y:
        result += 1
    print(result)


