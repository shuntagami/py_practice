def g():
    for i in range(10):
        yield i

g = g()

g = (i for i in range(10) if i % 2 == 0)

for x in g:
    print(x)
print(type(g))
