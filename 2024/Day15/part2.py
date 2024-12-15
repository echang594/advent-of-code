from itertools import chain

with open("2024/Day15/input.txt", "r") as f:
    grid, moves = f.read().split("\n\n")

changes = {"#": "##", "O": "[]", ".": "..", "@": "@."}
grid = [[c for c in chain.from_iterable(changes[c] for c in line)] for line in grid.splitlines()]
moves = moves.replace("\n", "")
n = len(grid)
m = len(grid[0])

ds = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

for i in range(n):
    for j in range(m):
        if grid[i][j] == "@":
            x, y = i, j

grid[x][y] = "."

for move in moves:
    dx, dy = ds[move]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == ".":
        x, y = nx, ny
        continue
    if grid[nx][ny] == "#":
        continue
    if move in "<>":
        while grid[nx][ny] in "[]":
            nx, ny = nx + dx, ny + dy
        if grid[nx][ny] == "#":
            continue
        c = "[" if move == "<" else "]"
        while (nx, ny) != (x + dx, y + dy):
            grid[nx][ny] = c
            c = "]" if c == "[" else "["
            nx, ny = nx - dx, ny - dy
        x, y = nx, ny
        grid[x][y] = "."
        continue
    boxes = [(nx, ny if grid[nx][ny] == "[" else ny - 1)]
    blocked = False
    i = 0
    while i < len(boxes):
        cx, cy = boxes[i]
        nx, ny = cx + dx, cy + dy
        if grid[nx][ny] == "#" or grid[nx][ny + 1] == "#":
            blocked = True
            break
        if grid[nx][ny] == "[":
            boxes.append((nx, ny))
        if grid[nx][ny] == "]":
            boxes.append((nx, ny - 1))
        if grid[nx][ny + 1] == "[":
            boxes.append((nx, ny + 1))
        i += 1
    if blocked:
        continue
    for cx, cy in reversed(boxes):
        nx, ny = cx + dx, cy + dy
        grid[nx][ny] = "["
        grid[nx][ny + 1] = "]"
        grid[cx][cy] = "."
        grid[cx][cy + 1] = "."
    x, y = x + dx, y + dy

ans = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "[":
            ans += 100 * i + j

print(ans)
