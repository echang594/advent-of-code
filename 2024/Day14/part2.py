with open("2024/Day14/input.txt", "r") as f:
    robots = f.read().splitlines()

N = 103
M = 101

for i in range(len(robots)):
    p, v = robots[i].split()
    p, v = p[2:].split(","), v[2:].split(",")
    p, v = tuple(int(x) for x in reversed(p)), tuple(int(x) for x in reversed(v))
    robots[i] = (p, v)

t = 0
cur_pos = [p for p, _ in robots]
ans = 0

while not ans:
    t += 1
    grid = ["." * M for _ in range(N)]
    for i in range(len(robots)):
        x, y = cur_pos[i]
        vx, vy = robots[i][1]
        cur_pos[i] = ((x + vx) % N, (y + vy) % M)
        grid[cur_pos[i][0]] = (
            grid[cur_pos[i][0]][: cur_pos[i][1]] + "#" + grid[cur_pos[i][0]][cur_pos[i][1] + 1 :]
        )
    for i in range(N):
        if grid[i].find("#########") != -1:
            ans = t
            break

print(ans)
for i in range(N):
    print(grid[i])
