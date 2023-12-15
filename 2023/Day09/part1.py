import itertools

with open("2023/Day09/input.txt") as f:
    lines = f.read().splitlines()


def r(seq):
    if all(x == seq[-1] for x in seq):
        return seq[-1]
    new_seq = [y - x for (x, y) in itertools.pairwise(seq)]
    return seq[-1] + r(new_seq)


sum = 0
for line in lines:
    seq = [int(x) for x in line.split()]
    sum += r(seq)

print(sum)
