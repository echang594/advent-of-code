from queue import Queue

PIPE_DIRS = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1)),
}

DIR_PIPES = {
    (-1, 0): ("|", "7", "F"),
    (1, 0): ("|", "L", "J"),
    (0, -1): ("-", "L", "F"),
    (0, 1): ("-", "J", "7"),
}

with open("2023/Day10/input.txt") as f:
    tiles = f.read().splitlines()

start = None
for i in range(len(tiles)):
    for j in range(len(tiles[i])):
        if tiles[i][j] == "S":
            start = (i, j)
            break
    if start is not None:
        break


start_dirs = []
for dir, pipes in DIR_PIPES.items():
    new_x, new_y = start[0] + dir[0], start[1] + dir[1]
    if tiles[new_x][new_y] in pipes:
        start_dirs.append(dir)
start_dirs = tuple(start_dirs)

for pipe, dirs in PIPE_DIRS.items():
    if start_dirs == dirs:
        tiles[start[0]] = tiles[start[0]][: start[1]] + pipe + tiles[start[0]][start[1] + 1 :]
        break

visited = [[False] * len(tiles[0]) for _ in tiles]
q = Queue()
visited[start[0]][start[1]] = True
q.put((start, 0))
max_dist = 0
while not q.empty():
    (cur_x, cur_y), dist = q.get()
    max_dist = max(max_dist, dist)
    for dir in PIPE_DIRS[tiles[cur_x][cur_y]]:
        new_x, new_y = cur_x + dir[0], cur_y + dir[1]
        if visited[new_x][new_y]:
            continue
        visited[new_x][new_y] = True
        q.put(((new_x, new_y), dist + 1))

print(max_dist)
