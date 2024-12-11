with open("2024/Day11/input.txt", "r") as f:
    stones = [int(x) for x in f.read().split()]

cur = {}
for stone in stones:
    if stone not in cur:
        cur[stone] = 1
    else:
        cur[stone] += 1


def f(stone):
    if not stone:
        return [1]
    s = str(stone)
    if len(s) % 2 == 0:
        return [int(s[: len(s) // 2]), int(s[len(s) // 2 :])]
    return [stone * 2024]


for i in range(75):
    nxt = {}
    for stone, num in cur.items():
        nxts = f(stone)
        for s in nxts:
            if s not in nxt:
                nxt[s] = num
            else:
                nxt[s] += num
    cur = nxt

ans = sum(cur.values())
print(ans)
