with open("2024/Day24/input.txt", "r") as f:
    inputs, gates = f.read().split("\n\n")

gates = gates.split()
gates = [
    (gates[i + 1],) + tuple(sorted((gates[i], gates[i + 2]))) + (gates[i + 4],)
    for i in range(0, len(gates), 5)
]

sus = set()
check1 = set()
check2 = set()
for gate_type, a, b, c in gates:
    if a[0] in "xy":
        if c[0] == "z" and (a, b, c) != ("x00", "y00", "z00"):
            sus.add(c)
    if gate_type == "XOR" and not a[0] in "xy":
        if c[0] != "z":
            sus.add(c)
    if c[0] == "z" and gate_type != "XOR" and c != "z45":
        sus.add(c)
    if gate_type == "AND" and not a == "x00":
        check1.add(c)
    if gate_type == "OR":
        check2.add(a)
        check2.add(b)

for a in set(check1):
    if a in check2:
        check1.remove(a)
        check2.remove(a)

sus.update(check1, check2)
ans = ",".join(sorted(sus))
print(ans)
