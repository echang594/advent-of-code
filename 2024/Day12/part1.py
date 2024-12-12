with open("2024/Day12/input.txt", "r") as f:
    plot = f.read().splitlines()

n = len(plot)
m = len(plot[0])
vis = [[False] * m for _ in range(n)]
ds = ((-1, 0), (0, 1), (1, 0), (0, -1))


def in_plot(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y):
    global a, p
    vis[x][y] = True
    a += 1
    for dx, dy in ds:
        nx, ny = x + dx, y + dy
        if not in_plot(nx, ny) or plot[nx][ny] != plot[x][y]:
            p += 1
        elif not vis[nx][ny]:
            dfs(nx, ny)


ans = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            a = 0
            p = 0
            dfs(i, j)
            ans += a * p

print(ans)
