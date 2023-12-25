import operator
from collections import deque

with open("2023/Day22/input.txt") as f:
    lines = f.read().splitlines()

bricks = []
for line in lines:
    p, q = line.split("~")
    p, q = tuple(int(n) for n in p.split(",")), tuple(int(n) for n in q.split(","))
    bricks.append((p, q))
bricks.sort(key=lambda l: l[0][2])


def sub(p, q):
    return tuple(map(operator.sub, p, q))


def dot(p, q):
    return sum(map(operator.mul, p, q))


def cross(p, q):
    return (p[1] * q[2] - p[2] * q[1], p[2] * q[0] - p[0] * q[2], p[0] * q[1] - p[1] * q[0])


def find_diff_pos(*points):
    return [i for i in range(3) if any(point[i] != points[0][i] for point in points)]


def intersects(p0, p1, q0, q1):
    dp, dq, pq = sub(p1, p0), sub(q1, q0), sub(q0, p0)
    if dp == (0, 0, 0) and dq == (0, 0, 0):
        return p0 == q0
    if dq == (0, 0, 0):
        p0, p1, q0, q1, dp, dq = q0, q1, p0, p1, dq, dp
    if dp == (0, 0, 0):
        diff = find_diff_pos(p0, q0, q1)
        return len(diff) == 1 and q0[diff[0]] <= p0[diff[0]] <= q1[diff[0]]
    c, e, f = cross(dp, dq), cross(pq, dq), cross(pq, dp)
    if dot(pq, c):
        return False
    d = dot(c, c)
    t = dot(e, c)
    s = dot(f, c)
    if not d:
        if e == (0, 0, 0):
            diff = find_diff_pos(q0, q1)
            return p0[diff[0]] <= q1[diff[0]] and q0[diff[0]] <= p1[diff[0]]
        return False
    return 0 <= t <= d and 0 <= s <= d


below = [[] for _ in range(len(bricks))]
above = [[] for _ in range(len(bricks))]

for i in range(len(bricks)):
    p0, p1 = bricks[i]
    while p0[2] > 1:
        p0 = (p0[0], p0[1], p0[2] - 1)
        p1 = (p1[0], p1[1], p1[2] - 1)
        supported = False
        for j in range(i - 1, -1, -1):
            q0, q1 = bricks[j]
            if p0[2] > q1[2]:
                continue
            if intersects(p0, p1, q0, q1):
                below[i].append(j)
                above[j].append(i)
                supported = True
        if supported:
            p0 = (p0[0], p0[1], p0[2] + 1)
            p1 = (p1[0], p1[1], p1[2] + 1)
            break
    bricks[i] = (p0, p1)

total = 0
for i in range(len(bricks)):
    indeg = [len(x) for x in below]
    q = deque()
    q.append(i)
    while q:
        cur = q.popleft()
        for brick in above[cur]:
            indeg[brick] -= 1
            if not indeg[brick]:
                q.append(brick)
                total += 1

print(total)
