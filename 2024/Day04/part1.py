with open("2024/Day04/input.txt", "r") as f:
    lines = f.read().splitlines()

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

n = len(lines)
m = len(lines[0])

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(8):
            x = i
            y = j
            for c in "XMAS":
                if x < 0 or x >= n or y < 0 or y >= m or lines[x][y] != c:
                    break
                x += dx[k]
                y += dy[k]
            else:
                ans += 1

print(ans)
