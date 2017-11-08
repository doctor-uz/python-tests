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
x1 = round(n1/4)
last = []
n2 = len(ls2)
x2 = round(n2/5)
last2 = []


sys.stdout = open('wsn2.txt', 'w')
for h in range(5):
    print(0, 1.0)

for k in range(5):
    for iii in range(1):
        lst = [ls1, ls2]
        ran = random.choice(lst)

    if ran == ls2:
        for i in range(1):
            index2 = randint(0, n2 - 1)
        while index2 in last2:
            index2 = randint(0, n2 - 1)
        last2.append(index2)
        del ran[index2]
        ran.insert(index2, randint(0, 0))

        v2 = sum(ls2)/n2
        print(v2)

       # g2 = 1 - (abs(v2 - 0.6) - e) / (u - l)
       #  if g2 >= 1:
       #      g2 == 0.6
       #  else:
       #      g2 == v2

        ls2 = [0.6, 0.6, 0.6, 0.6, 0.6]
    elif ran == ls1:


        for i in range(1):
            index = randint(0, n1 - 1)
        while index in last:
            index = randint(0, n1 - 1)
        last.append(index)
        del ran[index]
        ran.insert(index, randint(0, 0))

        v = (sum(ls1)-0.6 + v2)/n1

        with open("wsn2.txt", "a") as f:
            for j in range(5):
                g1 = 1-(abs(v - 0.6) - e)/(u-l)
                print(x1, g1)

        ls1 = [0.6, 0.6, 0.6, 0.6]


