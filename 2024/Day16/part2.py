from queue import Queue, PriorityQueue

with open("2024/Day16/input.txt", "r") as f:
    maze = f.read().splitlines()

n = len(maze)
d = [[[1000000000] * 4 for _ in range(n)] for _ in range(n)]
p = [[[[] for _ in range(4)] for _ in range(n)] for _ in range(n)]
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
dr = 1

for i in range(n):
    for j in range(n):
        if maze[i][j] == "S":
            s = (i, j)
            break
    else:
        continue
    break

pq = PriorityQueue()
d[s[0]][s[1]][dr] = 0
pq.put((0, s[0], s[1], dr))

while not pq.empty():
    s, x, y, dr = pq.get()
    if s != d[x][y][dr]:
        continue
    if maze[x][y] == "E":
        break
    for i, (dx, dy) in enumerate(dirs):
        if i == (dr + 2) % 4:
            continue
        nx, ny = x + dx, y + dy
        l = 1 if i == dr else 1001
        if maze[nx][ny] != "#":
            if d[x][y][dr] + l < d[nx][ny][i]:
                d[nx][ny][i] = d[x][y][dr] + l
                p[nx][ny][i] = [(x, y, dr)]
                pq.put((d[nx][ny][i], nx, ny, i))
            elif d[x][y][dr] + l == d[nx][ny][i]:
                p[nx][ny][i].append((x, y, dr))

q = Queue()
vis = set()
q.put((x, y, dr))
vis.add((x, y, dr))
while not q.empty():
    x, y, dr = q.get()
    for pr in p[x][y][dr]:
        if pr not in vis:
            q.put(pr)
            vis.add(pr)
ans = len(set((x, y) for x, y, _ in vis))
print(ans)
