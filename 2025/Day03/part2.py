with open("2025/Day03/input.txt", "r") as f:
    banks = [[int(c) for c in l] for l in f.read().splitlines()]

ans = 0
for bank in banks:
    dp = [0] * 13
    for b in bank:
        for i in range(12, 0, -1):
            dp[i] = max(dp[i], dp[i - 1] * 10 + b)
    ans += dp[12]

print(ans)
