DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]

with open("2023/Day18/input.txt") as f:
    plan = f.read().splitlines()

x, y = [0], [0]
for i, line in enumerate(plan[:-1]):
    instructions = line.split()[2][2:-1]
    distance = int(instructions[:-1], 16)
    direction = DIRS[int(instructions[-1])]
    x.append(x[-1] + direction[0] * distance)
    y.append(y[-1] + direction[1] * distance)

area = 0
perimeter = 0
net_clockwise = 0
for i in range(len(x)):
    area += x[i - 1] * y[i] - x[i] * y[i - 1]
    perimeter += abs(x[i] - x[i - 1] + y[i] - y[i - 1])
    net_clockwise += (
        1
        if (x[i - 1] - x[i - 2]) * (y[i] - y[i - 2]) - (x[i] - x[i - 2]) * (y[i - 1] - y[i - 2]) < 0
        else -1
    )

area = abs(area) // 2 + perimeter // 2 + abs(net_clockwise) // 4

print(area)
