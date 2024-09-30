import math

number_of_child, subin_location = map(int, input().split())

location_list = list(map(int,input().split()))
location_diff = []
for i in range(number_of_child):
  location_diff.append(abs(subin_location - location_list[i]))

print(math.gcd(*location_diff))