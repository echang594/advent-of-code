import operator
import functools

with open("2025/Day06/input.txt", "r") as f:
    lines = f.read().splitlines()

nums = [[]]
for l in zip(*lines[:-1]):
    l = "".join(l).strip()
    if l:
        nums[-1].append(int(l))
    else:
        nums.append([])

ops = lines[-1].split()

ans = 0
for l, op in zip(nums, ops):
    f = operator.add if op == "+" else operator.mul
    ans += functools.reduce(f, l)

print(ans)
