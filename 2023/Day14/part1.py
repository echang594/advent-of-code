with open("2023/Day14/input.txt") as f:
    platform = f.read().splitlines()

load = 0
for j in range(len(platform[0])):
    k = 0
    for i in range(len(platform)):
        if platform[i][j] == "#":
            k = i + 1
        elif platform[i][j] == "O":
            load += len(platform) - k
            k += 1

print(load)
