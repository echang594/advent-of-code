with open("2024/Day07/input.txt", "r") as f:
    lines = f.read().splitlines()


def calc(i, total):
    global val, nums
    if i == len(nums):
        return total == val
    if total > val:
        return False
    return (
        calc(i + 1, total + nums[i])
        or calc(i + 1, total * nums[i])
        or calc(i + 1, int(str(total) + str(nums[i])))
    )


ans = 0
for line in lines:
    val, nums = line.split(":")
    val = int(val)
    nums = [int(x) for x in nums.split()]
    if calc(1, nums[0]):
        ans += val

print(ans)
