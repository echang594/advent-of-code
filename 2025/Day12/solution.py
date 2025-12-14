import operator
import functools

with open("2025/Day12/input.txt", "r") as f:
    *_, regions = f.read().split("\n\n")

regions = regions.splitlines()
ans = 0
for region in regions:
    dims, nums = region.split(":")
    dims = [int(x) for x in dims.split("x")]
    nums = [int(x) for x in nums.split()]
    if functools.reduce(operator.mul, (dim // 3 for dim in dims)) >= sum(nums):
        ans += 1

print(ans)
