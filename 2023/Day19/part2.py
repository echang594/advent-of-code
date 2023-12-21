from collections import deque
import functools
import operator

with open("2023/Day19/input.txt") as f:
    workflows, _ = f.read().split("\n\n")

w = {}
for workflow in workflows.splitlines():
    name = workflow[: workflow.find("{")]
    w[name] = []
    rules = workflow[len(name) + 1 : -1].split(",")
    for rule in rules[:-1]:
        cond, wf = rule.split(":")
        cat, op, num = cond[0], cond[1], int(cond[2:])
        w[name].append((cat, op, num, wf))
    w[name].append(rules[-1])

total = 0
q = deque()
q.append(("in", {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}))
while q:
    cur, constraints = q.pop()
    if cur == "R" or cur == "A":
        if cur == "A":
            total += functools.reduce(
                operator.mul,
                (constraint[1] - constraint[0] + 1 for constraint in constraints.values()),
            )
        continue
    for cat, op, num, wf in w[cur][:-1]:
        new_constraints = constraints.copy()
        if op == "<":
            new_constraints[cat] = (constraints[cat][0], num - 1)
            constraints[cat] = (num, constraints[cat][1])
        else:
            new_constraints[cat] = (num + 1, constraints[cat][1])
            constraints[cat] = (constraints[cat][0], num)
        q.append((wf, new_constraints))
    q.append((w[cur][-1], constraints))

print(total)
