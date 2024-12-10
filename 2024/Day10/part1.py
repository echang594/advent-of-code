with open("2024/Day10/input.txt", "r") as f:
    grid = [[int(h) for h in line] for line in f.read().splitlines()]

n = len(grid)
m = len(grid[0])

d = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dfs(x, y):
    if grid[x][y] == 9:
        v.add((x, y))
        return
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[x][y] + 1:
            dfs(nx, ny)


ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            v = set()
            dfs(i, j)
            ans += len(v)

print(ans)
