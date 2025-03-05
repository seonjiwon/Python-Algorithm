import sys
input = sys.stdin.readline

def moo(n, k, l):
    if n <= 3:
        return "moo"[n-1]

    new_k = l * 2 + k + 3

    if new_k < n:
        return moo(n, k+1, new_k)
    else:
        if l < n <= l + k + 3:
            if n - l == 1:
                return "m"
            else:
                return "o"
        else:
            return moo(n - (l + k + 3), 1, 3)

N = int(input())
print(moo(N, 1, 3))