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


data = [0, 1, 2, 3]
s = SegmentTree(base_list=data)
s.update(0, -1)
print(s.get_min(0, 2))
print(s.node)
