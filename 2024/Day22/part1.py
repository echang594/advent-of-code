with open("2024/Day22/input.txt", "r") as f:
    secrets = [int(secret) for secret in f.read().splitlines()]

ans = 0
MASK = (1 << 24) - 1

for secret in secrets:
    for i in range(2000):
        secret = ((secret << 6) ^ secret) & MASK
        secret = ((secret >> 5) ^ secret) & MASK
        secret = ((secret << 11) ^ secret) & MASK
    ans += secret

print(ans)
