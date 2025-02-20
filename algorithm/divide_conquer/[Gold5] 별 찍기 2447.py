import sys
input = sys.stdin.readline

def draw_star(n):
    if n == 1:
        return ["*"]

    stars = draw_star(n // 3)
    new_pattern = []

    for star in stars:
        new_pattern.append(star * 3)
    for star in stars:
        new_pattern.append(star + " " * (n // 3) + star)
    for star in stars:
        new_pattern.append(star * 3)

    return new_pattern


N = int(input().strip())
print("\n".join(draw_star(N)))
