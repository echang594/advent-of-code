with open("2023/Day03/input.txt") as f:
    m = f.read().splitlines()


def is_num(i: int, j: int):
    return i >= 0 and i < len(m) and j >= 0 and j < len(m[i]) and m[i][j].isdigit()


def find_full_num(i: int, j: int):
    l = j - 1
    r = j + 1
    while is_num(i, l):
        l -= 1
    while is_num(i, r):
        r += 1
    return int(m[i][l + 1 : r])


sum = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == "." or m[i][j].isdigit():
            continue

        positions = [(i, j - 1), (i, j + 1)]
        for a in (i - 1, i + 1):
            if is_num(a, j):
                positions.append((a, j))
            else:
                positions.extend(((a, j - 1), (a, j + 1)))

        parts = []
        for a, b in positions:
            if is_num(a, b):
                parts.append(find_full_num(a, b))
                if len(parts) > 2:
                    break
        if len(parts) == 2:
            gear_ratio = parts[0] * parts[1]
            sum += gear_ratio

print(sum)
