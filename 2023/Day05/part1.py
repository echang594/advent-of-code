with open("2023/Day05/input.txt") as f:
    blocks = f.read().split("\n\n")

nums = [int(x) for x in blocks[0].split()[1:]]

for block in blocks[1:]:
    mapped = []
    for line in block.split("\n")[1:]:
        unmapped = []
        dest, src, size = (int(x) for x in line.split())
        for num in nums:
            if src <= num < src + size:
                mapped.append(dest + num - src)
            else:
                unmapped.append(num)
        nums = unmapped
    if nums:
        mapped += nums
    nums = mapped

print(min(nums))
