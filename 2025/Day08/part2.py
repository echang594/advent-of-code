import itertools

with open("2025/Day08/input.txt", "r") as f:
    v = [tuple(int(x) for x in l.split(",")) for l in f.read().splitlines()]


def sq_dist(t):
    a, b = t
    return sum((c - d) ** 2 for c, d in zip(a, b))


d = {}
for i, u in enumerate(v):
    d[u] = i
e = sorted(itertools.combinations(v, 2), key=sq_dist)
p = list(range(len(v)))
sz = [1] * len(v)


def find(v):
    if v == p[v]:
        return v
    p[v] = find(p[v])
    return p[v]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if sz[a] < sz[b]:
            a, b = b, a
        p[b] = a
        sz[a] += sz[b]


cc = len(v)
for a, b in e:
    if find(d[a]) != find(d[b]):
        union(d[a], d[b])
        cc -= 1
        if cc == 1:
            ans = a[0] * b[0]

print(ans)

# n = len(v)
# INF = 1e12
# vis = [False] * n
# min_e = [(INF, -1)] * n
# min_e[0] = (0, -1)
# max_e = (0, -1, -1)

# for _ in range(n):
#     u = -1
#     for i in range(n):
#         if not vis[i] and (u == -1 or min_e[i][0] < min_e[u][0]):
#             u = i
#     vis[u] = True
#     max_e = max(max_e, (*min_e[u], u))
#     for i in range(n):
#         dist = sq_dist((v[u], v[i]))
#         if dist < min_e[i][0]:
#             min_e[i] = (dist, u)

# ans = v[max_e[1]][0] * v[max_e[2]][0]
# print(ans)
