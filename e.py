def check(nums, m, target):
    if max(nums) > target:
        return False

    split_count = 1
    current_sum = 0
    for num in nums:
        if current_sum + num <= target:
            current_sum += num
        else:
            split_count += 1
            current_sum = num
            if split_count > m:
                return False

    return split_count <= m


nums = list(map(int, input().split()))
m = int(input())

result = -1

search_min = max(nums) if nums else 0
search_max = sum(nums)
n = 0
while search_min <= search_max:
    n += 1
    potential_max_sum = (search_min + search_max) // 2
    is_valid = check(nums, m, potential_max_sum)
    if n == 20:
        break
    if is_valid:
        result = potential_max_sum
        search_max = potential_max_sum - 1
    else:
        search_min = potential_max_sum + 1

print(result)
