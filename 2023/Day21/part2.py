from collections import deque
import itertools

NUM_STEPS = 26501365

with open("2023/Day21/input.txt") as f:
    m = f.read().splitlines()


def find_plots(start, step_limit):
    visited = {start: 0}
    q = deque()
    q.append(start)
    num_plots = int(step_limit % 2 == 0)
    while q:
        cur = q.popleft()
        r, c = cur
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            new = (nr, nc)
            if m[nr % len(m)][nc % len(m[0])] == "#" or new in visited:
                continue
            visited[new] = visited[cur] + 1
            if visited[new] % 2 == step_limit % 2:
                num_plots += 1
            if visited[new] == step_limit:
                continue
            q.append(new)
    return num_plots


start = (len(m) // 2, len(m[0]) // 2)
step_limits = [len(m) * i + len(m) // 2 for i in range(3)]
plots_in_range = [find_plots(start, step_limit) for step_limit in step_limits]
first_diff = [y - x for (x, y) in itertools.pairwise(plots_in_range)]
second_diff = first_diff[1] - first_diff[0]
a = second_diff // 2
c = plots_in_range[0]
b = plots_in_range[1] - a - c
x = NUM_STEPS // len(m)
num_plots = a * x * x + b * x + c
print(num_plots)
