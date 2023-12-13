MAX_CUBES = {"red": 12, "green": 13, "blue": 14}

with open("2023/Day02/input.txt") as f:
    lines = f.read().splitlines()

sum = 0
for game_num, line in enumerate(lines, 1):
    rounds = line[line.find(":") + 2 :].split("; ")
    possible = True
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            num = int(num)
            if num > MAX_CUBES[color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        sum += game_num

print(sum)
