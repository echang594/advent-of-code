import re

with open("2024/Day03/input.txt", "r") as f:
    lines = f.read()

p = re.compile(r"mul\(\d+,\d+\)")

ans = 0
for match in p.finditer(lines):
    a, b = (int(x) for x in match.group()[4:-1].split(","))
    ans += a * b

print(ans)
