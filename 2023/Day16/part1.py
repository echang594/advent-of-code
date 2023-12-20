from collections import deque

with open("2023/Day16/input.txt") as f:
    g = f.read().splitlines()

visited = {}
q = deque()
q.append(((0, 0), (0, 1)))
while q:
    (r, c), (dr, dc) = q.pop()
    while 0 <= r < len(g) and 0 <= c < len(g[0]):
        if g[r][c] in "|-" and (r, c) in visited:
            break
        visited[(r, c)] = True
        if g[r][c] == "/":
            dr, dc = -dc, -dr
        elif g[r][c] == "\\":
            dr, dc = dc, dr
        elif g[r][c] == "|" and dc:
            q.append(((r - 1, c), (-1, 0)))
            q.append(((r + 1, c), (1, 0)))
            break
        elif g[r][c] == "-" and dr:
            q.append(((r, c - 1), (0, -1)))
            q.append(((r, c + 1), (0, 1)))
            break
        r += dr
        c += dc
print(len(visited))
