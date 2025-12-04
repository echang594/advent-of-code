with open("2025/Day04/input.txt", "r") as f:
    grid = f.read().splitlines()

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n = len(grid)

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] != "@":
            continue
        cnt = 0
        for x, y in zip(dx, dy):
            a, b = i + x, j + y
            if a >= 0 and a < n and b >= 0 and b < n and grid[a][b] == "@":
                cnt += 1
        if cnt < 4:
            ans += 1

print(ans)
