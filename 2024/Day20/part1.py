from queue import Queue

with open("2024/Day20/input.txt", "r") as f:
    grid = f.read().splitlines()

n = len(grid)
INF = 20000
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
dirs2 = ((-2, 0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -2), (-1, -1))

for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            s = (i, j)
        elif grid[i][j] == "E":
            e = (i, j)


def bfs(start):
    d = [[INF] * n for _ in range(n)]
    d[start[0]][start[1]] = 0
    q = Queue()
    q.put(start)
    while not q.empty():
        x, y = q.get()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != "#" and d[nx][ny] == INF:
                d[nx][ny] = d[x][y] + 1
                q.put((nx, ny))
    return d


ds = bfs(s)
de = bfs(e)
T = ds[e[0]][e[1]]


ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "#" or ds[i][j] + abs(i - e[0]) + abs(j - e[1]) > T - 100:
            continue
        for dx, dy in dirs2:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < n and grid[x][y] != "#":
                t = ds[i][j] + de[x][y] + 2
                saved = T - t
                if saved >= 100:
                    ans += 1

print(ans)
