import numpy as np
from scipy.optimize import milp

with open("2025/Day10/input.txt", "r") as f:
    lines = f.read().splitlines()

ans = 0
for l in lines:
    i = l.find("]")
    j = l.find("{")
    buttons = [[int(x) for x in button[1:-1].split(",")] for button in l[i + 1 : j].split()]
    m = len(buttons)
    b = np.array([int(x) for x in l[j + 1 : -1].split(",")])
    n = len(b)
    A = np.array([[0] * m for _ in range(n)])
    for i, button in enumerate(buttons):
        A[button, i] = 1
    c = np.ones(m)
    res = milp(c, integrality=c, constraints=(A, b, b))
    ans += np.rint(res.x).astype(int).sum()

print(ans)
