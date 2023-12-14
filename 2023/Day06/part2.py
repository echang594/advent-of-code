import math

with open("2023/Day06/input.txt") as f:
    lines = f.read().splitlines()

time = int(lines[0][lines[0].find(":") + 1 :].replace(" ", ""))
dist = int(lines[1][lines[1].find(":") + 1 :].replace(" ", ""))

prod = 1
d = time * time - 4 * dist
x1 = math.ceil((time - math.sqrt(d)) / 2)
x2 = math.floor((time + math.sqrt(d)) / 2)
prod *= x2 - x1 + 1

print(prod)
