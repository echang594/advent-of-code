from collections import defaultdict
from itertools import combinations

with open("2024/Day23/input.txt", "r") as f:
    edges = [edge.split("-") for edge in f.read().splitlines()]

adj = defaultdict(set)
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)

cliques = set()
for a in filter(lambda x: x[0] == "t", adj):
    for b, c in combinations(adj[a], 2):
        if c in adj[b]:
            cliques.add(frozenset((a, b, c)))

ans = len(cliques)
print(ans)
