from random import randint

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(ls)
x = round(n/9)
y = 2

for i in range(y):
    d = randint(1, n)
    del ls[d]
    ls.insert(d, randint(1, n))
print(ls)

v = sum(ls)/n
print(v)

