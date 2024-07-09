from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
  command = sys.stdin.readline().strip()
  if command.startswith("push_front"):
    _, insert_word = command.split()
    queue.appendleft(insert_word)
  elif command.startswith("push_back"):
    _, insert_word = command.split()
    queue.append(insert_word)
  elif command == "pop_front":
    if queue:
      print(queue.popleft())
    else:
      print(-1)
  elif command == "pop_back":
    if queue:
      print(queue.pop())
    else:
      print(-1)
  elif command == "size":
    print(len(queue))
  elif command == "empty":
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif command == "front":
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif command == "back":
    if queue:
      print(queue[-1])
    else:
      print(-1)
