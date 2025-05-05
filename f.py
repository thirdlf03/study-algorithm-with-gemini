from collections import Counter

nums = list(map(int, input().split()))

counter = Counter(nums)
common = counter.most_common(1)[0]
print(common[0])
