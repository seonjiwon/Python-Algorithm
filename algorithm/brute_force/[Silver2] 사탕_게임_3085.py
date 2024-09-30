import sys

def candy_crush(n, candies):

  def check_max_candies(candies, x, y):
    max_candies = 1

    row_count = 1
    for j in range(1, n):
      if candies[x][j] == candies[x][j-1]:
        row_count += 1
      else:
        max_candies = max(max_candies, row_count)
        row_count = 1
      max_candies = max(max_candies, row_count)

    col_count = 1
    for i in range(1, n):
      if candies[i][y] == candies[i-1][y]:
        col_count += 1
      else:
        max_candies = max(max_candies, col_count)
        col_count = 1
      max_candies = max(max_candies, col_count)
    return max_candies

  max_candies = 0
  for i in range(n):
    for j in range(n):
      if j+1 < n:
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
        max_candies = max(max_candies, check_max_candies(candies, i, j), check_max_candies(candies, i, j+1))
        candies[i][j], candies[i][j+1] = candies[i][j+1], candies[i][j]
      if i+1 < n:
        candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
        max_candies = max(max_candies, check_max_candies(candies, i, j), check_max_candies(candies, i+1, j))
        candies[i][j], candies[i+1][j] = candies[i+1][j], candies[i][j]
  return max_candies



n = int(sys.stdin.readline().strip())
candies = []
for i in range(n):
  candy = list(sys.stdin.readline().strip())
  candies.append(candy)
print(candy_crush(n, candies))