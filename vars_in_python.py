  bar = [2, 2]


# ==  1  ==
def foo(bar):
    bar = sum(bar)
    return bar
print(foo(bar))


# ==  2  ==
def foo(bar):
    bar[0] = 1
    return sum(bar)
print(foo(bar))


# ==  3  ==
def foo():
    bar = sum(bar)
    return bar
print(foo())


# ==  4  ==
def foo(bar):
    bar = [1, 2, 3, ]
    return sum(bar)
print(foo(bar), bar)


# ==  5  ==
def foo(bar):
    bar[:] = [1, 2, 3, ]
    return sum(bar)
print(foo(bar), bar)


# ==  6  ==
try:
    bar = 1 / 0
    print(bar)
except ZeroDivisionError as bar:
    print(bar)
print(bar)
