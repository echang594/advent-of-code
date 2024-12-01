with open("2024/Day01/input.txt", "r") as f:
    lines = f.read().splitlines()

x, y = zip(*((int(num) for num in line.split()) for line in lines))
x = sorted(x)
y = sorted(y)
ans = sum(abs(a - b) for a, b in zip(x, y))
print(ans)
