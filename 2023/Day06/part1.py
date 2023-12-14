import math

with open("2023/Day06/input.txt") as f:
    lines = f.read().splitlines()

times = [int(x) for x in lines[0].split()[1:]]
dists = [int(x) for x in lines[1].split()[1:]]

prod = 1
for time, dist in zip(times, dists):
    d = time * time - 4 * dist
    if not d:
        continue
    x1 = math.ceil((time - math.sqrt(d)) / 2)
    x2 = math.floor((time + math.sqrt(d)) / 2)
    prod *= x2 - x1 + 1

print(prod)
