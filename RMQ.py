class SegmentTree:
    def __init__(self, base_n):
        self.base_size = base_n
        self.n = 1
        while self.n < self.base_size:
            self.n *= 2

        self.INF = -100000000
        self.node = [0 for _ in range(2 * self.n - 1)]

    def update(self, x, val):
        x += self.n - 1
        self.node[x] = val

        parent = (x - 1) // 2
        while parent >= 0:
            self.node[parent] = max(
                self.node[parent * 2 + 1], self.node[parent * 2 + 2]
            )
            parent = (parent - 1) // 2

    def get_max(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.n

        if r <= a or b <= l:
            return self.INF

        if a <= l and r <= b:
            return self.node[k]

        vl = self.get_max(a, b, 2 * k + 1, l, (l + r) // 2)
        vr = self.get_max(a, b, 2 * k + 2, (l + r) // 2, r)
        return max(vl, vr)


N, Q = map(int, input().split())
queries = []
for i in range(Q):
    l, ll, lll = map(int, input().split())
    queries.append([l, ll, lll])
segtree = SegmentTree(N)

for query in queries:
    if query[0] == 1:
        segtree.update(query[1] - 1, query[2])
    else:
        print(segtree.get_max(query[1] - 1, query[2] - 1))
