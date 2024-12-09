with open("2024/Day09/input.txt", "r") as f:
    disk = [int(x) for x in f.read().strip()]

pos = 0
files = []
gaps = []
for i, size in enumerate(disk):
    if i % 2 == 0:
        files.append((pos, size))
    else:
        gaps.append((pos, size))
    pos += size

for i in range(len(files) - 1, -1, -1):
    file_pos, file_size = files[i]
    for j in range(len(gaps)):
        gap_pos, gap_size = gaps[j]
        if gap_size >= file_size:
            files[i] = (gap_pos, file_size)
            gaps[j] = (gap_pos + file_size, gap_size - file_size)
            break
    if gaps:
        del gaps[-1]

ans = 0
for num, (pos, size) in enumerate(files):
    for i in range(pos, pos + size):
        ans += i * num

print(ans)
