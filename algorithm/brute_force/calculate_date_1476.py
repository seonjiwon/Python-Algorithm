import sys

def calculate_date(e, s, m):
  x, y, z = 0, 0, 0
  while True:
    ee = e + (15 * x)
    ss = s + (28 * y)
    mm = m + (19 * z)
    if ee == ss == mm:
      return ee
    if ee <= ss and ee <= mm:
      x += 1
    elif ss <= ee and ss <= mm:
      y += 1
    elif mm <= ee and mm <= ss:
      z += 1


e, s, m = map(int, sys.stdin.readline().strip().split())
print(calculate_date(e, s, m))