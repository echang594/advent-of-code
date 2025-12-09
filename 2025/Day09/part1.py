import itertools

with open("2025/Day09/input.txt", "r") as f:
    locs = [tuple(int(x) for x in l.split(",")) for l in f.read().splitlines()]


def rect(a, b):
    return (abs(b[0] - a[0]) + 1) * (abs(b[1] - a[1]) + 1)


ans = max(rect(a, b) for a, b in itertools.combinations(locs, 2))
print(ans)
