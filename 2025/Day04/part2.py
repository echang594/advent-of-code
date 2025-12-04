from collections import deque

with open("2025/Day04/input.txt", "r") as f:
    grid = [list(l) for l in f.read().splitlines()]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n = len(grid)
neighbors = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j] != "@":
            continue
        for x, y in zip(dx, dy):
            a, b = i + x, j + y
            if a >= 0 and a < n and b >= 0 and b < n:
                neighbors[a][b] += 1

d = deque()
for i in range(n):
    for j in range(n):
        if grid[i][j] == "@" and neighbors[i][j] < 4:
            d.append((i, j))
            grid[i][j] = "."

ans = 0
while d:
    i, j = d.popleft()
    ans += 1
    for x, y in zip(dx, dy):
        a, b = i + x, j + y
        if a >= 0 and a < n and b >= 0 and b < n:
            neighbors[a][b] -= 1
            if grid[a][b] == "@" and neighbors[a][b] < 4:
                d.append((a, b))
                grid[a][b] = "."

print(ans)
