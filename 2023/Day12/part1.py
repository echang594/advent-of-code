import re
import itertools

with open("2023/Day12/input.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    damaged, undamaged = line.split()
    undamaged = [int(x) for x in undamaged.split(",")]
    unknowns = [m.start() for m in re.finditer("\?", damaged)]
    possible = 0
    for arrangement in itertools.product(".#", repeat=len(unknowns)):
        combined = list(damaged)
        for unknown, condition in zip(unknowns, arrangement):
            combined[unknown] = condition
        combined = "".join(combined)
        possible += [len(x) for x in combined.split(".") if x] == undamaged
    total += possible

print(total)
