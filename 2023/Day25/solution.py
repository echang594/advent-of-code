import copy
import random
from collections import deque
import math

with open("2023/Day25/input.txt") as f:
    lines = f.read().splitlines()

g = {}
for line in lines:
    node, edges = line.split(": ")
    edges = edges.split()
    if node not in g:
        g[node] = {"edges": [], "size": 1}
    for edge in edges:
        g[node]["edges"].append(edge)
        if edge not in g:
            g[edge] = {"edges": [], "size": 1}
        g[edge]["edges"].append(node)


def contract(g, t):
    g = copy.deepcopy(g)
    while len(g) > t:
        u = random.choice(list(g.keys()))
        v = random.choice(g[u]["edges"])
        for w in g[v]["edges"]:
            g[w]["edges"].remove(v)
            if w != u:
                g[u]["edges"].append(w)
                g[w]["edges"].append(u)
        g[u]["size"] += g[v]["size"]
        del g[v]
    return g


def cut(g):
    return len(list(g.values())[0]["edges"])


def fast_min_cut(g):
    q = deque()
    q.append(g)
    min_cut = math.inf
    min_cut_g = g
    while q:
        g = q.pop()
        if len(g) <= 6:
            g = contract(g, 2)
            cut_g = cut(g)
            if cut_g < min_cut:
                min_cut = cut_g
                min_cut_g = g
                if min_cut == 3:
                    break
            continue
        t = 1 + math.ceil(len(g) / math.sqrt(2))
        q.append(contract(g, t))
        q.append(contract(g, t))
    return min_cut_g


min_cut_g = fast_min_cut(g)
ans = math.prod([min_cut_g[node]["size"] for node in min_cut_g])
print(ans)

# index = {}
# edges = []
# for line in lines:
#     node, node_edges = line.split(": ")
#     node_edges = node_edges.split()
#     if node not in index:
#         index[node] = len(index)
#     for edge in node_edges:
#         if edge not in index:
#             index[edge] = len(index)
#         edges.append((index[node], index[edge]))
# adj = [[0] * len(index) for _ in index]
# for u, v in edges:
#     adj[u][v] = 1
#     adj[v][u] = 1


# def global_min_cut(mat):
#     best = (math.inf, [])
#     n = len(mat)
#     co = [[i] for i in range(n)]
#     for i in range(n - 1):
#         w = mat[0].copy()
#         s = t = 0
#         for _ in range(n - 1 - i):
#             w[t] = -math.inf
#             s, t = t, w.index(max(w))
#             for j in range(n):
#                 w[j] += mat[t][j]
#         best = min(best, (w[t] - mat[t][t], co[t]))
#         if best[0] == 3:
#             break
#         co[s].extend(co[t])
#         for j in range(n):
#             mat[s][j] += mat[t][j]
#             mat[j][s] = mat[s][j]
#         mat[0][t] = -math.inf
#     return best


# min_cut = global_min_cut(adj)
# ans = len(min_cut[1]) * (len(adj) - len(min_cut[1]))
# print(ans)
