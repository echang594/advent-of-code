with open("2025/Day01/input.txt", "r") as f:
    lines = f.read().splitlines()

ans = 0
dial = 50
for line in lines:
    dial += (1 if line[0] == "R" else -1) * int(line[1:])
    if dial % 100 == 0:
        ans += 1
print(ans)
