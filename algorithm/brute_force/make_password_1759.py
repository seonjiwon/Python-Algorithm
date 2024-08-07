import sys

def dfs(depth, start):
  if depth == l:
    cnt = 0
    for j in vowel:
      cnt += arr.count(j)
    if 2 <= len(arr) - cnt and cnt >= 1:
      print(''.join(map(str, arr)))
    return

  for i in range(start, c):
    arr.append(alphabet_list[i])
    dfs(depth+1, i+1)
    arr.pop()


l, c = map(int, sys.stdin.readline().strip().split())
alphabet_list = list(sys.stdin.readline().strip().split())
vowel = ['a', 'e', 'i', 'o', 'u']
alphabet_list.sort()
arr = []
dfs(0, 0)