with open("2025/Day03/input.txt", "r") as f:
    banks = [[int(c) for c in l] for l in f.read().splitlines()]

ans = 0
for bank in banks:
    mx = 0
    a = bank[0]
    for b in bank[1:]:
        mx = max(mx, a * 10 + b)
        a = max(a, b)
    ans += mx

print(ans)
