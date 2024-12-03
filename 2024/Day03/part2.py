import re

with open("2024/Day03/input.txt", "r") as f:
    lines = f.read()

p = re.compile(r"mul\(\d+,\d+\)|do(n't)?\(\)")

ans = 0
do = True
for match in p.finditer(lines):
    s = match.group()
    if s.startswith("mul"):
        if not do:
            continue
        a, b = (int(x) for x in s[4:-1].split(","))
        ans += a * b
    elif len(s) == 4:
        do = True
    else:
        do = False

print(ans)
