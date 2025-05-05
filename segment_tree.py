class SegmentTree:
    def __init__(self, base_list):
        self.base_size = len(base_list)
        self.n = 1
        while self.n < self.base_size:
            self.n *= 2

        self.INF = 100000000
        self.node = [self.INF for _ in range(2 * self.n - 1)]

        self._build(base_list)

    def _build(self, base_list):
        for i in range(self.base_size):
            self.node[i + self.n - 1] = base_list[i]

        for i in range(self.n - 2, -1, -1):
            self.node[i] = min(self.node[2 * i + 1], self.node[2 * i + 2])
        print(self.node)

    def update(self, x, val):
        x += self.n - 1
        self.node[x] = val

        parent = (x - 1) // 2
        while parent >= 0:
            self.node[parent] = min(
                self.node[parent * 2 + 1], self.node[parent * 2 + 2]
            )
            parent = (parent - 1) // 2

    def get_min(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.n

        if r <= a or b <= l:
            return self.INF

        if a <= l and r <= b:
            return self.node[k]

        vl = self.get_min(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.get_min(a, b, 2 * k + 2, (l + r) // 2, r)
        return min(vl, vr)


class LazySegmentTree:
    def __init__(self, base_list):
        self.size = len(base_list)
        self.n = 1
        while self.n < self.size:
            self.n *= 2

        self.node = [0 for _ in range(2 * self.n - 1)]
        self.lazy = [0 for _ in range(2 * self.n - 1)]
        self._build(base_list)

    def _build(self, base_list):
        for i in range(self.size):
            self.node[i + self.n - 1] = base_list[i]
        for i in range(self.n - 2, -1, -1):
            self.node[i] = self.node[2 * i + 1] + self.node[2 * i + 2]

    def eval(self, k, l, r):
        if self.lazy[k] != 0:
            self.node[k] += self.lazy[k]

            if r - l > 1:
                self.lazy[2 * k + 1] += self.lazy[k] // 2
                self.lazy[2 * k + 2] += self.lazy[k] // 2

            self.lazy[k] = 0

    def add(self, a, b, x, k=0, l=0, r=-1):
        if r < 0:
            r = self.n

        self.eval(k, l, r)

        if b <= l or r <= a:
            return

        if a <= l and r <= b:
            self.lazy[k] += (r - l) * x
            self.eval(k, l, r)
        else:
            self.add(a, b, x, 2 * k + 1, l, (l + r) // 2)
            self.add(a, b, x, 2 * k + 2, (l + r) // 2, r)
            self.node[k] = self.node[2 * k + 1] + self.node[2 * k + 2]

    def get_sum(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.n
        if b <= l or r <= a:
            return 0
        self.eval(k, l, r)
        if a <= l and r <= b:
            return self.node[k]
        vl = self.get_sum(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.get_sum(a, b, 2 * k + 2, (l + r) // 2, r)
        return vl + vr


data = [0, 1, 2, 3]

print("--- SegmentTree (Min) ---")
s = SegmentTree(base_list=data)
print(f"Initial Min Tree Node: {s.node}")
s.update(0, -1)
print("After update(0, -1):")
print(f"  Node: {s.node}")
min_val = s.get_min(0, 2)
print(f"  get_min(0, 2): {min_val}")  # Expected: -1

print("\n--- LazySegmentTree (Sum/Add) ---")
lazy_st = LazySegmentTree(base_list=data)
print(f"Initial Sum Tree Node: {lazy_st.node}")
print(f"Initial Lazy Array:    {lazy_st.lazy}")
sum_val1 = lazy_st.get_sum(0, 2)
print(f"Initial get_sum(0, 2): {sum_val1}")  # Expected: 1

print("\nCalling add(0, 2, 3)... (Add 3 to elements in [0, 2))")
lazy_st.add(0, 2, 3)
print("After add(0, 2, 3):")
print(f"  Node: {lazy_st.node}")
print(f"  Lazy: {lazy_st.lazy}")  # lazy propagation might have happened

sum_val2 = lazy_st.get_sum(0, 2)
print(f"\nget_sum(0, 2) after add:")
print(f"  Result: {sum_val2}")  # Expected: (0+3) + (1+3) = 7

print("\nState after get_sum (lazy values might have been propagated down):")
print(f"  Node: {lazy_st.node}")
print(f"  Lazy: {lazy_st.lazy}")
