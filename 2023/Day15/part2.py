with open("2023/Day15/input.txt") as f:
    seq = f.read().split(",")

boxes = [{} for _ in range(256)]
for step in seq:
    if step[-1] == "-":
        put = False
        label = step[:-1]
    else:
        put = True
        eq = step.find("=")
        label = step[:eq]
        focal_length = int(step[eq + 1 :])
    box_num = 0
    for char in label:
        box_num = (box_num + ord(char)) * 17 % 256
    if put:
        boxes[box_num][label] = focal_length
    else:
        boxes[box_num].pop(label, None)

total = 0
for box_num, box in enumerate(boxes, 1):
    for slot_num, focal_length in enumerate(box.values(), 1):
        total += box_num * slot_num * focal_length

print(total)
