import copy
from collections import deque

with open("2023/Day20/input.txt") as f:
    modules = f.read().splitlines()

m = {}
init_state = {}
for module in modules:
    name, dests = module.split(" -> ")
    dests = dests.split(", ")
    kind = "b"
    if name[0] == "%" or name[0] == "&":
        kind, name = name[0], name[1:]
        if kind == "%":
            init_state[name] = False
        else:
            init_state[name] = {}
    m[name] = {"kind": kind, "dests": dests}

for name in m:
    for dest in m[name]["dests"]:
        if dest in m and m[dest]["kind"] == "&":
            init_state[dest][name] = "l"


def get_hash(d: dict):
    return tuple(tuple(v.values()) if type(v) is dict else v for k, v in d.items())


states = {get_hash(init_state): (0, 0)}
state = init_state
low, high = 0, 0
for i in range(1, 1001):
    state = copy.deepcopy(state)
    low += 1
    q = deque()
    q.append(("broadcaster", "l", "button"))
    while q:
        cur, pulse, prev = q.popleft()
        if cur not in m:
            continue

        if m[cur]["kind"] == "%":
            if pulse == "h":
                continue
            pulse = "l" if state[cur] else "h"
            state[cur] = not state[cur]
        if m[cur]["kind"] == "&":
            state[cur][prev] = pulse
            pulse = "l" if all(last_pulse == "h" for last_pulse in state[cur].values()) else "h"

        for dest in m[cur]["dests"]:
            q.append((dest, pulse, cur))
        if pulse == "l":
            low += len(m[cur]["dests"])
        else:
            high += len(m[cur]["dests"])

    h = get_hash(state)
    if h in states:
        break
    states[h] = (low, high)

if i == 1001:
    print(low * high)
else:
    num_cycles = 1000 // i
    print(low * high * num_cycles * num_cycles)
