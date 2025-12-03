with open("2025/Day02/input.txt", "r") as f:
    ranges = [tuple(r.split("-")) for r in f.read().split(",")]

ans = 0
for sl, sr in ranges:
    l, r = int(sl), int(sr)
    for i in range(l, r + 1):
        x = str(i)
        for j in range(1, len(x) // 2 + 1):
            if len(x) % j != 0:
                continue
            if x == x[:j] * (len(x) // j):
                ans += i
                break

print(ans)
