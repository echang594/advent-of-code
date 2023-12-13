with open("2023/Day02/input.txt") as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    rounds = line[line.find(":") + 2 :].split("; ")
    num_cubes = {"red": 0, "green": 0, "blue": 0}
    for round in rounds:
        cubes = round.split(", ")
        for cube in cubes:
            num, color = cube.split(" ")
            num = int(num)
            num_cubes[color] = max(num_cubes[color], num)
    power = 1
    for num in num_cubes.values():
        power *= num
    sum += power

print(sum)
