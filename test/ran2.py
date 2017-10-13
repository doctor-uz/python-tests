from random import randint

ls = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
n = len(ls)

x = round(n / 9)
y = 2


for i in range(y):

    index = randint(0, n)
    del ls[index]
    ls.insert(index, randint(0, 0))

print(ls)