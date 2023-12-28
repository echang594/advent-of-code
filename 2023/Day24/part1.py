import operator
import itertools

AREA = (200000000000000, 400000000000000)

with open("2023/Day24/input.txt") as f:
    lines = f.read().splitlines()

hail = []
for line in lines:
    p, v = line.split(" @ ")
    p = tuple(int(n) for n in p.split(", ")[:-1])
    v = tuple(int(n) for n in v.split(", ")[:-1])
    hail.append((p, v))


def sub(p, q):
    return tuple(map(operator.sub, p, q))


def cross_2d(u, v):
    return u[0] * v[1] - u[1] * v[0]


def ray_ray_intersects_2d(p, vp, q, vq):
    pq = sub(q, p)
    a, b, c = cross_2d(vp, vq), cross_2d(pq, vq), cross_2d(pq, vp)
    if not a:
        return False
    t = b / a
    s = c / a
    if t < 0 or s < 0:
        return False
    return (p[0] + t * vp[0], p[1] + t * vp[1])


total = 0
for (p, vp), (q, vq) in itertools.combinations(hail, 2):
    intersects = ray_ray_intersects_2d(p, vp, q, vq)
    if intersects:
        x, y = intersects
        if AREA[0] <= x <= AREA[1] and AREA[0] <= y <= AREA[1]:
            total += 1

print(total)
