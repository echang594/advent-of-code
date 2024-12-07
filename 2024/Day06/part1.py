with open("2024/Day06/input.txt", "r") as f:
    grid = f.read().splitlines()

n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            start = (i, j)
            break
    else:
        continue
    break

ans = 1
visited = [[False for _ in range(m)] for _ in range(n)]
visited[start[0]][start[1]] = True
cur = start
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d = 0
while True:
    nxt = (cur[0] + dirs[d][0], cur[1] + dirs[d][1])
    if nxt[0] < 0 or nxt[0] >= n or nxt[1] < 0 or nxt[1] >= m:
        break
    if grid[nxt[0]][nxt[1]] == "#":
        d = (d + 1) % len(dirs)
        continue
    if not visited[nxt[0]][nxt[1]]:
        visited[nxt[0]][nxt[1]] = True
        ans += 1
    cur = nxt

print(ans)
