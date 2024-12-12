from itertools import pairwise

with open("2024/Day12/input.txt", "r") as f:
    plot = f.read().splitlines()

n = len(plot)
vis = [[False] * n for _ in range(n)]
ds = ((-1, 0), (0, 1), (1, 0), (0, -1))


def in_plot(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y):
    global a, p
    vis[x][y] = True
    a += 1
    for i, (dx, dy) in enumerate(ds):
        nx, ny = x + dx, y + dy
        if not in_plot(nx, ny) or plot[nx][ny] != plot[x][y]:
            if i % 2 == 0:
                if x not in p[i]:
                    p[i][x] = []
                p[i][x].append(y)
            else:
                if y not in p[i]:
                    p[i][y] = []
                p[i][y].append(x)
        elif not vis[nx][ny]:
            dfs(nx, ny)


ans = 0
for i in range(n):
    for j in range(n):
        if not vis[i][j]:
            a = 0
            p = [{} for _ in range(4)]
            dfs(i, j)
            np = 0
            for d in p:
                for s in d:
                    np += 1
                    for b, c in pairwise(sorted(d[s])):
                        if c - b > 1:
                            np += 1
            ans += a * np

print(ans)
