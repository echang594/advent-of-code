from collections import defaultdict
from itertools import pairwise

with open("2024/Day22/input.txt", "r") as f:
    secrets = [int(secret) for secret in f.read().splitlines()]

MASK = (1 << 24) - 1


def generate(secret):
    secret = ((secret << 6) ^ secret) & MASK
    secret = ((secret >> 5) ^ secret) & MASK
    secret = ((secret << 11) ^ secret) & MASK
    return secret


seq = defaultdict(int)
for secret in secrets:
    nums = [secret] + [secret := generate(secret) for _ in range(2000)]
    prices = [num % 10 for num in nums]
    diffs = [b - a for a, b in pairwise(prices)]
    used = set()
    for i in range(4, len(prices)):
        change = tuple(diffs[i - 4 : i])
        if change not in used:
            seq[change] += prices[i]
            used.add(change)

ans = max(seq.values())
print(ans)
