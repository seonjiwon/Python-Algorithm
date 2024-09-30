def mod_exp(A, B, C):
  # Base case
  if B == 0:
    return 1
  # 분할 정복
  half = mod_exp(A, B // 2, C)
  half = (half * half) % C
  if B % 2 == 0:
    return half
  else:
    return (half * A) % C

# 입력 처리
A, B, C = map(int, input().split())

# 결과 출력
print(mod_exp(A, B, C))