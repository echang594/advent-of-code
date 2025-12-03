with open("2025/Day02/input.txt", "r") as f:
    ranges = [tuple(r.split("-")) for r in f.read().split(",")]

ans = 0
for sl, sr in ranges:
    l, r = int(sl), int(sr)
    for i in range(l, r + 1):
        x = str(i)
        if x == x[: len(x) // 2] * 2:
            ans += i

print(ans)
