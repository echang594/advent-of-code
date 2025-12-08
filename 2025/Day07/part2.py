with open("2025/Day07/input.txt", "r") as f:
    grid = f.read().splitlines()

beams = [0] * len(grid[0])
beams[grid[0].find("S")] = 1
for row in grid[1:]:
    new_beams = [0] * len(grid[0])
    for i in range(len(row)):
        if not beams[i]:
            continue
        if row[i] == "^":
            new_beams[i - 1] += beams[i]
            new_beams[i + 1] += beams[i]
        else:
            new_beams[i] += beams[i]
    beams = new_beams

ans = sum(beams)
print(ans)
