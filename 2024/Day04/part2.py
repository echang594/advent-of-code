with open("2024/Day04/input.txt", "r") as f:
    lines = f.read().splitlines()

n = len(lines)
m = len(lines[0])

ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if lines[i][j] == "A":
            ans += int(
                (
                    lines[i - 1][j - 1] == "M"
                    and lines[i - 1][j + 1] == "M"
                    and lines[i + 1][j + 1] == "S"
                    and lines[i + 1][j - 1] == "S"
                )
                or (
                    lines[i - 1][j - 1] == "S"
                    and lines[i - 1][j + 1] == "M"
                    and lines[i + 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == "S"
                )
                or (
                    lines[i - 1][j - 1] == "S"
                    and lines[i - 1][j + 1] == "S"
                    and lines[i + 1][j + 1] == "M"
                    and lines[i + 1][j - 1] == "M"
                )
                or (
                    lines[i - 1][j - 1] == "M"
                    and lines[i - 1][j + 1] == "S"
                    and lines[i + 1][j + 1] == "S"
                    and lines[i + 1][j - 1] == "M"
                )
            )

print(ans)
