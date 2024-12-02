with open("2024/Day02/input.txt", "r") as f:
    lines = f.read().splitlines()


def safe(nums, inc, removed):
    for i in range(1, len(nums)):
        if not (1 <= (nums[i] - nums[i - 1] if inc else nums[i - 1] - nums[i]) <= 3):
            if removed:
                return False
            return safe(nums[max(i - 2, 0) : i - 1] + nums[i:], inc, True) or safe(
                nums[i - 1 : i] + nums[i + 1 :], inc, True
            )
    return True


ans = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    if safe(nums, True, False) or safe(nums, False, False):
        ans += 1

print(ans)
