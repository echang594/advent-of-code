import re
import itertools

with open("2023/Day11/input.txt") as f:
    image = f.read().splitlines()

expand_x = []
expand_y = []
galaxies = []
for i, row in enumerate(image):
    new_galaxies = [(i, m.start()) for m in re.finditer("#", row)]
    galaxies.extend(new_galaxies)
    expand_x.append((expand_x[-1] if expand_x else 0) + (not new_galaxies))
for col in zip(*image):
    expand_y.append((expand_y[-1] if expand_y else 0) + all(element == "." for element in col))

sum = 0
for a, b in itertools.combinations(galaxies, 2):
    sum += (
        abs(a[0] - b[0])
        + abs(a[1] - b[1])
        + abs(expand_x[b[0]] - expand_x[a[0]]) * 999999
        + abs(expand_y[b[1]] - expand_y[a[1]]) * 999999
    )

print(sum)
