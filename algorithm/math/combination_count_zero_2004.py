def count_zeros(n, m):
  def count_factors(num, factor):
    count = 0
    while num > 0:
      count += num//factor
      num //= factor
    return count
  twos_n = count_factors(n, 2)
  fives_n = count_factors(n, 5)

  twos_m = count_factors(m, 2)
  fives_m = count_factors(m, 5)

  twos_nm = count_factors(n-m, 2)
  fives_nm = count_factors(n-m, 5)

  twos = twos_n - (twos_m + twos_nm)
  fives = fives_n - (fives_m + fives_nm)

  return min(twos, fives)

n, m = map(int, input().split())
print(count_zeros(n, m))
