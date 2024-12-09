with open("2024/Day09/input.txt", "r") as f:
    disk = [int(x) for x in f.read().strip()]

s = []
for i, x in enumerate(disk):
    num = i // 2 if i % 2 == 0 else -1
    for _ in range(x):
        s.append(num)

i = 0
j = len(s) - 1
while i < j:
    if s[i] != -1:
        i += 1
        continue
    if s[j] == -1:
        j -= 1
        continue
    s[i] = s[j]
    s[j] = -1

n = i
ans = 0
for i in range(n):
    ans += i * s[i]

print(ans)
