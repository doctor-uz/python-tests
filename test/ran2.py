from random import randint
 
ls = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
 
n = len(ls)
x = round(n/9)
y = 2
z = 3
last = []
for i in range(y):
    index = randint(0, n-1)
    while index in last :
        index = randint(0, n-1)
    last.append(index)
    del ls[index]
    ls.insert(index, randint(0, 0))
 
print(ls)
print(last)
 
v = sum(ls)/n
print(v)

g = 1-(abs(v - 0.6))/(0.75 - 0.05)
print(g)
