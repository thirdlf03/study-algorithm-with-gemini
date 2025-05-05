n, W = map(int, input().split())

weights = []
values = []
for _ in range(n):
    w_i, v_i = map(int, input().split())
    weights.append(w_i)
    values.append(v_i)

memos = [0 for _ in range(W + 1)]

for i in range(0, n):
    w = weights[i]
    for j in range(w, W + 1):
        memos[j] = max(memos[j], memos[j - w] + values[i])
    print(memos)
print(memos[W])
