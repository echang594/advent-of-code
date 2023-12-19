with open("2023/Day15/input.txt") as f:
    seq = f.read().split(",")

total = 0
for step in seq:
    cur = 0
    for char in step:
        cur = (cur + ord(char)) * 17 % 256
    total += cur

print(total)
