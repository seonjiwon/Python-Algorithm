import sys

def dwarf_height(height):
  sum_height = sum(height)
  find_number = sum_height - 100
  fake = []
  for i in range(9):
    for j in range(i+1, 9):
      if height[i] + height[j] == find_number:
        fake.append(height[i])
        fake.append(height[j])
        break
  height.remove(fake[0])
  height.remove(fake[1])
  height.sort()
  return height




height = []
for i in range(9):
  n = int(sys.stdin.readline().strip())
  height.append(n)

h = dwarf_height(height)
for i in h:
  print(i)
