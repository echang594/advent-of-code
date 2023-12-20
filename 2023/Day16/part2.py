from collections import deque

with open("2023/Day16/input.txt") as f:
    g = f.read().splitlines()

starts = [
    *(((r, c), (0, 1 if not c else -1)) for c in (0, len(g[0]) - 1) for r in range(len(g))),
    *(((r, c), (1 if not r else -1, 0)) for r in (0, len(g) - 1) for c in range(len(g[0]))),
]
mx = 0
for pos, dir in starts:
    visited = {}
    q = deque()
    q.append((pos, dir))
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
    mx = max(mx, len(visited))

print(mx)
