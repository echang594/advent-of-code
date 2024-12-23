from collections import defaultdict
from itertools import combinations

with open("2024/Day23/input.txt", "r") as f:
    edges = [edge.split("-") for edge in f.read().splitlines()]

adj = defaultdict(set)
for a, b in edges:
    adj[a].add(b)
    adj[b].add(a)

cliques = set()
for a in adj:
    for b, c in combinations(adj[a], 2):
        if c in adj[b]:
            cliques.add(tuple(sorted((a, b, c))))

while True:
    new_cliques = set()
    for clique in cliques:
        for d in adj[clique[0]]:
            if d not in clique and all(x in adj[d] for x in clique):
                new_clique = tuple(sorted(clique + (d,)))
                new_cliques.add(new_clique)
    if not len(new_cliques):
        break
    cliques = new_cliques

ans = ",".join(next(iter(cliques)))
print(ans)
