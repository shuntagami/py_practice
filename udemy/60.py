t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)
r = [i for i in t]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i*j for i in t for j in t2]
print(r)