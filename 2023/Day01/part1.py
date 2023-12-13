def find_first_digit(s: str):
    for c in s:
        if c.isdigit():
            return int(c)


with open("2023/Day01/input.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    first_digit = find_first_digit(line)
    last_digit = find_first_digit(line[::-1])
    calibration_value = first_digit * 10 + last_digit
    sum += calibration_value

print(sum)
