from fractions import Fraction

with open("2023/Day24/input.txt") as f:
    lines = f.read().splitlines()

hail = []
for line in lines:
    p, v = line.split(" @ ")
    p = tuple(int(n) for n in p.split(", "))
    v = tuple(int(n) for n in v.split(", "))
    hail.append((p, v))

(
    ((pax, pay, paz), (vax, vay, vaz)),
    ((pbx, pby, pbz), (vbx, vby, vbz)),
    ((pcx, pcy, pcz), (vcx, vcy, vcz)),
) = hail[0:3]
m = [
    [
        0,
        vaz - vcz,
        vcy - vay,
        0,
        pcz - paz,
        pay - pcy,
        pay * vaz - paz * vay - pcy * vcz + pcz * vcy,
    ],
    [
        vaz - vcz,
        0,
        vcx - vax,
        pcz - paz,
        0,
        pax - pcx,
        pax * vaz - paz * vax - pcx * vcz + pcz * vcx,
    ],
    [
        vay - vcy,
        vcx - vax,
        0,
        pcy - pay,
        pax - pcx,
        0,
        pax * vay - pay * vax - pcx * vcy + pcy * vcx,
    ],
    [
        0,
        vbz - vcz,
        vcy - vby,
        0,
        pcz - pbz,
        pby - pcy,
        pby * vbz - pbz * vby - pcy * vcz + pcz * vcy,
    ],
    [
        vbz - vcz,
        0,
        vcx - vbx,
        pcz - pbz,
        0,
        pbx - pcx,
        pbx * vbz - pbz * vbx - pcx * vcz + pcz * vcx,
    ],
    [
        vby - vcy,
        vcx - vbx,
        0,
        pcy - pby,
        pbx - pcx,
        0,
        pbx * vby - pby * vbx - pcx * vcy + pcy * vcx,
    ],
]


def gauss(a: list[list[int]]):
    n = len(a)
    a = [[Fraction(i) for i in row] for row in a]

    for i in range(n):
        mx = a[i][i]
        mx_k = i
        for k in range(i + 1, n):
            if abs(a[k][i]) > mx:
                mx = abs(a[k][i])
                mx_k = k

        a[i], a[mx_k] = a[mx_k], a[i]

        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]
            for j in range(i + 1, n + 1):
                a[k][j] -= c * a[i][j]
            a[k][i] = 0

    x = []
    for i in range(n - 1, -1, -1):
        x.insert(0, a[i][n] / a[i][i])
        for k in range(i - 1, -1, -1):
            a[k][n] -= a[k][i] * x[0]

    return [int(i) for i in x]


rock = gauss(m)
ans = sum(rock[:3])

print(ans)
