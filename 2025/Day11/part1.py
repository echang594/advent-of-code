import collections

with open("2025/Day11/input.txt", "r") as f:
    lines = f.read().splitlines()

d = {}
n = len(lines) + 1
adj = [[] for _ in range(n)]
indeg = [0] * n
for l in lines:
    u, vs = l.split(":")
    vs = vs.split()
    if u not in d:
        d[u] = len(d)
    for v in vs:
        if v not in d:
            d[v] = len(d)
        adj[d[u]].append(d[v])
        indeg[d[v]] += 1

q = collections.deque()
paths = [0] * n
paths[d["you"]] = 1
for i in range(n):
    if indeg[i] == 0:
        q.append(i)

while q:
    u = q.popleft()
    for v in adj[u]:
        paths[v] += paths[u]
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

ans = paths[d["out"]]
print(ans)
