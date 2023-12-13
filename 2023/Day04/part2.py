with open("2023/Day04/input.txt") as f:
    lines = f.read().splitlines()

sum = 0
nums = [0] * len(lines)
nums[0] = 1
cur_num = 0
for i, line in enumerate(lines):
    cur_num += nums[i]
    sum += cur_num
    winning_nums, your_nums = line[line.find(":") + 1 :].split("|")
    winning_nums = winning_nums.split()
    your_nums = your_nums.split()
    num_same = len(set(winning_nums).intersection(set(your_nums)))
    if num_same:
        nums[i + 1] += cur_num
        if i + num_same + 1 < len(lines):
            nums[i + num_same + 1] -= cur_num
print(sum)
