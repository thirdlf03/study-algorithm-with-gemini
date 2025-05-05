nums = list(map(int, input().split()))
memos = [1 for _ in range(len(nums) + 1)]

for i in range(1, len(nums)):
    current_value = nums[i]

    max_length = 1
    for j in range(0, i):
        if nums[j] < current_value:
            max_length = max(max_length, memos[j] + 1)
    memos[i] = max_length

print(max(memos))
