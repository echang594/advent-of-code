with open("2023/Day03/input.txt") as f:
    m = f.read().splitlines()


def is_symbol(i: int, j: int):
    return (
        i >= 0
        and i < len(m)
        and j >= 0
        and j < len(m[i])
        and m[i][j] != "."
        and not m[i][j].isdigit()
    )


sum = 0
for i in range(len(m)):
    j = 0
    while j < len(m[i]):
        if not m[i][j].isdigit():
            j += 1
            continue

        k = j + 1
        while k < len(m[i]) and m[i][k].isdigit():
            k += 1
        num = int(m[i][j:k])

        positions = [(i, j - 1), (i, k)] + [
            (a, b) for a in (i - 1, i + 1) for b in range(j - 1, k + 1)
        ]
        found_symbol = False
        for a, b in positions:
            if is_symbol(a, b):
                found_symbol = True
                break
        if found_symbol:
            sum += num
        j = k + 1

print(sum)
