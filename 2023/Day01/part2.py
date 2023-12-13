import re

DIGITS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("2023/Day01/input.txt") as f:
    lines = f.readlines()

sum = 0
for line in lines:
    matches = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    calibration_value = DIGITS[matches[0]] * 10 + DIGITS[matches[-1]]
    sum += calibration_value

print(sum)
