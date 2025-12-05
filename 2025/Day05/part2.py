with open("2025/Day05/input.txt", "r") as f:
    ranges, _ = f.read().split("\n\n")

ranges = [tuple(int(x) for x in r.split("-")) for r in ranges.splitlines()]
points = sorted([(r[0], 0) for r in ranges] + [(r[1] + 1, 1) for r in ranges])

ans = 0
cnt = 0
start = 0
for x, t in points:
    if t == 0:
        cnt += 1
        if cnt == 1:
            start = x
    else:
        cnt -= 1
        if cnt == 0:
            ans += x - start

print(ans)
