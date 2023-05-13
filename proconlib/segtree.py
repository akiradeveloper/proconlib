# https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71

class SegTree:
    def __init__(self, N, X_f):
        self.N = N
        self.X_f = X_f
        self.X = [self.X_f()] * (N + N)

    def set_val(self, i, x):
        i += self.N
        self.X[i] = x
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
        L += self.N
        R += self.N
        vL = self.X_f()
        vR = self.X_f()
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self.X[L])
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self.X[R], vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)


class LazySegTree:
    def __init__(self, N, X_f, A_f, g):
        self.N = N
        self.X_f = X_f
        self.A_f = A_f
        self.g = g
        self.X = [self.X_f()] * (N + N)
        self.A = [self.A_f()] * (N + N)

    def build(self, seq):
        for i, x in enumerate(seq, self.N):
            self.X[i] = x
        for i in range(self.N - 1, 0, -1):
            self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def _eval_at(self, i):
        return self.g(self.X[i], self.A[i])

    def _propagate_at(self, i):
        self.X[i] = self._eval_at(i)
        self.A[i << 1] = self.A_f(self.A[i << 1], self.A[i])
        self.A[i << 1 | 1] = self.A_f(self.A[i << 1 | 1], self.A[i])
        self.A[i] = self.A_f()

    def _propagate_above(self, i):
        H = i.bit_length() - 1
        for h in range(H, 0, -1):
            self._propagate_at(i >> h)

    def _recalc_above(self, i):
        while i > 1:
            i >>= 1
            self.X[i] = self.X_f(self._eval_at(i << 1), self._eval_at(i << 1 | 1))

    def set_val(self, i, x):
        i += self.N
        self._propagate_above(i)
        self.X[i] = x
        self.A[i] = self.A_f()
        self._recalc_above(i)

    def fold(self, L, R):
        L += self.N
        R += self.N
        self._propagate_above(L // (L & -L))
        self._propagate_above(R // (R & -R) - 1)
        vL = self.X_f()
        vR = self.X_f()
        while L < R:
            if L & 1:
                vL = self.X_f(vL, self._eval_at(L))
                L += 1
            if R & 1:
                R -= 1
                vR = self.X_f(self._eval_at(R), vR)
            L >>= 1
            R >>= 1
        return self.X_f(vL, vR)

    def operate_range(self, L, R, x):
        L += self.N
        R += self.N
        L0 = L // (L & -L)
        R0 = R // (R & -R) - 1
        self._propagate_above(L0)
        self._propagate_above(R0)
        while L < R:
            if L & 1:
                self.A[L] = self.A_f(self.A[L], x)
                L += 1
            if R & 1:
                R -= 1
                self.A[R] = self.A_f(self.A[R], x)
            L >>= 1
            R >>= 1
        self._recalc_above(L0)
        self._recalc_above(R0)