nums = list(map(int, input().split()))

k = int(input())

# 尺取り法

nums.sort()

count = 0
left = 0
right = len(nums) - 1

while left < right:
    current_num = nums[left] + nums[right]
    if current_num < k:
        left += 1
    elif current_num > k:
        right += -1
    else:
        if nums[left] == nums[right]:
            n = right - left + 1
            count += n * (n - 1) // 2
            break
        else:
            left_num_count = 1
            i = left + 1
            while i < right and nums[i] == nums[left]:
                left_num_count += 1
                i += 1

            right_num_count = 1
            j = right - 1
            while j > left and nums[j] == nums[right]:
                right_num_count += 1
                j -= 1

            count += (left_num_count) * (right_num_count)
            left += left_num_count
            right -= right_num_count
print(count)
