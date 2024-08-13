def backtrack():
  if len(answer) == M:
    print(' '.join(map(str, answer)))
    return

  previous = 0
  for i in range(N):
    if not visited[i] and previous != numbers[i]:
      visited[i] = 1
      answer.append(numbers[i])
      previous = numbers[i]
      backtrack()
      visited[i] = 0
      answer.pop()

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = [0] * N
answer = []

backtrack()