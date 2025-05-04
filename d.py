s = input()
stack = []
mapping = {")": "(", "}": "{", "]": "["}
is_valid = True

for char in s:
    if char not in mapping:
        stack.append(char)
    else:
        if not stack or stack[-1] != mapping[char]:
            is_valid = False
            break
        stack.pop()

if stack:
    is_valid = False

print(is_valid)
