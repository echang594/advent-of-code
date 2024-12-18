with open("2024/Day18/input.txt", "r") as f:
    blocks = f.read().splitlines()

blocks = [tuple(int(x) for x in block.split(",")) for block in blocks]
N = 71
blocked = [[False] * N for _ in range(N)]
for x, y in blocks:
    blocked[x][y] = True
p = [[None] * N for _ in range(N)]
s = [[1] * N for _ in range(N)]
ds = ((-1, 0), (0, 1), (1, 0), (0, -1))


def dfs(x, y, np):
    p[x][y] = np
    s[np[0]][np[1]] += 1
    for dx, dy in ds:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not blocked[nx][ny] and p[nx][ny] is None:
            dfs(nx, ny, np)


for i in range(N):
    for j in range(N):
        if p[i][j] is None:
            dfs(i, j, (i, j))


def find(v):
    x, y = v
    if v == p[x][y]:
        return v
    p[x][y] = find(p[x][y])
    return p[x][y]


def union(a, b):
    a = find(a)
    b = find(b)
    x, y = a
    w, z = b
    if a != b:
        if s[x][y] < s[w][z]:
            a, b, x, y, w, z = b, a, w, z, x, y
        p[w][z] = a
        s[x][y] += s[w][z]


for b in reversed(blocks):
    x, y = b
    blocked[x][y] = False
    for dx, dy in ds:
        nx, ny = x + dx, y + dy
        v = (nx, ny)
        if 0 <= nx < N and 0 <= ny < N and not blocked[nx][ny]:
            union(b, v)
    if find((0, 0)) == find((N - 1, N - 1)):
        ans = b
        break

print(",".join(str(x) for x in ans))
