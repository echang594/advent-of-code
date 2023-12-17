with open("2023/Day12/input.txt") as f:
    lines = f.read().splitlines()

total = 0
for line in lines:
    damaged, undamaged = line.split()
    damaged = "?".join([damaged] * 5)
    undamaged = [int(x) for x in undamaged.split(",")] * 5
    dp = [0] * len(damaged)
    for i in range(undamaged[0] - 1, len(damaged)):
        if (
            (i == len(damaged) - 1 or damaged[i + 1] != "#")
            and not any(x == "." for x in damaged[i + 1 - undamaged[0] : i + 1])
            and not any(x == "#" for x in damaged[: i + 1 - undamaged[0]])
        ):
            dp[i] = 1
    for block in undamaged[1:]:
        for i in range(len(damaged) - 1, -1, -1):
            dp[i] = 0
            if (
                i != len(damaged) - 1
                and damaged[i + 1] == "#"
                or i <= block
                or any(x == "." for x in damaged[i + 1 - block : i + 1])
            ):
                continue
            for j in range(i - block):
                if not any(x == "#" for x in damaged[j + 1 : i + 1 - block]):
                    dp[i] += dp[j]
    last_damaged = damaged.rfind("#")
    total += sum(dp[last_damaged if last_damaged != -1 else 0 :])

print(total)
