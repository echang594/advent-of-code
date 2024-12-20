with open("2024/Day19/input.txt", "r") as f:
    patterns, designs = f.read().split("\n\n")

patterns = patterns.split(", ")
designs = designs.split()

ans = 0
for design in designs:
    ways = [0] * (len(design) + 1)
    ways[0] = 1
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if i >= len(pattern) and design[i - len(pattern) : i] == pattern:
                ways[i] += ways[i - len(pattern)]
    ans += ways[len(design)]

print(ans)
