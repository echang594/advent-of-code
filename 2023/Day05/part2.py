with open("2023/Day05/input.txt") as f:
    blocks = f.read().split("\n\n")

nums = [int(x) for x in blocks[0].split()[1:]]
it = iter(nums)
groups = list(zip(it, it))

for block in blocks[1:]:
    mapped = []
    for line in block.split("\n")[1:]:
        unmapped = []
        dest, src, size = (int(x) for x in line.split())
        for start, group_size in groups:
            if src + size < start or start + group_size < src:
                unmapped.append((start, group_size))
            elif src <= start and start + group_size <= src + size:
                mapped.append((start + dest - src, group_size))
            elif src <= start and src + size < start + group_size:
                mapped.append((start + dest - src, (src + size) - start))
                unmapped.append((src + size, (start + group_size) - (src + size)))
            elif start < src and start + group_size <= src + size:
                mapped.append((dest, (start + group_size) - src))
                unmapped.append((start, src - start))
            elif start < src and src + size < start + group_size:
                mapped.append((dest, size))
                unmapped.extend(
                    ((start, src - start), (src + size, (start + group_size) - (src + size)))
                )
        groups = unmapped
    if groups:
        mapped += groups
    groups = mapped

print(min(groups)[0])
