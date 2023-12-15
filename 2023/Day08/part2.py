import re
import math

with open("2023/Day08/input.txt") as f:
    instructions, network = f.read().split("\n\n")

nodes = {}
init = []
for path in network.splitlines():
    node, left, right, *_ = re.split(r" = \(|, |\)", path)
    nodes[node] = (left, right)
    if node[-1] == "A":
        init.append(node)


def walk_to_end(node):
    steps = 0
    while True:
        dir = 0 if instructions[steps % len(instructions)] == "L" else 1
        node = nodes[node][dir]
        steps += 1
        if node[-1] == "Z":
            break
    return steps


steps_to_end = [walk_to_end(node) for node in init]
total_steps = math.lcm(*steps_to_end)

print(total_steps)
