from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open("2023/Day23/input.txt") as f:
    m = f.read().splitlines()

start, end = (0, 1), (len(m) - 1, len(m[0]) - 2)
visited = {}
nodes = {start: 0}
g = [[]]
q = deque()
q.append((start, 0, 0))
while q:
    cur, prev, dist = q.pop()
    r, c = cur
    if cur in nodes and nodes[cur] != prev:
        g[nodes[cur]].append((prev, dist))
        g[prev].append((nodes[cur], dist))
    if cur in visited:
        continue
    visited[cur] = True
    if cur == end:
        nodes[end] = len(nodes)
        g.append([(prev, dist)])
        g[prev].append((nodes[end], dist))
    new = []
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= len(m) or nc < 0 or nc >= len(m[0]) or m[nr][nc] == "#":
            continue
        new.append((nr, nc))
    if len(new) <= 2:
        for nr, nc in new:
            q.append(((nr, nc), prev, dist + 1))
        continue
    nodes[cur] = len(nodes)
    g.append([(prev, dist)])
    g[prev].append((nodes[cur], dist))
    for nr, nc in new:
        q.append(((nr, nc), nodes[cur], 1))


def longest_hike(u, dist):
    if u == len(g) - 1:
        return dist
    visited[u] = True
    mx = 0
    for v, d in g[u]:
        if not visited[v]:
            mx = max(mx, longest_hike(v, dist + d))
    visited[u] = False
    return mx


visited = [False] * len(g)
num_steps = longest_hike(0, 0)

print(num_steps)
