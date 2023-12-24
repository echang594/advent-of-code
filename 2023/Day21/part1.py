from collections import deque

NUM_STEPS = 64

with open("2023/Day21/input.txt") as f:
    m = f.read().splitlines()

start = (len(m) // 2, len(m[0]) // 2)
visited = {start: 0}
q = deque()
q.append(start)
num_plots = 1
while q:
    cur = q.popleft()
    r, c = cur
    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nr, nc = r + dr, c + dc
        new = (nr, nc)
        if (
            nr < 0
            or nr >= len(m)
            or nc < 0
            or nc >= len(m[0])
            or m[nr][nc] == "#"
            or new in visited
        ):
            continue
        visited[new] = visited[cur] + 1
        if visited[new] % 2 == 0:
            num_plots += 1
        if visited[new] < NUM_STEPS:
            q.append(new)

print(num_plots)
