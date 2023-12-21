with open("2023/Day19/input.txt") as f:
    workflows, parts = f.read().split("\n\n")

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
for part in parts.splitlines():
    ratings = part[1:-1].split(",")
    p = {}
    for rating in ratings:
        cat, num = rating[0], int(rating[2:])
        p[cat] = num

    cur = "in"
    while cur != "A" and cur != "R":
        for cat, op, num, wf in w[cur][:-1]:
            if op == "<" and p[cat] < num or op == ">" and p[cat] > num:
                cur = wf
                break
        else:
            cur = w[cur][-1]

    if cur == "A":
        total += sum(p.values())

print(total)
