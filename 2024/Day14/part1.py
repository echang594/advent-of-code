import math

with open("2024/Day14/input.txt", "r") as f:
    robots = f.read().splitlines()

N = 103
M = 101
T = 100

for i in range(len(robots)):
    p, v = robots[i].split()
    p, v = p[2:].split(","), v[2:].split(",")
    p, v = tuple(int(x) for x in reversed(p)), tuple(int(x) for x in reversed(v))
    robots[i] = (p, v)

q = [0] * 4
for p, v in robots:
    end_p = ((p[0] + v[0] * T) % N, (p[1] + v[1] * T) % M)
    if end_p[0] == N // 2 or end_p[1] == M // 2:
        continue
    k = 2 * int(end_p[0] > N // 2) + int(end_p[1] > M // 2)
    q[k] += 1

ans = math.prod(q)
print(ans)
