with open("2024/Day15/input.txt", "r") as f:
    grid, moves = f.read().split("\n\n")

grid = [[c for c in line] for line in grid.splitlines()]
moves = moves.replace("\n", "")
n = len(grid)

ds = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            x, y = i, j

grid[x][y] = "."

for move in moves:
    dx, dy = ds[move]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == ".":
        x, y = nx, ny
        continue
    if grid[nx][ny] == "#":
        continue
    while grid[nx][ny] == "O":
        nx, ny = nx + dx, ny + dy
    if grid[nx][ny] == "#":
        continue
    grid[nx][ny] = "O"
    x, y = x + dx, y + dy
    grid[x][y] = "."

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "O":
            ans += 100 * i + j

print(ans)
