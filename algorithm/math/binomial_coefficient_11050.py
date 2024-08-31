import math
import sys

N, K = map(int, sys.stdin.readline().strip().split())
print(math.factorial(N) // math.factorial(N-K) // math.factorial(K))