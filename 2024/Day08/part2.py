from itertools import combinations

with open("2024/Day08/input.txt", "r") as f:
    grid = f.read().splitlines()

n = len(grid)
m = len(grid[0])

ant = {}
for i in range(n):
    for j in range(m):
        freq = grid[i][j]
        if freq == ".":
            continue
        if freq not in ant:
            ant[freq] = []
        ant[freq].append((i, j))

anti = [[False] * m for _ in range(n)]
ans = 0
for freq, locs in ant.items():
    for (a, b), (c, d) in combinations(locs, 2):
        dx, dy = c - a, d - b
        e, f = a, b
        while 0 <= e < n and 0 <= f < m:
            if not anti[e][f]:
                anti[e][f] = True
                ans += 1
            e, f = e - dx, f - dy
        e, f = c, d
        while 0 <= e < n and 0 <= f < m:
            if not anti[e][f]:
                anti[e][f] = True
                ans += 1
            e, f = e + dx, f + dy

print(ans)
