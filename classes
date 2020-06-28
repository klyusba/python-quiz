class A:
    def __init__(self):
        self.a = 1


class B:
    a = 1


class C(A):
    a = 2


# print(A.a)
print('01:', A().a)
print('02:', B.a)
print('03:', B().a)
print('04:', C.a)
print('05:', C().a)

class L:
    a = []

class M(L):
    def __init__(self):
        self.a = []

class N(L):
    def __init__(self):
        pass

L.a.append(1)
print('06:', L.a)
M.a.append(1)
print('07:', M.a)
m = M()
m.a.append(1)
print('08:', M.a, m.a)
n = N()
print('09:', N.a, n.a)


class D(A):
    def __init__(self):
        super().__init__()
        self.b = 1


class E(D):
    def __init__(self):
        super().__init__()
        self.c = self.a + self.b


print('10:', D().a, D().b)
print('11:', E().c)
