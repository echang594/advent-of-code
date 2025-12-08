import itertools
import heapq
import collections
import functools
import operator

with open("2025/Day08/input.txt", "r") as f:
    v = [tuple(int(x) for x in l.split(",")) for l in f.read().splitlines()]


def sq_dist(t):
    a, b = t
    return sum((c - d) ** 2 for c, d in zip(a, b))


e = heapq.nsmallest(1000, itertools.combinations(v, 2), sq_dist)
adj = collections.defaultdict(list)
for a, b in e:
    adj[a].append(b)
    adj[b].append(a)
vis = collections.defaultdict(bool)


def dfs(u):
    vis[u] = True
    cnt = 1
    for v in adj[u]:
        if vis[v]:
            continue
        cnt += dfs(v)
    return cnt


sizes = []
for i in v:
    if vis[i]:
        continue
    sizes.append(dfs(i))

ans = functools.reduce(operator.mul, heapq.nlargest(3, sizes))
print(ans)
