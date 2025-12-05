with open("2025/Day05/input.txt", "r") as f:
    ranges, ids = f.read().split("\n\n")

ranges = [tuple(int(x) for x in r.split("-")) for r in ranges.splitlines()]
ids = [int(x) for x in ids.splitlines()]

points = sorted([(r[0], 0) for r in ranges] + [(id, 1) for id in ids] + [(r[1], 2) for r in ranges])

ans = 0
cnt = 0
for x, t in points:
    if t == 0:
        cnt += 1
    elif t == 1:
        ans += cnt > 0
    elif t == 2:
        cnt -= 1

print(ans)
