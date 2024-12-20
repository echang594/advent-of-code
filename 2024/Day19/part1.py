with open("2024/Day19/input.txt", "r") as f:
    patterns, designs = f.read().split("\n\n")

patterns = patterns.split(", ")
designs = designs.split()

ans = 0
for design in designs:
    possible = [False] * (len(design) + 1)
    possible[0] = True
    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if (
                i >= len(pattern)
                and design[i - len(pattern) : i] == pattern
                and possible[i - len(pattern)]
            ):
                possible[i] = True
                break
    if possible[len(design)]:
        ans += 1

print(ans)
