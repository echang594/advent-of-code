import numpy as np

with open("2024/Day13/input.txt", "r") as f:
    games = f.read().split("\n\n")

OFFSET = 10_000_000_000_000

ans = 0
for game in games:
    a, b, prize = game.strip().splitlines()
    c, d, e = a.split()[2:], b.split()[2:], prize.split()[1:]
    f, g, h, i = int(c[0][2:-1]), int(c[1][2:]), int(d[0][2:-1]), int(d[1][2:])
    j, k = int(e[0][2:-1]), int(e[1][2:])

    A = np.array([[f, h], [g, i]])
    b = np.array([OFFSET + j, OFFSET + k])
    x = np.linalg.solve(A, b).round().astype(int)
    if np.array_equal(np.dot(A, x), b):
        ans += 3 * x[0] + x[1]

print(ans)
