import operator
from collections import deque

DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

with open("2023/Day18/input.txt") as f:
    plan = f.read().splitlines()

cur = (0, 0)
g = {}
r_min = r_max = c_min = c_max = 0
for line in plan:
    d, l, color = line.split()
    l = int(l)
    for i in range(l):
        cur = tuple(map(operator.add, cur, DIRS[d]))
        g[cur] = 1
    if d == "U":
        r_min = min(r_min, cur[0])
    elif d == "D":
        r_max = max(r_max, cur[0])
    elif d == "L":
        c_min = min(c_min, cur[1])
    else:
        c_max = max(c_max, cur[1])


def floodfill(start, fill):
    count = 0
    q = deque()
    q.append(start)
    while q:
        cur = q.pop()
        r, c = cur
        if r < r_min - 1 or r > r_max + 1 or c < c_min - 1 or c > c_max + 1 or cur in g:
            continue
        g[cur] = fill
        count += 1
        for dr, dc in DIRS.values():
            q.append((r + dr, c + dc))
    return count


exterior_area = floodfill((r_min - 1, c_min - 1), 0)
lagoon_area = (r_max - r_min + 3) * (c_max - c_min + 3) - exterior_area

print(lagoon_area)
