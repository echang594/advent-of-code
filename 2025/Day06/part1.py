import operator
import functools

with open("2025/Day06/input.txt", "r") as f:
    lines = [l.split() for l in f.read().splitlines()]

nums = [[int(x) for x in l] for l in zip(*lines[:-1])]
ops = lines[-1]

ans = 0
for l, op in zip(nums, ops):
    f = operator.add if op == "+" else operator.mul
    ans += functools.reduce(f, l)

print(ans)
