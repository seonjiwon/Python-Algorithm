import sys

def bellman_ford(start):
  distance = [10001] * (N + 1)
  distance[start] = 0

  for i in range(N):
    for s in range(1, N+1):
      for v, w in load[s]:
        if distance[v] > distance[s] + w:
          distance[v] = distance[s] + w
          if i == N-1:
            return True

  return False


TC = int(sys.stdin.readline())
for _ in range(TC):
  N, M, W = map(int, sys.stdin.readline().strip().split())
  load = [[] for _ in range(N+1)]
  for _ in range(M):
    S, E, T = map(int, sys.stdin.readline().strip().split())
    load[S].append((E, T))
    load[E].append((S, T))
  for _ in range(W):
    S, E, T = map(int, sys.stdin.readline().strip().split())
    load[S].append((E, -T))


  if bellman_ford(1):
    print("YES")
  else:
    print("NO")
