from collections import deque
import math

with open("2023/Day20/input.txt") as f:
    modules = f.read().splitlines()

m = {}
state = {}
for module in modules:
    name, dests = module.split(" -> ")
    dests = dests.split(", ")
    kind = "b"
    if name[0] == "%" or name[0] == "&":
        kind, name = name[0], name[1:]
        if kind == "%":
            state[name] = False
        else:
            state[name] = {}
    m[name] = {"kind": kind, "dests": dests}

for name in m:
    for dest in m[name]["dests"]:
        if dest in m and m[dest]["kind"] == "&":
            state[dest][name] = "l"

button_presses = 1
first_low_pulse = {"bt": 0, "dl": 0, "fr": 0, "rv": 0}
while not all(first_low_pulse.values()):
    q = deque()
    q.append(("broadcaster", "l", "button"))
    count = 0
    while q:
        cur, pulse, prev = q.popleft()
        if cur in first_low_pulse and not first_low_pulse[cur] and pulse == "l":
            first_low_pulse[cur] = button_presses
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

    button_presses += 1

ans = math.lcm(*first_low_pulse.values())

print(ans)
