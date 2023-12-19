import functools

with open("2023/Day14/input.txt") as f:
    platform = f.read().splitlines()


def cycle(m: list[list[str]]):
    for j in range(len(m[0])):
        k = 0
        for i in range(len(m)):
            if m[i][j] == "#":
                k = i + 1
            elif m[i][j] == "O":
                m[i][j], m[k][j] = m[k][j], m[i][j]
                k += 1
    for i in range(len(m)):
        k = 0
        for j in range(len(m[0])):
            if m[i][j] == "#":
                k = j + 1
            elif m[i][j] == "O":
                m[i][j], m[i][k] = m[i][k], m[i][j]
                k += 1
    for j in range(len(m[0])):
        k = len(m) - 1
        for i in range(len(m) - 1, -1, -1):
            if m[i][j] == "#":
                k = i - 1
            elif m[i][j] == "O":
                m[i][j], m[k][j] = m[k][j], m[i][j]
                k -= 1
    for i in range(len(m)):
        k = len(m[0]) - 1
        for j in range(len(m[0]) - 1, -1, -1):
            if m[i][j] == "#":
                k = j - 1
            elif m[i][j] == "O":
                m[i][j], m[i][k] = m[i][k], m[i][j]
                k -= 1


def get_hash(m: list[list[str]]):
    return tuple(
        functools.reduce(lambda x, y: x << 1 | y, (char == "O" for char in row), 0) for row in m
    )


m = [list(row) for row in platform]
cycles = {}
cycles[get_hash(m)] = 0
num = 0
while True:
    num += 1
    cycle(m)
    h = get_hash(m)
    if h in cycles:
        break
    cycles[h] = num
cycle_len = num - cycles[h]
for i in range((1000000000 - num) % cycle_len):
    cycle(m)
    h = get_hash(m)

load = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "O":
            load += len(m) - i

print(load)
