n, w = map(int, input().split())
weights = []
values = []

for i in range(n):
    w_i, v_i = map(int, input().split())
    weights.append(w_i)
    values.append(v_i)

memo = [0 for _ in range(w + 1)]

for i in range(n):
    for j in range(w, weights[i] - 1, -1):
        memo[j] = max(memo[j], memo[j - weights[i]] + values[i])
print(memo[w])
