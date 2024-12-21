from itertools import pairwise
from functools import cache, partial

with open("2024/Day21/input.txt", "r") as f:
    codes = f.read().splitlines()

numpad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
dirpad = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}


@cache
def cost1(a, b):
    if a == b:
        return 1
    if a in ("1", "4", "7") and b in ("0", "A"):
        seq = ">" * numpad[b][1] + "v" * (3 - numpad[a][0])
        return sum(costn(2, c, d) for c, d in pairwise("A" + seq + "A"))
    if a in ("0", "A") and b in ("1", "4", "7"):
        seq = "^" * (3 - numpad[b][0]) + "<" * numpad[a][1]
        return sum(costn(2, c, d) for c, d in pairwise("A" + seq + "A"))
    dx, dy = (numpad[b][0] - numpad[a][0]), (numpad[b][1] - numpad[a][1])
    ud = "^" if dx < 0 else "v"
    lr = "<" if dy < 0 else ">"
    seq1 = lr * abs(dy) + ud * abs(dx)
    if dx == 0 or dy == 0:
        return sum(costn(2, c, d) for c, d in pairwise("A" + seq1 + "A"))
    seq2 = ud * abs(dx) + lr * abs(dy)
    return min(
        sum(costn(2, c, d) for c, d in pairwise("A" + seq1 + "A")),
        sum(costn(2, c, d) for c, d in pairwise("A" + seq2 + "A")),
    )


@cache
def costn(num, a, b):
    cost = cost26 if num == 25 else partial(costn, num + 1)
    if a == b:
        return 1
    if a == "<" and b in ("^", "A"):
        seq = ">" * dirpad[b][1] + "^"
        return sum(cost(c, d) for c, d in pairwise("A" + seq + "A"))
    if a in ("^", "A") and b == "<":
        seq = "v" + "<" * dirpad[a][1]
        return sum(cost(c, d) for c, d in pairwise("A" + seq + "A"))
    dx, dy = (dirpad[b][0] - dirpad[a][0]), (dirpad[b][1] - dirpad[a][1])
    ud = "^" if dx < 0 else "v"
    lr = "<" if dy < 0 else ">"
    seq1 = lr * abs(dy) + ud * abs(dx)
    if dx == 0 or dy == 0:
        return sum(cost(c, d) for c, d in pairwise("A" + seq1 + "A"))
    seq2 = ud * abs(dx) + lr * abs(dy)
    return min(
        sum(cost(c, d) for c, d in pairwise("A" + seq1 + "A")),
        sum(cost(c, d) for c, d in pairwise("A" + seq2 + "A")),
    )


@cache
def cost26(a, b):
    if a == b:
        return 1
    return abs(dirpad[b][0] - dirpad[a][0]) + abs(dirpad[b][1] - dirpad[a][1]) + 1


ans = 0
for code in codes:
    for a, b in pairwise("A" + code):
        ans += cost1(a, b) * int(code[:-1])

print(ans)
