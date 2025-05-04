nums = list(map(int, input().split()))
k = int(input())

count = 0

n = len(nums)

hashmap = {}

for i in nums:
    hashmap[i] = hashmap.get(i, 0) + 1

for x in hashmap:
    target = k - x
    if target in hashmap:
        if x == target:
            num_x = hashmap[x]
            if num_x >= 2:
                count += num_x * (num_x - 1) // 2
        elif x < target:
            count += hashmap[x] * hashmap[target]

print(count)
