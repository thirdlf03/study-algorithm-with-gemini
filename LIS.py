class SegmentTree:
    def __init__(self, base_list):
        self.size = len(base_list)
        self.n = 1
        while self.n < self.size:
            self.n *= 2
        self.node = [0 for _ in range(2 * self.n - 1)]

    def update(self, x, val):
        x += self.n - 1
        self.node[x] = val
        parent = (x - 1) // 2
        while parent >= 0:
            self.node[parent] = max(
                self.node[2 * parent + 1], self.node[2 * parent + 2]
            )
            parent = (parent - 1) // 2

    def get_max(self, a, b, k=0, l=0, r=-1):
        if r < 0:
            r = self.n

        if r <= a or b <= l:
            return 0

        if a <= l and r <= b:
            return self.node[k]

        mid = (l + r) // 2
        vl = self.get_max(a, b, 2 * k + 1, l, mid)
        vr = self.get_max(a, b, 2 * k + 2, mid, r)
        return max(vl, vr)

    def print_max(self):
        print(self.node[0])


def coord_compress(datas):
    S = sorted(list(set(datas)))
    ranking = {x: i for i, x in enumerate(S)}

    compress = []
    for data in datas:
        compress.append(ranking[data])
    return compress, len(S)


datas = list(map(int, input().split()))
compress, unique = coord_compress(datas)


seg = SegmentTree([0] * unique)

for i in compress:
    max_value = seg.get_max(0, i) + 1
    seg.update(i, max_value)
seg.print_max()
