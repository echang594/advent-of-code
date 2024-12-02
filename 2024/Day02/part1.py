from itertools import pairwise

with open("2024/Day02/input.txt", "r") as f:
    lines = f.read().splitlines()


def safe(nums, inc):
    for a, b in pairwise(nums):
        if not (1 <= (b - a if inc else a - b) <= 3):
            return False
    return True


ans = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    if safe(nums, True) or safe(nums, False):
        ans += 1

print(ans)
