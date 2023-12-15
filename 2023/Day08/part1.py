import re

with open("2023/Day08/input.txt") as f:
    instructions, network = f.read().split("\n\n")

nodes = {}
for line in network.splitlines():
    node, left, right, *_ = re.split(r" = \(|, |\)", line)
    nodes[node] = (left, right)

cur = "AAA"
steps = 0
while cur != "ZZZ":
    cur = nodes[cur][0 if instructions[steps % len(instructions)] == "L" else 1]
    steps += 1

print(steps)
