from collections import Counter

with open("2024/Day01/input.txt", "r") as f:
    lines = f.read().splitlines()

x, y = zip(*((int(num) for num in line.split()) for line in lines))
y = Counter(y)
ans = sum(i * y[i] for i in x)
print(ans)
