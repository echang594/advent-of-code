import heapq
import functools
import operator
import math

MAX_SAME_DIRECTION = 3

with open("2023/Day17/input.txt") as f:
    m = f.read().splitlines()


def get(d, *keys):
    try:
        return functools.reduce(operator.getitem, keys, d)
    except KeyError:
        return math.inf


def put(d, *keys, value):
    for key in keys[:-1]:
        if key not in d:
            d[key] = {}
        d = d[key]
    d[keys[-1]] = value


m = [[int(hl) for hl in row] for row in m]
mhl = {(0, 0): {(0, 0): {1: 0}}}
h = [(0, (0, 0), (0, 0), 1)]
while h:
    uhl, u, ud, usd = heapq.heappop(h)
    if uhl > mhl[u][ud][usd]:
        continue
    uhl = mhl[u][ud][usd]
    (ui, uj), (udi, udj) = u, ud
    for vd in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        vdi, vdj = vd
        vi, vj = ui + vdi, uj + vdj
        v = vi, vj
        if vi < 0 or vi >= len(m) or vj < 0 or vj >= len(m[0]) or udi == -vdi and udj == -vdj:
            continue
        vsd = usd + 1 if ud == vd else 1
        if vsd <= MAX_SAME_DIRECTION and uhl + m[vi][vj] < get(mhl, v, vd, vsd):
            put(mhl, v, vd, vsd, value=uhl + m[vi][vj])
            vhl = mhl[v][vd][vsd]
            heapq.heappush(h, (vhl, v, vd, vsd))

print(
    min(
        mhl[len(m) - 1, len(m[0]) - 1][d][sd]
        for d in ((0, 1), (1, 0))
        for sd in range(1, MAX_SAME_DIRECTION + 1)
    )
)
