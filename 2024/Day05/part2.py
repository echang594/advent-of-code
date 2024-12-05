with open("2024/Day05/input.txt", "r") as f:
    edges, orders = f.read().split("\n\n")

edges = [tuple(int(i) for i in edge.split("|")) for edge in edges.split()]
orders = [[int(i) for i in order.split(",")] for order in orders.split()]

adj = {}
for edge in edges:
    a, b = edge
    if a not in adj:
        adj[a] = set()
    if b not in adj:
        adj[b] = set()
    adj[a].add(b)


def dfs(u):
    visited.add(u)
    for v in adj[u]:
        if v in vertices and v not in visited:
            dfs(v)
    post.append(u)


ans = 0
for order in orders:
    for i in range(1, len(order)):
        for j in range(i):
            if order[j] in adj[order[i]]:
                break
        else:
            continue
        break
    else:
        continue
    vertices = set(order)
    visited = set()
    post = []
    for i in order:
        if i not in visited:
            dfs(i)
    mid = post[len(post) // 2]
    ans += mid

print(ans)
