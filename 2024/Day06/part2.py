with open("2024/Day06/input.txt", "r") as f:
    grid = f.read().splitlines()

n = len(grid)
m = len(grid[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
move = [[[(-1, -1) for _ in range(4)] for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            start = (i, j)
        elif grid[i][j] == "#":
            for k in range(4):
                x, y = ox, oy = i + dirs[k][0], j + dirs[k][1]
                while 0 <= x < n and 0 <= y < m and grid[x][y] != "#":
                    move[x][y][k ^ 2] = ox, oy
                    x, y = x + dirs[k][0], y + dirs[k][1]

ans = 0
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = True
cur = start
d = 0
while True:
    nxt = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
    if nxt[0] < 0 or nxt[0] >= n or nxt[1] < 0 or nxt[1] >= m:
        break
    if grid[nxt[0]][nxt[1]] == "#":
        d = (d + 1) % 4
        continue
    if visited[nxt[0]][nxt[1]]:
        cur = nxt
        continue
    temp = {}
    for k in range(4):
        x, y = ox, oy = nxt[0] + dirs[k][0], nxt[1] + dirs[k][1]
        while 0 <= x < n and 0 <= y < m and grid[x][y] != "#":
            temp[(x, y, k ^ 2)] = ox, oy
            x, y = x + dirs[k][0], y + dirs[k][1]
    i, j = cur
    nd = (d + 1) % 4
    vis = set(((i, j, nd),))
    while i != -1:
        if (i, j, nd) in temp:
            i, j = temp[(i, j, nd)]
        else:
            i, j = move[i][j][nd]
        nd = (nd + 1) % 4
        if (i, j, nd) in vis:
            ans += 1
            break
        vis.add((i, j, nd))
    visited[nxt[0]][nxt[1]] = True
    cur = nxt

print(ans)
