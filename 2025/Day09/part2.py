import itertools
import collections

with open("2025/Day09/input.txt", "r") as f:
    locs = [tuple(int(x) for x in l.split(",")) for l in f.read().splitlines()]


xs = sorted(set(x for x, _ in locs))
ys = sorted(set(y for _, y in locs))
from_x = {x: i for i, x in enumerate(xs)}
from_y = {y: i for i, y in enumerate(ys)}
n = len(xs)
m = len(ys)
grid = [[False] * m for _ in range(n)]
for a, b in itertools.pairwise(locs + [locs[0]]):
    a = (from_x[a[0]], from_y[a[1]])
    b = (from_x[b[0]], from_y[b[1]])
    if a[0] == b[0]:
        c, d = min(a[1], b[1]), max(a[1], b[1])
        for i in range(c, d + 1):
            grid[a[0]][i] = True
    else:
        c, d = min(a[0], b[0]), max(a[0], b[0])
        for i in range(c, d + 1):
            grid[i][a[1]] = True

vis = collections.defaultdict(bool)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def is_outside(x, y):
    d = collections.deque()
    d.append((x, y))
    vis[(x, y)] = True
    res = False
    while d:
        x, y = d.popleft()
        if x < 0 or x >= n or y < 0 or y >= m:
            res = True
            continue
        if grid[x][y]:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if vis[(nx, ny)]:
                continue
            d.append((nx, ny))
            vis[(nx, ny)] = True
    return res


def mark(x, y):
    d = collections.deque()
    d.append((x, y))
    grid[x][y] = True
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if grid[nx][ny]:
                continue
            d.append((nx, ny))
            grid[nx][ny] = True


for i in range(1, n - 1):
    for j in range(1, m - 1):
        if not vis[(i, j)] and not is_outside(i, j):
            mark(i, j)


def rect(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


ans = 0
for a, b in itertools.combinations(locs, 2):
    a = (from_x[a[0]], from_y[a[1]])
    b = (from_x[b[0]], from_y[b[1]])
    c = (min(a[0], b[0]), min(a[1], b[1]))
    d = (max(a[0], b[0]), max(a[1], b[1]))
    if not grid[c[0]][c[1]] or not grid[c[0]][d[1]] or not grid[d[0]][c[1]] or not grid[d[0]][d[1]]:
        continue
    valid = True
    for i in range(c[1] + 1, d[1]):
        if not grid[c[0]][i] or not grid[d[0]][i]:
            valid = False
            break
    if not valid:
        continue
    for i in range(c[0] + 1, d[0]):
        if not grid[i][c[1]] or not grid[i][d[1]]:
            valid = False
            break
    if not valid:
        continue
    a = (xs[a[0]], ys[a[1]])
    b = (xs[b[0]], ys[b[1]])
    ans = max(ans, rect(a, b))

print(ans)
