from queue import Queue
from collections import defaultdict

with open("2024/Day24/input.txt", "r") as f:
    inputs, gates = f.read().split("\n\n")

gate_funcs = {
    "AND": lambda a, b: int(a and b),
    "OR": lambda a, b: int(a or b),
    "XOR": lambda a, b: int(a and not b or not a and b),
}

wires = {}
q = Queue()
for inpt in inputs.splitlines():
    wire, value = inpt.split(": ")
    wires[wire] = int(value)
    q.put(wire)

inc = {}
ind = {}
out = defaultdict(list)
for gate in gates.splitlines():
    a, gate_type, b, _, c = gate.split()
    inc[c] = (gate_type, a, b)
    out[a].append(c)
    out[b].append(c)
    ind[c] = 2

while not q.empty():
    cur = q.get()
    if cur in inc:
        gate_type, a, b = inc[cur]
        wires[cur] = gate_funcs[gate_type](wires[a], wires[b])
    for wire in out[cur]:
        ind[wire] -= 1
        if not ind[wire]:
            q.put(wire)

zwires = [str(wires[x]) for x in sorted(filter(lambda x: x.startswith("z"), wires), reverse=True)]
ans = int("".join(zwires), 2)
print(ans)
