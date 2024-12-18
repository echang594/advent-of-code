from queue import Queue

with open("2024/Day18/input.txt", "r") as f:
    blocks = f.read().splitlines()

blocks = [tuple(int(x) for x in block.split(",")) for block in blocks]

N = 71
INF = 1000000
grid = [["."] * N for _ in range(N)]
for x, y in blocks[:1024]:
    grid[x][y] = "#"

ds = ((-1, 0), (0, 1), (1, 0), (0, -1))
d = [[INF] * N for _ in range(N)]
d[0][0] = 0
q = Queue()
q.put((0, 0))
while not q.empty():
    x, y = q.get()
    if (x, y) == (N - 1, N - 1):
        break
    for dx, dy in ds:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != "#" and d[nx][ny] == INF:
            d[nx][ny] = d[x][y] + 1
            q.put((nx, ny))

ans = d[N - 1][N - 1]
print(ans)
