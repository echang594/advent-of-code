with open("2024/Day25/input.txt", "r") as f:
    schematics = f.read().split("\n\n")

locks = []
keys = []
for schema in schematics:
    lock = schema[0] == "#"
    schema = [col.count("#") for col in zip(*schema.splitlines())]
    (locks if lock else keys).append(schema)

ans = 0
for lock in locks:
    for key in keys:
        if all(a + b <= 7 for a, b in zip(lock, key)):
            ans += 1

print(ans)
