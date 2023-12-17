with open("2023/Day13/input.txt") as f:
    patterns = f.read().split("\n\n")


def find_reflection(a: list[int]):
    for i in range(1, len(a)):
        for j in range(min(i, len(a) - i)):
            if a[i + j] != a[i - j - 1]:
                break
        else:
            return i
    return 0


num = 0
for pattern in patterns:
    m = [row.replace(".", "0").replace("#", "1") for row in pattern.splitlines()]
    rows = [int(row, 2) for row in m]
    reflection = find_reflection(rows)
    if reflection:
        num += 100 * reflection
        continue
    cols = [int("".join(col), 2) for col in zip(*m)]
    num += find_reflection(cols)

print(num)
