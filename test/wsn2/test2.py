import math
import numpy as np
import sys
from random import randint
import random

ls1 = [0.6, 0.6, 0.6, 0.6]
ls2 = [0.6, 0.6, 0.6, 0.6, 0.6]


e = 0.03
u = 0.75
l = 0.05
n1 = len(ls1)
x = round(n/4)

last = []

# for i in range(x):
#     index = randint(0, n - 1)
#     while index in last:
#         index = randint(0, n - 1)
#     last.append(index)
#     del ls[index]
#     ls.insert(index, randint(0, 0))
# print(ls)

sys.stdout = open('wsn2.txt', 'w')
for h in range(5):
    print(0, 1.0)

for iii in range(1):
    lst = [ls1, ls2]
    ran = random.choice(lst)
if ran == ls1:
    for i in range(x):
    index = randint(0, n - 1)
    while index in last:
        index = randint(0, n - 1)
    last.append(index)
    del ran[index]
    ran.insert(index, randint(0, 0))
    print(ran)
v = sum(ls1)/n1
with open("wsn2.txt", "a") as f:
    for j in range(5):
        g = 1-(abs(v - 0.6) - e)/(u-l)
        print(x, g)

