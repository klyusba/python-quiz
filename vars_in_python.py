# ==  1  ==
bar = [1, 2]

def foo(bar):
    bar = sum(bar)
    return bar
print(foo(bar))


# ==  2  ==
bar = [1, 2]

def foo(bar):
    bar[0] = 1
    return sum(bar)
print(foo(bar))


# ==  3  ==
bar = [1, 2]

def foo():
    bar = sum(bar)
    return bar
print(foo())


# ==  4  ==
bar = [1, 2]

def foo(bar):
    bar = [1, 2, 3, ]
    return sum(bar)
print(foo(bar), bar)


# ==  5  ==
bar = [1, 2]

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


# ==  7  ==
bar = [1, 2]

print(list(bar for bar in bar))
print(bar)


# ==  8  ==
bar = [1, 2]

f = lambda: sum(bar)
print(f())
bar = [1, 2, 3, ]
print(f())


# ==  9  ==
bar = [1, 2]

def foo(bar):
    return lambda: sum(bar)

f = foo(bar)
print(f())
bar = [1, 2, 3, ]
print(f())


# ==  10  ==
bar = [1, 2]

foo = []
for i in bar:
    foo.append(lambda: i)

print([f() for f in foo])

# ==  11  ==
bar = [1, 2]

foo = [
    lambda: i
    for i in bar
]
print(list(f() for f in foo))


# ==  12  ==
bar = [1, 2]

foo = [
    lambda: i
    for i in bar
]
print(list(f() for f in foo))
bar = [1, 2, 3, ]
print(list(f() for f in foo))
bar[:] = [1, 2, 3, ]
print(list(f() for f in foo))


# ==  13  ==
bar = [1, 2]

foo = [
    lambda i=i: i
    for i in bar
]
print(list(f() for f in foo))
