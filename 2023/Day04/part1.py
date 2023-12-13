with open("2023/Day04/input.txt") as f:
    lines = f.read().splitlines()

sum = 0
for line in lines:
    winning_nums, your_nums = line[line.find(":") + 1 :].split("|")
    winning_nums = winning_nums.split()
    your_nums = your_nums.split()
    num_same = len(set(winning_nums).intersection(set(your_nums)))
    if num_same:
        sum += 2 ** (num_same - 1)
print(sum)
