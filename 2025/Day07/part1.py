with open("2025/Day07/input.txt", "r") as f:
    grid = f.read().splitlines()

ans = 0
beams = [False] * len(grid[0])
beams[grid[0].find("S")] = True
for row in grid[1:]:
    new_beams = [False] * len(grid[0])
    for i in range(len(row)):
        if not beams[i]:
            continue
        if row[i] == "^":
            new_beams[i - 1] = True
            new_beams[i + 1] = True
            ans += 1
        else:
            new_beams[i] = True
    beams = new_beams

print(ans)
