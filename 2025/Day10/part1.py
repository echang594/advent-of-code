import numpy as np

with open("2025/Day10/input.txt", "r") as f:
    lines = f.read().splitlines()

ans = 0
for l in lines:
    i = l.find("]")
    j = l.find("{")
    buttons = [[int(x) for x in button[1:-1].split(",")] for button in l[i + 1 : j].split()]
    m = len(buttons)
    b = np.array([1 if c == "#" else 0 for c in l[1:i]])
    n = len(b)
    A = np.array([[0] * m for _ in range(n)])
    for i, button in enumerate(buttons):
        A[button, i] = 1
    num = m
    for i in range(2**m):
        x = np.array([int(x) for x in f"{i:0{m}b}"])
        if np.array_equal((A @ x) % 2, b):
            num = min(num, x.sum())
    ans += num

print(ans)
