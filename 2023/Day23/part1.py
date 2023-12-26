from collections import deque

SLOPE_DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
DIR_SLOPES = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}
SLOPES = "^v<>"
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open("2023/Day23/input.txt") as f:
    m = f.read().splitlines()

start = (0, 1)
visited = {}
neg_dist = {start: 0}
q = deque()
q.append(start)
while q:
    cur = q.popleft()
    r, c = cur
    if m[r][c] == ".":
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            new = (nr, nc)
            if (
                nr < 0
                or nr >= len(m)
                or nc < 0
                or nc >= len(m[0])
                or m[nr][nc] == "#"
                or new in visited
            ):
                continue
            visited[new] = True
            neg_dist[new] = neg_dist[cur] - 1
            q.append(new)
    else:
        dr, dc = SLOPE_DIRS[m[r][c]]
        nr, nc = r + dr, c + dc
        new = (nr, nc)
        for dr, dc in DIRS:
            mr, mc = nr + dr, nc + dc
            if m[mr][mc] in SLOPES and m[mr][mc] != DIR_SLOPES[dr, dc] and (mr, mc) not in visited:
                break
        else:
            visited[new] = True
            q.append(new)
        if new not in neg_dist or neg_dist[new] > neg_dist[cur] - 1:
            neg_dist[new] = neg_dist[cur] - 1

print(-neg_dist[len(m) - 1, len(m[0]) - 2])
